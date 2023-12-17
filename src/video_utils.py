import tempfile

import cv2


def save_temporary_video(uploaded_file):
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tfile.write(uploaded_file.read())
    tfile.close()
    return tfile.name


def get_video_fps(video_path):
    video_capture = cv2.VideoCapture(video_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    video_capture.release()
    return 1.0 / fps if fps > 0 else 1.0 / 25  # Default to 25 FPS if fps is zero
