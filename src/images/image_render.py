import cv2
import streamlit as st
from PIL import Image

from src.frame_processing.frame_annotator import FrameAnnotator
from src.frame_processing.model_processor import ModelProcessor


class ImageRender:
    def __init__(self):
        self.model_processor = ModelProcessor()
        self.video_annotator = FrameAnnotator()

    def display_image(self, image_path):
        # Load the image
        image = cv2.imread(image_path)

        # Process the image
        processed_frame = self.model_processor.process_frame(image)[0]
        annotated_frame = self.video_annotator.annotate_frame(image, processed_frame)

        # Convert the processed image to a format suitable for display
        image_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image_rgb)

        # Display the image using Streamlit's image display method, ensuring it fits the column width
        st.image(image_pil, channels="RGB")
