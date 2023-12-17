import time

import cv2
import streamlit as st
from PIL import Image
from supervision.utils.video import get_video_frames_generator

from src.processor import MediaProcessor


class VideoPlayer:
    def __init__(self):
        self.processor = MediaProcessor()

    def display_video_frames(self, video_path, fps):
        frame_placeholder = st.empty()
        for frame in get_video_frames_generator(video_path):
            processed_frame = self.processor.process_video_frame(frame)

            # Convert the processed frame to a format suitable for display
            frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_rgb)
            frame_placeholder.image(frame_pil, channels="RGB")

            # Introduce delay to match the video's frame rate
            time.sleep(1.0 / fps)
