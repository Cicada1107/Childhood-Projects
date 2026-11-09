#Wassabi 2.0.2
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


#Build a csv file to output
#df = pd.DataFrame()#{"A": ['Hello', 'Test']})
#df.to_csv("E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.0.2/log.csv")

driver = webdriver.Chrome("E:/SOFTWARE/Chromedriver/chromedriver_win32/chromedriver.exe")
driver.get("https://web.whatsapp.com")
print("Please scan the QR Code from your phone's WhatsApp app to provide access to your WhatsApp.")
user_name = input("Please type in the contact name of the victim: ")
search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_bar.click()
search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search.send_keys(user_name)
search.send_keys(Keys.RETURN)
#However, whichever phone number shows up first in the list gets selected by default(if the targeted recipent has multiple numbers by rthe same name)
#user.click()
#user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
print("searching WebHost for " + str(user_name) + "...")
print("Search complete. Victim found: " + str(user_name))

while True:
    status = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header')
    status_str = status.text
    if 'online' in status_str:
        print ('Victim online')

        #Beeping sound to alert
        duration = 1000  # milliseconds
        freq = 1000 # Hz
        winsound.Beep(freq, duration)
        time.sleep(15)
        driver.close()

        #Grab the time when the user comes online and when he/she goes offline
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = datetime.today()
        current_date = today
        print("Online Time =", current_time)

        #make a disctionary with the username, online time, offline time, duration.
        user_data = {"Victim": user_name, "Date": current_date, "Online time": current_time}#"offline time":
        #csv file
        df = pd.read_csv('E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.0.2/log.csv', index_col=0)
        df = df.append(user_data, ignore_index=True)#({"Last online": current_time}, ignore_index=True)
        df.to_csv("E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.0.2/log.csv")
        break
print("Log successful")
