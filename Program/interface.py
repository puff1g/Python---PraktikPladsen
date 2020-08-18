from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
from win10toast import ToastNotifier

#! Remember to type in your credentials below
#! Also edit the path in the NoSuchElementExceptions to your liking for logging

# Credentials
yourUsername = ""
yourPassword = ""
toast = ToastNotifier()

options = webdriver.ChromeOptions()
# Option to make the window invisible - Uncomment the line below for use
# options.add_argument("--headless")

driver = webdriver.Chrome(
    "driver/chromedriver.exe", options=options)
driver.get("https://www.praktikpladsen.dk/login")

# Finding login button
try:
    loginBtn = driver.find_element_by_xpath(
        "/html/body/div/div/div/div[4]/main/div/div/div/div[1]/div/button[1]")
    loginBtn.click()
except NoSuchElementException:
    f = open("C:/Users/maje/Desktop/log.txt", "a")
    today = datetime.now()
    f.write("\nLogin knap ikke fundet. " +
            today.strftime("%d/%m/%Y %H:%M:%S") + " SKAL FIKSES!!!")
    f.close()
    driver.quit()

# Logging in - Username
try:
    username = driver.find_element_by_class_name("form-input")
    username.send_keys(yourUsername)
    username.send_keys(Keys.ENTER)
except NoSuchElementException:
    f = open("C:/Users/maje/Desktop/log.txt", "a")
    today = datetime.now()
    f.write("\nFejl - Har du husket at indtaste dit username? " +
            today.strftime("%d/%m/%Y %H:%M:%S"))
    f.close()
    driver.quit()

# Logging in - Password
try:
    pwd = driver.find_element_by_id("form-error")
    pwd.send_keys(yourPassword)
    pwd.send_keys(Keys.ENTER)
except NoSuchElementException:
    f = open("C:/Users/maje/Desktop/log.txt", "a")
    today = datetime.now()
    f.write("\nFejl - Har du husket at indtaste dit password? " +
            today.strftime("%d/%m/%Y %H:%M:%S"))
    f.close()
    driver.quit()

# Skipping password change and animation
try:
    wait = driver.find_element_by_name("wait").click()
    time.sleep(2)
except NoSuchElementException:
    time.sleep(2)
    pass

# Finding edit button
try:
    try:
        editBtn = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[4]/main/div/div/div/div[1]/div[2]/button")
        editBtn.click()
    except NoSuchElementException:
        f = open("C:/Users/maje/Desktop/log.txt", "a")
        today = datetime.now()
        f.write("\nKan ikke finde 'Rediger profil' knappen. " +
                today.strftime("%d/%m/%Y %H:%M:%S") + " SKAL FIKSES!!!")
        f.close()
        driver.quit()

    # Finding the prolong button
    extendButtons = driver.find_elements_by_xpath(
        "/html/body/div/div/div/div[4]/main/div/div/div/div[2]/div/div/button[2]")
    for x in extendButtons:
        if 'Forlæng synlighed' in x.text:
            x.click()

    # * Succesfully prolonged visibility
    # f = open("C:/Users/maje/Desktop/log.txt", "a")
    today = datetime.now()
    # f.write("\nSynlighed forlænget d. " + today.strftime("%d/%m/%Y %H:%M:%S"))
    # f.close()
    print(today.strftime("%d/%m/%Y %H:%M:%S"))
    time.sleep(2)
    element = driver.find_element_by_xpath("/html/body/div/div/div/div[4]/main/div/div/div/div[2]/div/p").text
    print(element)
    toast.show_toast("Praktikpladsen",element,duration=8,)
    # * Couldn't prolong because it was recently done
except NoSuchElementException:
    pass
    today = datetime.now()
    print("\nIngen mulighed for forlængelse d. " +
            today.strftime("%d/%m/%Y %H:%M:%S"))


# Closing the window
driver.quit()
