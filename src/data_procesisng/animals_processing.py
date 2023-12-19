import os
import shutil

path = "/home/patrik/repos/multiple_object_detection/data/raw_data/African Wildlife"
labeltrainpath = (
    "/home/patrik/repos/multiple_object_detection/data/raw_data/moved_images/labels"
)
imgtrainpath = (
    "/home/patrik/repos/multiple_object_detection/data/raw_data/moved_images/images"
)

for dirname in os.listdir(path):
    dirpath = os.path.join(path, dirname)
    for file in os.listdir(dirpath):
        filepath = os.path.join(dirpath, file)
        newname = dirname + "_" + file

        if file.endswith((".txt")):  # if label file
            new_label_path = os.path.join(labeltrainpath, newname)
            shutil.copy(filepath, new_label_path)

        elif file.endswith((".jpg", ".JPG")):  # if image file
            new_image_path = os.path.join(imgtrainpath, newname)
            shutil.copy(filepath, new_image_path)
