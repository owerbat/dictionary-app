import os
import numpy as np


def make_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_root_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')


def get_dump_path():
    return make_dir(os.path.join(get_root_path(), 'dump'))


def softmax(x: np.ndarray):
    return np.exp(x) / np.sum(np.exp(x))
