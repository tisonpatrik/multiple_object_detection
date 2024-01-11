import os

import torch
from ultralytics import YOLO
from ultralytics.utils import autobatch

# Set the device to CUDA if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

curr_path = os.getcwd()
config_path = os.path.join(curr_path, "config.yaml")

# Initialize model and move it to the device
model = YOLO("yolov8s.yaml").load("yolov8s.pt")
model.to(device)

# Training process
results = model.train(
    data=config_path,
    epochs=300,
    batch=-1,
    patience=20,
)
