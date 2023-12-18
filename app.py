import streamlit as st

from src.video_player import VideoPlayer
from src.video_utils import save_temporary_video


def main():
    st.sidebar.title("Menu")

    # Initialize the current page in session state
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Analyze"

    # Sidebar buttons for page navigation
    if st.sidebar.button("Analyze"):
        st.session_state.current_page = "Analyze"
    if st.sidebar.button("Train"):
        st.session_state.current_page = "Train"

    # Call the appropriate page function based on current page
    if st.session_state.current_page == "Analyze":
        analyze_page()
    elif st.session_state.current_page == "Train":
        train_page()


def analyze_page():
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])

    if uploaded_file is not None:
        if (
            "last_uploaded_file" not in st.session_state
            or st.session_state.last_uploaded_file != uploaded_file.name
        ):
            st.session_state.last_uploaded_file = uploaded_file.name
            st.session_state.replay = True

        st.write("Uploaded video")
        handle_replay(uploaded_file)


def train_page():
    st.write("Train your model here.")


def handle_replay(uploaded_file):
    player = VideoPlayer()
    replay_button_clicked = st.button("Replay Video")

    if replay_button_clicked or st.session_state.replay:
        file_path = save_temporary_video(uploaded_file)
        player.display_video_frames(file_path)
        st.session_state.replay = False


if __name__ == "__main__":
    main()
