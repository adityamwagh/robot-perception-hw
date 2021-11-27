import importlib
import os
import sys

import cv2
import numpy as np
import pyAprilTag


def compute_camera_matrix(K: np.array, R: np.array, t: np.array) -> np.array:
    return K @ np.r_[np.c_[R, t]]  # 3x4 array


def draw_cube(K, image):
    ids, corners, centers, Hs = pyAprilTag.find(image)
    num, R, t, N = cv2.decomposeHomographyMat(Hs, K)
    print(num, R, t, N)


def get_calib_from_log():
    CUR_DIR = os.getcwd()
    LOG_DIR = os.path.join(CUR_DIR, "calib_log")
    sys.path.insert(0, CUR_DIR)  # otherwise importlib cannot find the path

    logs = sorted([f for f in os.listdir(LOG_DIR) if f.endswith(".py")])
    if len(logs) == 0:
        print("no calibration log available!")
        exit(-1)

    last_log = os.path.relpath(os.path.join(LOG_DIR, logs[-1])).replace(
        os.path.sep, "."
    )[:-3]
    return importlib.import_module(last_log)


def main():

    # get calibration matrix
    K = get_calib_from_log().K
    distCoeffs = get_calib_from_log().distCoeffs
    
    capture = cv2.VideoCapture(0)
    # read the images
    image1 = cv2.imread("HW1/task4/image1.jpg")
    image2 = cv2.imread("HW1/task4/image2.jpg")

    # draw the cube
    # draw_cube(K, image1)
    # draw_cube(K, image2)

    ids, corners, centers, Hs = pyAprilTag.find(image1)
    ids, corners, centers, Hs = pyAprilTag.find(image2)

    print(ids, corners, centers, Hs)
    print(type(image1))

    # cv2.imshow("image2", image2)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
