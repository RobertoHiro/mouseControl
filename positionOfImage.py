import pyautogui

def getPositionOfImage():
    return pyautogui.locateCenterOnScreen('start.png')#If the file is not a png file it will not work
