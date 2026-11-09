#WhatsApp Spy Bot 1.0.0
#= WSB = Wassabi(code name)
import time
from selenium import webdriver
import smtplib
from os import system
import winsound

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
        freq = 440  # Hz
        winsound.Beep(freq, duration)
        time.sleep(15)
        driver.close()
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
