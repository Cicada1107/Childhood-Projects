#WhatsApp Spy Bot 3.1.0
#WhatsApp Spy Bot = WSB = Wassabi(code name)
#This is a definitive version. This one does not send a mail. Instead, it sends the victim a message when and if thety are online.
#Added Multimedia support

import time
from selenium import webdriver
from os import system
import winsound
import pyautogui

print("=================================================")
print("            WHATSAPP SPY-BOT BY ARIJIT          ")
print("=================================================")
driver = webdriver.Chrome("E:/SOFTWARE/Chromedriver/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(15)
driver.get("https://web.whatsapp.com")
print("Please scan the QR Code from your phone's WhatsApp app to provide access to your WhatsApp")
user_name = pyautogui.prompt("Enter name of the Victim: ")
search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_bar.click()
search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.send_keys(user_name)
time.sleep(0.5)
#user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()
print("searching WebHost for " + str(user_name) + "...")
print("Search complete. Victim found: " + str(user_name))

document = pyautogui.prompt("Enter the File location:")

#browser window should pop open. Now I am thinking of using pyautogui to enter something in that pop up.
def browse():
    browse_bar = pyautogui.locateOnScreen("E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 3/3.1.0/browse_bar.png")
    #print(browse_bar)

    if browse_bar is None:
        raise Exception("Browse Bar not found!")

    pyautogui.click(browse_bar)
    time.sleep(0.75)
    pyautogui.typewrite(document)
    time.sleep(0.75)
    pyautogui.press('enter')
    send = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
    send.click()
    #browse_bar_x = browse_bar[0]
    #browse_bar_y = browse_bar[1]

    #return browse_bar_x, browse_bar_y


while True:
    status = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header')
    status_str = status.text
    if 'online' in status_str:
        #adding multimedia portal
        attach_option = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]')
        attach_option.click()
        document_option = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div/div/ul/li[3]/button')
        document_option.click()
        time.sleep(2)
        browse()
        break

print("The message has been sent.")
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
time.sleep(250)
driver.quit()
