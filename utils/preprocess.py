import cv2
import yaml
from typing import List


def load_yaml(filepath: List[str]) -> dict:
    cfg = dict()
    for file in filepath:
        print("Loading {}...".format(file))
        with open(file, encoding="utf-8") as f:
            # cfg |= yaml.load(f.read(), Loader=yaml.FullLoader)
            cfg.update(yaml.load(f.read(), Loader=yaml.FullLoader))
    print("Merging parsing results...")
    return cfg


def cv2_read_image(image_path):
    image_array = cv2.imread(image_path, cv2.IMREAD_COLOR | cv2.IMREAD_IGNORE_ORIENTATION)
    image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)  # (H, W, C(R, G, B)) (0~255) dtype = np.uint8
    return image_array