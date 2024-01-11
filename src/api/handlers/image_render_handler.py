import logging

import streamlit as st

from src.images.image_render import ImageRender
from src.utils.file_utils import save_temporary_file

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ImageHandler:
    def __init__(self):
        self.image_render = ImageRender()

    def handle_image(self, uploaded_file):
        try:
            file_path = save_temporary_file(uploaded_file)
            self.image_render.display_image(file_path)

        except Exception as e:
            logger.error(f"Error handling image: {e}")
            raise