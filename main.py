import pyautogui
import pyscreenshot
import cv2
import pytesseract
import pyttsx3
from PIL import Image
import conf

t = ''
all_text = ''


def show_the_scr():
    cv2.imshow('ScreenChot', img)
    cv2.waitKey(0)


# Get the screenshot coordinates
input('from')
x1, y1 = pyautogui.position()
input('to')
x2, y2 = pyautogui.position()

while t != 'q':
    image = pyscreenshot.grab(bbox=(x1, y1, x2, y2))

    # Save the screenshot
    image.save("scr.png")

    # Open the screenshot
    image = Image.open('scr.png')

    # Путь для подключения tesseract
    # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    # Connecting a screenshot
    img = cv2.imread('scr.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Screen-to-text
    config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, conf.lang)  # , config=config  .replace('\n', ' ')

    for line in text.splitlines():
        if line not in all_text:
            all_text += f'\n{line}'

    # sound
    conf.sound()

    # Continue to take screenshots and make Screens-to-texts or quit?
    t = input('print q to exit or any button to continued: ')

print(all_text)

# Text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 120)  # speed
engine.setProperty("volume", 1)  # volume (0-1)
engine.say(all_text)
engine.runAndWait()
