import os

import torch
from ultralytics import YOLO
from ultralytics.utils import autobatch
import os
import shutil

# Set the device to CUDA if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

root = os.getcwd()
config_path = os.path.join(root, "config.yaml")

# Initialize model and move it to the device
model = YOLO("yolov8n.yaml").load("yolov8n.pt")
model.to(device)


# Training process
results = model.train(
    data=config_path,
    epochs=300,
    batch=10, # setup this value to fit your GPU memory, 10 is just an example. for auto batch us -1 value
    patience=50,
)


# Find the directory with the highest number in curr_path/runs
runs_dir = os.path.join(root, "runs/detect")
highest_dir = max(sorted(os.listdir(runs_dir)))
highest_dir_path = os.path.join(runs_dir, highest_dir)

# Copy the best.pt file to curr_path
best_pt_path = os.path.join(highest_dir_path, "weights", "best.pt")
shutil.copy(best_pt_path, root)