import supervision as sv
from supervision.draw.color import ColorPalette
from ultralytics import YOLO


class MediaProcessor:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")
        self.class_names_dict = self.model.model.names
        pass

    def process_video_frame(self, frame):
        results = self.model(frame)
        box_annotator = sv.BoundingBoxAnnotator(
            color=ColorPalette.default(),  # Use the default color palette
            thickness=4,
        )
        detections = sv.Detections(
            xyxy=results[0].boxes.xyxy.cpu().numpy(),
            confidence=results[0].boxes.conf.cpu().numpy(),
            class_id=results[0].boxes.cls.cpu().numpy().astype(int),
        )
        labels = [
            f"{self.class_names_dict[class_id]} {conf:0.2f}"
            for class_id, conf in zip(detections.class_id, detections.confidence)
        ]
        processed_frame = box_annotator.annotate(scene=frame, detections=detections)
        return processed_frame
