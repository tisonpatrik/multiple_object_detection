import cv2
import streamlit as st
from PIL import Image
from supervision.utils.video import get_video_frames_generator

from src.video.processor import MediaProcessor


class VideoPlayer:
    def __init__(self):
        self.processor = MediaProcessor()
        self.frame_placeholder = st.empty()

    def display_video_frames(self, video_path, stride=1, start=0, end=None):
        frame_generator = get_video_frames_generator(
            source_path=video_path, stride=stride, start=start, end=end
        )
        iterator = iter(frame_generator)

        while True:
            try:
                frame = next(iterator)
                processed_frame = self.processor.process_video_frame(frame)

                # Convert the processed frame to a format suitable for display
                frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
                frame_pil = Image.fromarray(frame_rgb)
                self.frame_placeholder.image(frame_pil, channels="RGB")
            except StopIteration:
                # End of video or end reached as per 'end' parameter
                break
