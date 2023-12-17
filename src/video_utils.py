import tempfile

import cv2


def save_temporary_video(uploaded_file):
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tfile.write(uploaded_file.read())
    tfile.close()
    return tfile.name
