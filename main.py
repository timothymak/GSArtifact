import os
import time
import psutil    
from PIL import Image
import pygetwindow
import pyautogui

PROCESS_NAME = "GenshinImpact.exe"
WINDOW_NAME = "原神"
SCREENSHOT_DIR = "./temp"
SCREENSHOT_FILENAME = "screenshot.jpg"
SCREENSHOT_PATH = os.path.join(SCREENSHOT_DIR, SCREENSHOT_FILENAME)

def game_running():
    return PROCESS_NAME in (p.name() for p in psutil.process_iter())
    
def activate_window():
    titles = pygetwindow.getAllTitles()
    window = pygetwindow.getWindowsWithTitle(WINDOW_NAME)[0]
    window.activate()
    time.sleep(1)
    return window

def take_screenshot(window):
    if not os.path.exists(SCREENSHOT_DIR):
        print("Creating temp folder...")
        os.mkdir(SCREENSHOT_DIR)
    
    x1 = window.left
    y1 = window.top
    width = window.width
    height = window.height
    x2 = x1 + width
    y2 = y1 + height

    pyautogui.screenshot(SCREENSHOT_PATH)
    im = Image.open(SCREENSHOT_PATH)
    im = im.crop((x1, y1, x2, y2))
    im.save(SCREENSHOT_PATH)
    im.show(SCREENSHOT_PATH)

def main():
    if game_running():
        window = activate_window()
        take_screenshot(window)
        pass
    else:
        print(PROCESS_NAME + " is not running!")

if __name__ == "__main__":
    main()