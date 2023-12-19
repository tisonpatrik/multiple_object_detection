import random

import streamlit as st
from PIL import Image


class TrainPage:
    def __init__(self):
        self.uploaded_files = None
        self.random_images = []

    def train(self):
        st.write("Train your model here.")

        # Step 1: User uploads images
        self.uploaded_files = st.file_uploader(
            "Upload images", accept_multiple_files=True, type=["png", "jpg", "jpeg"]
        )

        # User uploads label files
        uploaded_labels = st.file_uploader(
            "Upload label files", accept_multiple_files=True, type=["txt"]
        )
