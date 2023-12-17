import tempfile
import time

import cv2
import streamlit as st
from PIL import Image
from supervision.utils.video import get_video_frames_generator

from src.processor import MediaProcessor
from src.video_utils import get_video_fps, save_temporary_video

# Initialize the MediaProcessor
processor = MediaProcessor()

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

    # Create a placeholder for the video frame
    frame_placeholder = st.empty()

    # Function to display video frames
    def display_video_frames():
        for frame in get_video_frames_generator(file_path):
            processed_frame = processor.process_video_frame(frame)

            # Convert the processed frame to a format suitable for display
            frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_rgb)
            frame_placeholder.image(frame_pil, channels="RGB")

            # Introduce delay to match the video's frame rate
            time.sleep(time_per_frame)

    # Play the video initially or when replay is triggered
    if not st.session_state.replay:
        display_video_frames()
    elif st.session_state.replay:
        st.session_state.replay = False  # Reset the replay state
        display_video_frames()
