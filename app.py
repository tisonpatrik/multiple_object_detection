import streamlit as st

from src.video_player import VideoPlayer
from src.video_utils import save_temporary_video


def main():
    player = VideoPlayer()
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])

    if uploaded_file is not None:
        # Detect changes in the uploaded file
        if (
            "last_uploaded_file" not in st.session_state
            or st.session_state.last_uploaded_file != uploaded_file.name
        ):
            st.session_state.last_uploaded_file = uploaded_file.name
            st.session_state.replay = True  # Set replay to True for new file

        st.write("Uploaded video")
        handle_replay(player, uploaded_file)


def handle_replay(player, uploaded_file):
    replay_button_clicked = st.button("Replay Video")

    if replay_button_clicked or st.session_state.replay:
        file_path = save_temporary_video(uploaded_file)
        player.display_video_frames(file_path)
        st.session_state.replay = False


if __name__ == "__main__":
    main()
