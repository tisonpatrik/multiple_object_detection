import streamlit as st
from src.api.pages.image_page import ImagePage
from src.api.pages.video_page import VideoPlayerPage

def main():
    with st.sidebar:
        st.title("Menu")

        # Initialize the current page in session state
        if "current_page" not in st.session_state:
            st.session_state.current_page = "Video"
            st.session_state.pages = {
                "Video": VideoPlayerPage(),
                "Image": ImagePage()
            }

        # Sidebar buttons for page navigation
        if st.button("Video"):
            st.session_state.current_page = "Video"
        if st.button("Image"):
            st.session_state.current_page = "Image"

    # Get the page instance from session state and render it
    current_page = st.session_state.pages[st.session_state.current_page]
    current_page.render()

if __name__ == "__main__":
    main()
