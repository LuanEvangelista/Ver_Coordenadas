import cv2
import numpy as np
from PIL import ImageGrab

global img


def get_color_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'coordinates {x}, {y} with color {img[y, x, :]}')


while True:

    img = ImageGrab.grab()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    factor = 0.5
    img = cv2.resize(img, None, fx=factor, fy=factor, interpolation=cv2.INTER_AREA)

    cv2.imshow('screen', img)
    cv2.setMouseCallback('screen', get_color_mouse)

    key = cv2.waitKey(1)
    if key == 27:  # ESC
        cv2.destroyAllWindows()
        break