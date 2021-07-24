import pyautogui
import time

time.sleep(2)
s = open('test.txt', 'r')

lst = [x.lstrip() for x in s]

for x in lst:
    pyautogui.typewrite(x + "\n")
