#Screen_Mouse_pointer_location
#this program teels the coordinate of the mouse pointer.

import pyautogui as pg
import time

m = input('How many points do you want to find the coordinate of? ')

n = 1
while n <= int(m):
    n += 1
    input("Position your mouse at one place of your choice and then press enter to print the coordinate of that point.")

    try:
        while True:
            x, y = pg.position()
            coordinates = "X: " + str(x).ljust(4) + "Y: " + str(y).ljust(4)
            print(coordinates, end = " ")
            print('\b' + str(len(coordinates)), end = " ", flush = True)
            break

    except KeyboardInterrupt:
        print("\nProgram Closed.")

input('Press enter to exit.')
