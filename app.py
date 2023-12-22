import streamlit as st

from src.pages.analyze_page import AnalyzePage


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

    # Instantiate page classes
    analyze_page = AnalyzePage()
    # Render the appropriate page based on current page
    if st.session_state.current_page == "Analyze":
        analyze_page.render()


if __name__ == "__main__":
    main()
