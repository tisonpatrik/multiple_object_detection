import time

import cv2
import streamlit as st
from PIL import Image
from supervision.utils.video import get_video_frames_generator

from src.video_player import VideoPlayer
from src.video_utils import get_video_fps, save_temporary_video

player = VideoPlayer()

uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])

# Initialize or get the state variable for replay
if "replay" not in st.session_state:
    st.session_state.replay = False


def play_video():
    st.session_state.replay = True


if uploaded_file is not None:
    st.write("Uploaded video")

    # Button to replay the video
    if st.button("Replay Video"):
        play_video()

    file_path = save_temporary_video(uploaded_file)
    time_per_frame = get_video_fps(file_path)

    # Play the video initially or when replay is triggered
    if not st.session_state.replay:
        player.display_video_frames(file_path, time_per_frame)
    elif st.session_state.replay:
        st.session_state.replay = False  # Reset the replay state
        player.display_video_frames(file_path, time_per_frame)
