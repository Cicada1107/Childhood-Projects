#Screen_Mouse tracer
#this program teels the coordinate of the mouse pointer.

import pyautogui as pg
import time

input("Position your mouse at one place of your choice and then press enter to print the coordinate of that point.")

try:
    while True:
        x, y = pg.position()
        coordinates = "X: " + str(x).ljust(4) + "Y: " + str(y).ljust(4)
        print(coordinates, end = " ")
        print('\b' + str(len(coordinates)), end = " ", flush = True)

except KeyboardInterrupt:
    print("\nProgram Closed.")

time.sleep(3)
