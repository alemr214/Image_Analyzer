import numpy as np
import matplotlib.pyplot as plt
from PIL import Image as IMG

try:
    from model.image import Image
except ModuleNotFoundError:
    from src.model.image import Image


def convert_image_array(img: Image) -> np.ndarray:
    return np.asarray(IMG.open(img.route))


def extract_red_channel(img_array: np.ndarray) -> np.ndarray:
    return img_array[:, :, 0]


def extract_green_channel(img_array: np.ndarray) -> np.ndarray:
    return img_array[:, :, 1]


def extract_blue_channel(img_array: np.ndarray) -> np.ndarray:
    return img_array[:, :, 2]


def shrink_image(img_array: np.ndarray, scalar: int) -> np.ndarray:
    return img_array[::scalar, ::scalar]


def rotate_image(img_array: np.ndarray) -> np.ndarray:
    return np.rot90(img_array)


def print_save_image(img_name: str, img_array: np.ndarray) -> None:
    plt.imsave(img_name, img_array)
