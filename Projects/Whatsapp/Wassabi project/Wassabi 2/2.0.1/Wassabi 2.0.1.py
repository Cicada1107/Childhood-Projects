#Wassabi 2.0.1
#= WSB = Wassabi(code name)
#This also logs the online time in a csv file
import time
from selenium import webdriver
import smtplib
from os import system
import winsound
import asyncio
import pandas as pd
from datetime import datetime


#Build a csv file to output
df = pd.DataFrame({"A": ['Hello', 'Test']})
df.to_csv('E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.0.1/output.csv')

driver = webdriver.Chrome("E:/SOFTWARE/Chromedriver/chromedriver_win32/chromedriver.exe")
driver.get("https://web.whatsapp.com")
print("Please scan the QR Code from your phone's WhatsApp app to provide access to your WhatsApp.\nYou have 40 seconds to scan and open the victim's chatbox.")
time.sleep(40)
while True:
    status = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header')
    status_str = status.text
    if 'online' in status_str:
        print ('Victim online')
        duration = 1000  # milliseconds
        freq = 1000  # Hz
        winsound.Beep(freq, duration)
        time.sleep(15)
        driver.close()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Online Time =", current_time)

        df = pd.read_csv('E:/ARIJIT/Misceleanous/PYTHON/Python scripts/Projects/Wassabi project/Wassabi 2/2.0.1/output.csv', index_col=0)
        df = df.append({"Online time": current_time}, ignore_index=True)
        #df = df.append({"Points": points}, ignore_index=True)
        df.to_csv("E:\ARIJIT\Misceleanous\PYTHON\Python scripts\Projects\Wassabi project\Wassabi 2\2.0.1\output.csv")

        email = 'arijitdubey2018@gmail.com'
        password = 'Aney@93046'
        send_to_mail = 'arijitdubey2018@gmail.com'
        message = 'Victim spotted online on WhatsApp.'
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email,send_to_mail,message)
        server.quit()
        time.sleep(300)
        break
