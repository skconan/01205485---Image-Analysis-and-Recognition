import cv2 as cv
import numpy as np


def main():
    camera_matrix = [
        [1443.422183, 0.000000, 997.861930],
        [0.000000, 1436.886498, 629.658405],
        [0.000000, 0.000000, 1.000000],
    ]

    distortion_coeffs = [0.60814, 0.460061, -0.001013, 0.003851, 0.000000]

    proj_matrix = [
        [1653.029785, 0.000000, 995.744853, 0.000000],
        [0.000000, 1647.675537, 626.574940, 0.000000],
        [0.000000, 0.000000, 1.000000, 0.000000],
    ]

    camera_matrix = np.array(camera_matrix)
    proj_matrix = np.array(proj_matrix)
    distortion_coeffs = np.array(distortion_coeffs)

    pincushion_1 = cv.imread(
        r"pincushion.png",
        1)
    pincushion_1 = cv.resize(pincushion_1, (1926, 1216))

    pincushion_2 = cv.imread(
        r"pincushion_2.png", 1)
    pincushion_2 = cv.resize(pincushion_2, (1926, 1216))

    undistort_1 = cv.undistort(
        pincushion_1, camera_matrix, distortion_coeffs, newCameraMatrix=proj_matrix)
    undistort_2 = cv.undistort(
        pincushion_2, camera_matrix, distortion_coeffs, newCameraMatrix=proj_matrix)

    pincushion_2 = cv.resize(pincushion_2, None, fx=0.5, fy=0.5)
    pincushion_1 = cv.resize(pincushion_1, None, fx=0.5, fy=0.5)

    undistort_1 = cv.resize(undistort_1, None, fx=0.5, fy=0.5)
    undistort_2 = cv.resize(undistort_2, None, fx=0.5, fy=0.5)

    cv.imshow("pinchusion_1", pincushion_1)
    cv.imshow("undistort_1", undistort_1)
    cv.imwrite("undistort_1.png", undistort_1)

    cv.imshow("pinchusion_2", pincushion_2)
    cv.imshow("undistort_2", undistort_2)
    cv.imwrite("undistort_2.png", undistort_2)

    cv.waitKey(-1)


if __name__ == "__main__":
    main()
