import pyautogui

def clickOnImage(imgPath):
    pyautogui.click(pyautogui.locateCenterOnScreen(imgPath))

def getPositionOfImage(imgPath):
    return pyautogui.locateCenterOnScreen(imgPath)

def click(x,y):
    pyautogui.click(x, y)
    pyautogui.click()
