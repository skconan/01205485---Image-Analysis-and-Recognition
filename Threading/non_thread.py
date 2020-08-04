import cv2 as cv
import numpy as np
import threading


img = None


def create_object(color, x,  name, step=10, r=5):
    global img
    y = 10
    for i in range(20):
        cv.circle(img, (int(x), y + step*i), r, color, -1)
        cv.waitKey(1000)
        cv.imshow(name, img)


def main():
    global img

    img = np.zeros((500, 500, 3), np.uint8)

    color = (0, 255, 0)
    x = 200
    step = 20
    r = 10
    name= "1"
    create_object(color, x, name, step, r)

    name= "2"
    color = (0, 0, 255)
    x = 250
    create_object(color, x, name, step, r)


if __name__ == "__main__":
    main()
