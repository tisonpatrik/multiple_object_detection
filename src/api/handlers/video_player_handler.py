import logging

import streamlit as st

from src.utils.file_utils import save_temporary_file
from src.video.video_player import VideoPlayer

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class VideoPlayerHandler:
    def __init__(self):
        self.player = VideoPlayer()

    def handle_video(self, uploaded_file):
        try:
            replay_button_clicked = st.button("Replay Video")

            if replay_button_clicked or st.session_state.replay:
                file_path = save_temporary_file(uploaded_file)
                self.player.display_video_frames(file_path)
                st.session_state.replay = False
        except Exception as e:
            logger.error(f"Error handling replay: {e}")
            raise
