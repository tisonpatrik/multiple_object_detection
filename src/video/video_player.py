import cv2
import streamlit as st
from PIL import Image
from supervision.utils.video import get_video_frames_generator

from src.frame_processing.model_processor import ModelProcessor
from src.frame_processing.frame_annotator import FrameAnnotator


class VideoPlayer:
    def __init__(self):
        self.video_annotator = FrameAnnotator()
        self.model_processor = ModelProcessor()
        self.frame_placeholder = st.empty()

    def display_video_frames(self, video_path, stride=1, start=0, end=None):
        frame_generator = get_video_frames_generator(
            source_path=video_path, stride=stride, start=start, end=end
        )

        while True:
            try:
                frame = next(iter(frame_generator))
                processed_frame = self.model_processor.process_frame(frame)[0]
                annotated_frame = self.video_annotator.annotate_frame(frame, processed_frame)

                # Convert the processed frame to a format suitable for display
                frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                frame_pil = Image.fromarray(frame_rgb)
                self.frame_placeholder.image(frame_pil, channels="RGB")
            except StopIteration:
                # End of video or end reached as per 'end' parameter
                break
