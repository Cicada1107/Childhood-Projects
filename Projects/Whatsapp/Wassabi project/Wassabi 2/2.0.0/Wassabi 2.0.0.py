#WhatsApp Spy Bot 2.0.0
#= WSB = Wassabi(code name)
#Make the Mail id user formattable!
import time
from selenium import webdriver
from os import system
import winsound

driver = webdriver.Chrome("D:/Programming/Python/Python_programs/Resources/ChromeDriver/chromedriver_win32/chromedriver.exe")
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
        winsound.Beep(freq, duration)       #This line makes a sound of a frequency whenevr the victim is online bro SO no need to check the mail lmao
        time.sleep(15)                      #Infact I can even convert the lines below into a doc string so just nise and no mail
        driver.close()
        time.sleep(300)
