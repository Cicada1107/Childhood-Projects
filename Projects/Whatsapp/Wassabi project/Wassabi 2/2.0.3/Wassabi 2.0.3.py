#Wassabi 2.0.3
#= WSB = Wassabi(code name)
#This also logs the online time in a csv file
#Keep a record of when the person comes online or when he goes offline in the csv file and don't close the window
#make a while loop for the sound generation. Make it beep a number of times. Maybe for as long as the victim stays online...
#And don't make this one send a mail to you.
#ALWAYS USE FRONT SLASH IN PANDAS FILE LOCATIONS!


import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import system
import winsound
import pandas as pd
from datetime import datetime
import pyautogui as pg

#Build a csv file to output
#df = pd.DataFrame()#{"A": ['Hello', 'Test']})
#df.to_csv("E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.0.3/output_data.csv")

driver = webdriver.Chrome("D:/Programming/Python/Python_programs/Resources/ChromeDriver/chromedriver_win32/chromedriver.exe")#"E:/SOFTWARE/Chromedriver/chromedriver_win32/chromedriver.exe")
driver.get("https://web.whatsapp.com")
print("Please scan the QR Code from your phone's WhatsApp app to provide access to your WhatsApp.")
user_name = pg.prompt("Please type in the contact name of the victim: ")
sound = input("Do you want sound?(y/n): ")
search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_bar.click()
search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.send_keys(user_name)
search.send_keys(Keys.RETURN)
now = datetime.now()
#However, whichever phone number shows up first in the list gets selected by default(if the targeted recipent has multiple numbers by the same name)
#user.click()
#user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
print("searching WebHost for " + str(user_name) + "...")
print("Search complete. Victim found: " + str(user_name))
print("Monitor Initiation time:", now.strftime("%H:%M:%S"))
while True:
    search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    status_str = status.text
    if 'online' in status_str:
        print ('Victim online')

        #Beeping sound to alert
        if sound == "y":
            duration = 1000  # milliseconds
            freq = 1000 # Hz
            winsound.Beep(freq, duration)
        elif sound == "n":
            pass
        time.sleep(15)

        #Grab the time when the user comes online and when he/she goes offline
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = datetime.today()
        current_date = today
        print("Online Time:", current_time, sep = ' ')

        #make a dictionary with the username, online time, offline time, duration.
        user_data = {"Victim": user_name, "Date": current_date, "Online time": current_time}#"offline time":
        #csv file
        df = pd.read_csv('E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.0.3/output_data.csv', index_col=0)
        df = df.append(user_data, ignore_index=True)#({"Last online": current_time}, ignore_index=True)
        df.to_csv("E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.0.3/output_data.csv")
        time.sleep(240)
print("Log successful")
