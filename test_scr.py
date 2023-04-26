import time
import os
import numpy as np
import pyscreenshot as ImageGrab
import cv2

import pytesseract
import pyautogui

input('from')
x1, y1 = pyautogui.position()
input('to')
x2, y2 = pyautogui.position()

# make a screen
screen = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))  # 589, 275, 1386, 408

# screen-to-image
cv2.imwrite('Image.png', screen)
img = cv2.imread('Image.png')

# image-to-string
text = pytesseract.image_to_string(img, lang='rus').replace('\n', '')
print(text)

# show screen
cv2.imshow('Screen', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
# cv2.destroyAllWindows()
