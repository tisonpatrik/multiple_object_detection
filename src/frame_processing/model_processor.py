import os

from scipy.__config__ import show
from ultralytics import YOLO


class ModelProcessor:
    def __init__(self):
        self.model_path = self._determine_model_path()
        self.model = YOLO(self.model_path)
        self.print_model_info()

    def process_frame(self, frame):
        results = self.model(frame, show=False, conf=0.25)
        return results

    def _determine_model_path(self):
        model_path = "best.pt"
        return model_path if os.path.exists(model_path) else "yolov8n.pt"

    def print_model_info(self):
        if self.model_path == "yolov8n.pt":
            print("Default yolov8n.pt model is used")
        else:
            print("Custom model is used")
