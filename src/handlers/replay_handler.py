import streamlit as st

from src.video_player import VideoPlayer
from src.video_utils import save_temporary_video


class ReplayHandler:
    def __init__(self):
        self.player = VideoPlayer()
        self.frame_placeholder = st.empty()

    def handle_replay(self, uploaded_file):
        replay_button_clicked = st.button("Replay Video")

        if replay_button_clicked or st.session_state.replay:
            file_path = save_temporary_video(uploaded_file)
            self.player.display_video_frames(file_path)
            st.session_state.replay = False
