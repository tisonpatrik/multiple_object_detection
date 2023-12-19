import streamlit as st

from src.pages.analyze_page import AnalyzePage
from src.pages.train_page import TrainPage


def main():
    # Sidebar setup using 'with' notation
    with st.sidebar:
        st.title("Menu")

        # Initialize the current page in session state
        if "current_page" not in st.session_state:
            st.session_state.current_page = "Analyze"

        # Sidebar buttons for page navigation
        if st.button("Analyze"):
            st.session_state.current_page = "Analyze"
        if st.button("Train"):
            st.session_state.current_page = "Train"

    # Instantiate page classes
    analyze_page = AnalyzePage()
    train_page = TrainPage()

    # Render the appropriate page based on current page
    if st.session_state.current_page == "Analyze":
        analyze_page.render()
    elif st.session_state.current_page == "Train":
        train_page.train()


if __name__ == "__main__":
    main()
