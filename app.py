import streamlit as st

from src.handlers.replay_handler import ReplayHandler
from src.pages.analyze_page import AnalyzePage
from src.pages.train_page import TrainPage

replay_handler = ReplayHandler()


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

    analyze_page = AnalyzePage()
    train_page = TrainPage()
    # Call the appropriate page function based on current page
    if st.session_state.current_page == "Analyze":
        analyze_page.render()
    elif st.session_state.current_page == "Train":
        train_page.train()


if __name__ == "__main__":
    main()
