import cv2
import os
import os.path as osp
from pathlib import Path
import pickle


def get_object(name):
    objects_dir = osp.join(Path(__file__).parent.absolute(), 'objects')
    print("objects_dir: ", objects_dir)
    if not name.endswith('.pkl'):
        name = name + ".pkl"
    filepath = osp.join(objects_dir, name)
    print("filepath: ", filepath)
    if not osp.exists(filepath):
        return None
    with open(filepath, 'rb') as f:
        obj = pickle.load(f)
    return obj
