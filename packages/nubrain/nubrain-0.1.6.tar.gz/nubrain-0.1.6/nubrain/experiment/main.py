import multiprocessing as mp
import os
import random
from time import sleep, time

import numpy as np
import pygame

from nubrain.device.device_interface import create_eeg_device
from nubrain.experiment.data import eeg_data_logging
from nubrain.experiment.global_config import GlobalConfig
from nubrain.image.tools import get_all_image_paths, load_and_scale_image
from nubrain.misc.datetime import get_formatted_current_datetime

mp.set_start_method("spawn", force=True)  # Necessary on if running on windows?


def experiment(config: dict):
    # ----------------------------------------------------------------------------------
    # *** Get config

    device_type = config["device_type"]
    lsl_stream_name = config.get("lsl_stream_name", "DSI-24")  # New config option

    subject_id = config["subject_id"]
    session_id = config["session_id"]

    output_directory = config["output_directory"]
    image_directory = config["image_directory"]

    eeg_channel_mapping = config.get("eeg_channel_mapping", None)

    utility_frequency = config["utility_frequency"]

    initial_rest_duration = config["initial_rest_duration"]
    image_duration = config["image_duration"]
    isi_duration = config["isi_duration"]
    isi_jitter = config["isi_jitter"]
    inter_block_grey_duration = config["inter_block_grey_duration"]

    n_blocks = config["n_blocks"]
    images_per_block = config["images_per_block"]

    eeg_device_address = config.get("eeg_device_address", None)

    global_config = GlobalConfig()

    # ----------------------------------------------------------------------------------
    # *** Test if output path exists

    if not os.path.isdir(output_directory):
        raise AssertionError(f"Target directory does not exist: {output_directory}")

    current_datetime = get_formatted_current_datetime()
    path_out_data = os.path.join(output_directory, f"eeg_session_{current_datetime}.h5")

    if os.path.isfile(path_out_data):
        raise AssertionError(f"Target file already exists: {path_out_data}")

    # ----------------------------------------------------------------------------------
    # *** Get image paths

    image_file_paths = get_all_image_paths(image_directory=image_directory)

    if not image_file_paths:
        raise AssertionError(f"Found no images at {image_directory}")
    print(f"Found {len(image_file_paths)} images")

    # ----------------------------------------------------------------------------------
    # *** Prepare EEG measurement

    # Create EEG device
    print(f"Initializing EEG device: {device_type}")

    device_kwargs = {
        "eeg_channel_mapping": eeg_channel_mapping,
    }

    if device_type in ["cyton", "synthetic"]:
        device_kwargs["eeg_device_address"] = eeg_device_address
    elif device_type == "dsi24":
        device_kwargs["lsl_stream_name"] = lsl_stream_name
    else:
        raise ValueError(f"Unexpected `device_type`: {device_type}")

    eeg_device = create_eeg_device(device_type, **device_kwargs)

    # Prepare session
    eeg_device.prepare_session()

    # Need to start the stream before calling `eeg_device.get_device_info()`, because
    # we retrieve data from board to determine data shape (number of channels).
    eeg_device.start_stream()
    sleep(0.1)

    # Get device info.
    device_info = eeg_device.get_device_info()
    eeg_board_description = device_info["board_description"]
    eeg_sampling_rate = device_info["sampling_rate"]
    eeg_channels = device_info["eeg_channels"]
    marker_channel = device_info["marker_channel"]
    n_channels_total = device_info["n_channels_total"]

    print(f"Board: {eeg_board_description['name']}")
    print(f"Sampling Rate: {eeg_sampling_rate} Hz")
    print(f"EEG Channels: {eeg_channels}")
    print(f"Marker Channel: {marker_channel}")

    board_data = eeg_device.get_board_data()

    print(f"Board data dtype: {board_data.dtype}")
    print(f"Board data shape: {board_data.shape}")

    # ----------------------------------------------------------------------------------
    # *** Start data logging subprocess

    data_logging_queue = mp.Queue()

    subprocess_params = {
        "device_type": device_type,
        "subject_id": subject_id,
        "session_id": session_id,
        "image_directory": image_directory,
        # EEG parameters
        "eeg_board_description": eeg_board_description,
        "eeg_sampling_rate": eeg_sampling_rate,
        "n_channels_total": n_channels_total,
        "eeg_channels": eeg_channels,
        "marker_channel": marker_channel,
        "eeg_channel_mapping": eeg_channel_mapping,
        "eeg_device_address": eeg_device_address,
        # Timing parameters
        "initial_rest_duration": initial_rest_duration,
        "image_duration": image_duration,
        "isi_duration": isi_duration,
        "inter_block_grey_duration": inter_block_grey_duration,
        # Experiment structure
        "n_blocks": n_blocks,
        "images_per_block": images_per_block,
        # Misc
        "utility_frequency": utility_frequency,
        "path_out_data": path_out_data,
        "data_logging_queue": data_logging_queue,
    }

    logging_process = mp.Process(
        target=eeg_data_logging,
        args=(subprocess_params,),
    )

    logging_process.daemon = (
        True  # Use lowercase 'daemon' for cross-platform compatibility
    )
    logging_process.start()

    # ----------------------------------------------------------------------------------
    # *** Start experiment

    running = True
    while running:
        pygame.init()

        # Get screen dimensions and set up full screen
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h
        screen = pygame.display.set_mode(
            (screen_width, screen_height), pygame.FULLSCREEN
        )
        pygame.display.set_caption("Image Presentation Experiment")
        pygame.mouse.set_visible(False)  # Hide the mouse cursor

        font = pygame.font.Font(None, 48)  # Basic font for messages

        # Load first image.
        image_and_metadata = None
        while image_and_metadata is None:
            # Select a random image from the full list.
            random_image_file_path = random.choice(image_file_paths)
            image_and_metadata = load_and_scale_image(
                image_file_path=random_image_file_path,
                screen_width=screen_width,
                screen_height=screen_height,
            )

        try:
            # Initial grey screen.
            pygame.time.wait(100)
            screen.fill(global_config.rest_condition_color)
            pygame.display.flip()
            pygame.time.wait(100)
            screen.fill(global_config.rest_condition_color)
            pygame.display.flip()

            # Clear board buffer.
            _ = eeg_device.get_board_data()

            # Pause for specified number of milliseconds.
            pygame.time.delay(int(round(initial_rest_duration * 1000.0)))

            # Block loop.
            for idx_block in range(n_blocks):
                print(f"Starting Block {idx_block + 1} out of {n_blocks}")

                # Image loop (within a block).
                for image_count in range(images_per_block):
                    if not running:
                        break  # Check for quit event

                    image_file_path = image_and_metadata["image_file_path"]
                    current_image = image_and_metadata["image"]
                    image_category = image_and_metadata["image_category"]

                    img_rect = current_image.get_rect(
                        center=(screen_width // 2, screen_height // 2)
                    )

                    # Display image. Clear previous screen content.
                    screen.fill(global_config.rest_condition_color)
                    screen.blit(current_image, img_rect)
                    pygame.display.flip()

                    # Start of stimulus presentation.
                    t1 = time()
                    # Insert stimulus start marker into EEG data.
                    eeg_device.insert_marker(global_config.stim_start_marker)

                    # Send pre-stimulus board data (to avoid buffer overflow).
                    data_to_queue = {
                        "board_data": eeg_device.get_board_data(),
                        "stimulus_data": None,
                    }
                    data_logging_queue.put(data_to_queue)

                    # Time until when to show stimulus.
                    t2 = t1 + image_duration
                    while time() < t2:
                        pass

                    # End of stimulus presentation. Display ISI grey screen.
                    screen.fill(global_config.rest_condition_color)
                    pygame.display.flip()
                    t3 = time()
                    eeg_device.insert_marker(global_config.stim_end_marker)

                    # Send data corresponding to stimulus period.
                    stimulus_data = {
                        "stimulus_start_time": t1,
                        "stimulus_end_time": t3,
                        "stimulus_duration_s": t3 - t1,
                        "image_file_path": image_file_path,
                        "image_category": image_category,
                    }
                    data_to_queue = {
                        "board_data": eeg_device.get_board_data(),
                        "stimulus_data": stimulus_data,
                    }
                    data_logging_queue.put(data_to_queue)

                    # Load next image.
                    image_and_metadata = None
                    while image_and_metadata is None:
                        # Select a random image from the full list.
                        random_image_file_path = random.choice(image_file_paths)
                        image_and_metadata = load_and_scale_image(
                            image_file_path=random_image_file_path,
                            screen_width=screen_width,
                            screen_height=screen_height,
                        )

                    # Time until when to show grey screen.
                    t4 = t3 + isi_duration + np.random.uniform(low=0.0, high=isi_jitter)
                    while time() < t4:
                        pass

                    # Event handling (allow quitting with ESC or window close).
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False

                    if not running:
                        break

                if not running:
                    break

                # Send post-stimulus board data (to avoid buffer overflow).
                data_to_queue = {
                    "board_data": eeg_device.get_board_data(),
                    "stimulus_data": None,
                }
                data_logging_queue.put(data_to_queue)

                # Inter-block grey screen.
                print(f"End of Block {idx_block + 1}. Starting inter-block interval.")
                screen.fill(global_config.rest_condition_color)
                pygame.display.flip()
                # We already waited for the ISI duration, therefore subtract it from the
                # inter block duration. Avoid negative value in case ISI duration is
                # longer than inter block duration.
                remaining_wait = max((inter_block_grey_duration - isi_duration), 0.0)
                pygame.time.delay(int(round(remaining_wait * 1000.0)))

            # End of experiment.
            if running:  # Only show if not quit early
                screen.fill(global_config.rest_condition_color)
                end_text = font.render("Experiment complete.", True, (0.0, 0.0, 0.0))
                text_rect = end_text.get_rect(
                    center=(screen_width // 2, screen_height // 2)
                )
                screen.blit(end_text, text_rect)
                pygame.display.flip()
                pygame.time.wait(500)

            running = False

            # Send final board data.
            data_to_queue = {
                "board_data": eeg_device.get_board_data(),
                "stimulus_data": None,
            }
            data_logging_queue.put(data_to_queue)

        except Exception as e:
            print(f"An error occurred during the experiment: {e}")
            running = False
        finally:
            pygame.quit()
            print("Experiment closed.")

    eeg_device.stop_stream()
    eeg_device.release_session()

    # Join process for sending data.
    print("Join process for sending data")
    data_logging_queue.put(None)
    logging_process.join()
