import numpy as np
import cv2 as cv
from PIL import Image

mean = (0.485, 0.456, 0.406)
std = (0.229, 0.224, 0.225)


def process(img, short_size):
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow("RGB", img)
    h, w = img.shape[:2]
    if h < w:
        scale_h = short_size / h
        tar_w = w * scale_h
        tar_w = tar_w - tar_w % 32
        tar_w = max(32, tar_w)
        scale_w = tar_w / w
    else:
        scale_w = short_size / w
        tar_h = h * scale_w
        tar_h = tar_h - tar_h - tar_h % 32
        tar_h = max(32, tar_h)
        scale_h = tar_h / h

    img = cv.resize(img, None, fx=scale_w, fy=scale_h)
    img = img.astype(np.float32)

    img /= 255.0
    img -= mean
    img /= std
    cv.imshow("img", img)
    img = img.transpose(2, 0, 1)
    # cv.imshow("trans", img)
    transformed_image = np.expand_dims(img, axis=0)
    # cv.imshow("transformed_image", transformed_image)

    cv.waitKey(0)


if __name__ == "__main__":
    img = cv.imread("./TEST.jpg")
    cv.imshow("origin", img)
    process(img, 960)
