#Wassabi 2.1.0
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
from tkinter import *

#Build a csv file to output
#df = pd.DataFrame()#{"A": ['Hello', 'Test']})
#df.to_csv("E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.1.0/data.csv")

driver = webdriver.Chrome("E:/SOFTWARE/Chromedriver/chromedriver_win32/chromedriver.exe")
driver.get("https://web.whatsapp.com")


root = Tk()
root.title("Wassabi 2.1.0 by Arijit Dubey")
root.geometry('600x100')
root.minsize(200, 100)
root.maxsize(600, 100)

Label(root, text="Please enter the Contact name of the Victim:", pady=11, padx=10).grid(row=2, column=0)

user_name = StringVar()
user_name_entry = Entry(root, textvariable=user_name, font="calibri 20 bold", width=23, relief=SUNKEN)
user_name_entry.grid(row=2, column=2)

sound_val = IntVar()
sound = Checkbutton(text="Enable Alert Sound", variable=sound_val, true_value=1, false_value=0)
sound.grid(row=3, column=2)


def deploy():
    user_name = user_name_entry.get()
    search_bar = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_bar.click()
    search = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search.send_keys(user_name)
    search.send_keys(Keys.RETURN)
    #fine till here
    while True:
        status = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header')
        status_str = status.text
        if 'online' in status_str:
            print ('Victim online')

            #Grab the time when the user comes online and when he/she goes offline
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            today = datetime.today()
            current_date = today
            print("Online Time =", current_time)

            #make a disctionary with the username, online time, offline time, duration.
            user_data = {"Victim": user_name, "Date": current_date, "Online time": current_time}#"offline time":
            #csv file
            df = pd.read_csv('E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.1.0/data.csv', index_col=0)
            df = df.append(user_data, ignore_index=True)#({"Last online": current_time}, ignore_index=True)
            df.to_csv("E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.1.0/data.csv")
            break

            #Beeping sound to alert
            if sound_val == 1:
                duration = 1000  # milliseconds
                freq = 1000 # Hz
                winsound.Beep(freq, duration)
                time.sleep(15)
                driver.close()
            else:
                pass


deployer = Button(root, text="Deploy spy", command=deploy)
deployer.grid(row=4, column=0)

root.mainloop()

#GUI is done. Now for the feature, add them.


