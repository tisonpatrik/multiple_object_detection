import supervision as sv


class FrameAnnotator:
    def __init__(self):
        self.tracker = sv.ByteTrack()
        self.box_annotator = sv.BoundingBoxAnnotator()
        self.label_annotator = sv.LabelAnnotator()

    def annotate_frame(self, frame, results):
        detections = sv.Detections.from_ultralytics(results)
        detections = self.tracker.update_with_detections(detections)
        labels = [
            f"#{tracker_id} {results.names[class_id]} ({confidence:.2f})"
            for class_id, tracker_id, confidence in zip(
                detections.class_id, detections.tracker_id, detections.confidence
            )
        ]
        boxed = self.box_annotator.annotate(frame.copy(), detections=detections)
        labeled = self.label_annotator.annotate(
            boxed, detections=detections, labels=labels
        )
        return labeled
