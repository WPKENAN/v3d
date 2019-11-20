import pyautogui
from pymouse import PyMouse

import time

class MouseClick:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def startclick(self):
        pyautogui.click(self.x, self.y, clicks=2, interval=0.0, button='left')

    def autoclick(self):
        m = PyMouse()
        m.click(self.x, self.y,button=1,n=2)

    def printXY(self):
        print('123123123')

#2373 1128
if __name__ == '__main__':


    while(True):

        x, y = pyautogui.position()
        print(x, y)

        for i in range(5):
            ob = MouseClick(1938, 1127)
            ob.startclick()

            ob = MouseClick(2124, 1131)
            ob.startclick()

            ob = MouseClick(2373, 1128)
            ob.startclick()

            # ob = MouseClick(2021, 1133)
            # ob.startclick()
            # time.sleep(0.3)

        # for i in range(5):
        #     ob = MouseClick(2113, 1133)
        #     ob.startclick()
        #     time.sleep(0.3)

        time.sleep(5)



