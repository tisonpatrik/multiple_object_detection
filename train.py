import os

import torch
from ultralytics import YOLO
from ultralytics.utils import autobatch

# Set the device to CUDA if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

curr_path = os.getcwd()
config_path = os.path.join(curr_path, "config.yaml")

# Initialize model and move it to the device
model = YOLO("yolov8n.yaml").load("yolov8n.pt")
model.to(device)

# Compute optimal batch size using autobatch
# optimal_batch_size = autobatch.autobatch(model, imgsz=640, fraction=0.6)
# optimal_batch_size = min(optimal_batch_size, 3)
# Training process
results = model.train(
    data=config_path,
    epochs=100,
    batch=3,
    iou=0.5,
    conf=0.01,
    patience=50,
)
