import streamlit as st

from src.handlers.replay_handler import ReplayHandler


class AnalyzePage:
    def __init__(self):
        self.replay_handler = ReplayHandler()

    def render(self):
        uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])

        if uploaded_file is not None:
            if (
                "last_uploaded_file" not in st.session_state
                or st.session_state.last_uploaded_file != uploaded_file.name
            ):
                st.session_state.last_uploaded_file = uploaded_file.name
                st.session_state.replay = True

            st.write("Uploaded video")
            self.replay_handler.handle_replay(uploaded_file)
