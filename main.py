import pyautogui
import pyscreenshot
import cv2
import pytesseract
import pyttsx3
from PIL import Image
import os

t = ''
all_text = ''

while t != 'q':
    # Get the screenshot coordinates
    input('from')
    x1, y1 = pyautogui.position()
    input('to')
    x2, y2 = pyautogui.position()

    image = pyscreenshot.grab(bbox=(x1, y1, x2, y2))

    # To save the screenshot
    image.save("scr.png")

    # Open the image
    image = Image.open('scr.png')

    # Connecting a picture
    img = cv2.imread('scr.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Show text from a picture
    config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, lang='rus').replace('\n', ' ')  # , config=config
    all_text += text
    print(all_text)

    # sound
    os.system('afplay shum-zapuschennogo-v-tsel-noja.wav')  # for mac
    # os.system('aplay path/to/sound.wav')  # for linux
    # winsound.PlaySound('path/to/sound.wav', winsound.SND_FILENAME)  # for win

    t = input('print q to exit or any button to continued: ')

# TTS
engine = pyttsx3.init()
engine.say(all_text)
engine.runAndWait()

# Show the Scr
# cv2.imshow('Result', img)
# cv2.waitKey(0)
