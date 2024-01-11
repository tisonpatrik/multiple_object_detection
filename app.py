import streamlit as st

from src.api.pages.image_page import ImagePage
from src.api.pages.video_page import VideoPlayerPage


def main():
    # Sidebar setup using 'with' notation
    with st.sidebar:
        st.title("Menu")

        # Initialize the current page in session state
        if "current_page" not in st.session_state:
            st.session_state.current_page = "Video"

        # Sidebar buttons for page navigation
        if st.button("Video"):
            st.session_state.current_page = "Video"
        if st.button("Image"):  # Add this line
            st.session_state.current_page = "Image"  # And this line

    # Instantiate page classes
    video_page = VideoPlayerPage()
    image_page = ImagePage()

    # Render the appropriate page based on current page
    if st.session_state.current_page == "Video":
        video_page.render()
    elif st.session_state.current_page == "Image":  # Change this line
        image_page.render()


if __name__ == "__main__":
    main()