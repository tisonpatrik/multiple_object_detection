import tempfile

import cv2
import streamlit as st
from PIL import Image

from processor import MediaProcessor

# Initialize the MediaProcessor
processor = MediaProcessor()

uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])

if uploaded_file is not None:
    st.write("Uploaded video")

    if uploaded_file.type == "video/mp4":
        # Save the video to a temporary file
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        tfile.write(uploaded_file.read())
        tfile.close()

        # Load video and process frame by frame
        video_stream = cv2.VideoCapture(tfile.name)

        # Create a placeholder for the video frame
        frame_placeholder = st.empty()

        while video_stream.isOpened():
            success, frame = video_stream.read()
            if not success:
                break
            processed_frame = processor.process_video_frame(frame)

            # Convert the processed frame to a format suitable for display
            frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_rgb)
            frame_placeholder.image(frame_pil, channels="RGB")

        video_stream.release()
