import argparse

import cv2
import numpy as np
import supervision as sv
from ultralytics import YOLO

ZONE_POLYGON = np.array([[0, 0], [0.5, 0], [0.5, 1], [0, 1]])


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument("--webcam-resolution", default=[1280, 720], nargs=2, type=int)
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("yolov8l.pt")

    box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=2, text_scale=1)

    zone_polygon = (ZONE_POLYGON * np.array(args.webcam_resolution)).astype(int)
    zone = sv.PolygonZone(
        polygon=zone_polygon, frame_resolution_wh=tuple(args.webcam_resolution)
    )
    zone_annotator = sv.PolygonZoneAnnotator(
        zone=zone, color=sv.Color.red(), thickness=2, text_thickness=4, text_scale=2
    )

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("Failed to read frame from the camera.")
            continue  # Skip the rest of the loop iteration

        result = model(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_ultralytics(result)

        labels = [
            f"{model.model.names[class_id]} {confidence:0.2f}"
            for confidence, class_id in zip(detections.confidence, detections.class_id)
        ]
        frame = box_annotator.annotate(
            scene=frame, detections=detections, labels=labels
        )

        zone.trigger(detections=detections)
        frame = zone_annotator.annotate(scene=frame)

        cv2.imshow("yolov8", frame)

        if cv2.waitKey(30) == 27:
            break


if __name__ == "__main__":
    main()
