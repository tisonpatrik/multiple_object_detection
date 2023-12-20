import os

from ultralytics import YOLO
from ultralytics.utils import autobatch

curr_path = os.getcwd()
config_path = os.path.join(curr_path, "config.yaml")


model = YOLO("yolov8n.yaml").load("yolov8n.pt")
optimal_batch_size = autobatch.autobatch(model, imgsz=640, fraction=0.6)
results = model.train(
    data=config_path,
    epochs=100,
    batch=optimal_batch_size,
    iou=0.5,
    conf=0.01,
    patience=50,
)
