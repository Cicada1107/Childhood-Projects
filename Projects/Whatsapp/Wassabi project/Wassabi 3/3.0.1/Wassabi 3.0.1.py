#WhatsApp Spy Bot 3.0.1
#WhatsApp Spy Bot = WSB = Wassabi(code name)
#This is a definitive version. This one does not send a mail. Instead, it sends the victim a message when and if thety are online. And does not close it self.
import time
from selenium import webdriver
from os import system
import winsound
import pyautogui as pg

print("=================================================")
print("            WHATSAPP SPY-BOT BY ARIJIT          ")
print("=================================================")
driver = webdriver.Chrome("E:/SOFTWARE/Chromedriver/chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(15)
driver.get("https://web.whatsapp.com")
print("Please scan the QR Code from your phone's WhatsApp app to provide access to your WhatsApp")
user_name = pg.prompt("Enter name of the Victim: ")
search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_bar.click()
search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.send_keys(user_name)
#user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()
print("searching WebHost for " + str(user_name) + "...")
print("Search complete. Victim found: " + str(user_name))
inputString = pg.prompt("What message do you want to send? ")
while True:
    status = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header')
    status_str = status.text
    if 'online' in status_str:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        print("The message has been sent.")
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        time.sleep(15)
        #driver.quit()
        time.sleep(300)


