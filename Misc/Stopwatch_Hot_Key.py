#Clicks the play and reset button on the given pixel using hotkeys
import keyboard
import pyautogui as pg

try:
    keyboard.add_hotkey('ctrl + shift + v', lambda: pg.click(x=1778, y=987))  #Play/Pause
    keyboard.add_hotkey('ctrl+ shift + b', lambda: pg.click(x = 1832, y = 979))  #Reset
except KeyboardInterrupt:
    print('\n HotKeys OFF')
