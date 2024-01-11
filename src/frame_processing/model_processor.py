import os

from scipy.__config__ import show
from ultralytics import YOLO


class ModelProcessor:
    def __init__(self):
        self.model = YOLO(self._determine_model_path())

    def process_frame(self, frame):
        results = self.model(frame, show=False, conf=0.25)
        return results

    def _determine_model_path(self):
        model_path = "runs/detect/train/weights/best.pt"
        return model_path if os.path.exists(model_path) else "yolov8s.pt"
