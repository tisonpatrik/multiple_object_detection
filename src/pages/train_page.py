import streamlit as st

from src.training.trainer import Trainer


class TrainPage:
    def __init__(self):
        self.trainer = Trainer()

    def train(self):
        st.write("Train your model here.")

        # Step 1: User uploads images
        uploaded_images = st.file_uploader(
            "Upload images", accept_multiple_files=True, type=["png", "jpg", "jpeg"]
        )

        # User uploads label files
        uploaded_labels = st.file_uploader(
            "Upload label files", accept_multiple_files=True, type=["txt"]
        )
        # Step 3: User initiates the training process
        if st.button("Train Model"):
            if uploaded_images and uploaded_labels:
                # Train the model
                self.trainer.start_training(uploaded_images, uploaded_labels)

                st.write("Training started!")
            else:
                st.write("Please upload both images and label files to start training.")
