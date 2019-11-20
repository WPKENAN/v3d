import os

import pyautogui as pag
import time

#1938 1127
try:
    while True:
        x,y=pag.position()
        print(x,y)
        time.sleep(0.5)
        os.system('cls')
except:
    print("end")