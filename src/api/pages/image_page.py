import streamlit as st

from src.api.handlers.image_render_handler import ImageHandler


class ImagePage:
    def __init__(self):
        self.image_handler = ImageHandler()

    def render(self):
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            if (
                "last_uploaded_file" not in st.session_state
                or st.session_state.last_uploaded_file != uploaded_file.name
            ):
                st.session_state.last_uploaded_file = uploaded_file.name
                st.session_state.replay = True

            st.write("Uploaded image")
            self.image_handler.handle_image(uploaded_file)
