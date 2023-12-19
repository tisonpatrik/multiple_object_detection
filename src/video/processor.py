import supervision as sv
from ultralytics import YOLO

CLASS_ID = [2, 3, 5, 7]


class MediaProcessor:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")
        self.tracker = sv.ByteTrack()
        self.box_annotator = sv.BoundingBoxAnnotator()
        self.label_annotator = sv.LabelAnnotator()

    def process_video_frame(self, frame):
        results = self.model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)
        detections = self.tracker.update_with_detections(detections)
        labels = [
            f"#{tracker_id} {results.names[class_id]}"
            for class_id, tracker_id in zip(detections.class_id, detections.tracker_id)
        ]
        annotated_frame = self.box_annotator.annotate(
            frame.copy(), detections=detections
        )
        return self.label_annotator.annotate(
            annotated_frame, detections=detections, labels=labels
        )
