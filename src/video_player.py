import time

import cv2
import streamlit as st
from PIL import Image
from supervision.utils.video import get_video_frames_generator

from src.processor import MediaProcessor


class VideoPlayer:
    def __init__(self):
        self.processor = MediaProcessor()

    def display_video_frames(
        self, video_path, time_per_frame, stride=1, start=0, end=None
    ):
        frame_placeholder = st.empty()

        frame_generator = get_video_frames_generator(
            source_path=video_path, stride=stride, start=start, end=end
        )

        for frame in frame_generator:
            processed_frame = self.processor.process_video_frame(frame)

            # Convert the processed frame to a format suitable for display
            frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_rgb)
            frame_placeholder.image(frame_pil, channels="RGB")

            # Introduce delay to match the video's frame rate
            time.sleep(time_per_frame)
