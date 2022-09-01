from time import sleep
from turtle import delay
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
option = webdriver.ChromeOptions()
option.add_argument("--headless")
browser = webdriver.Chrome(executable_path='/Users/fadyfaheem/Desktop/LunchAutoFill/chromedriver', options=option)

# FILL THESE IN FOR IT TO WORK!
firstandlastname = ""
studentIDUser = ""

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdvpyTexS7F0W7UEboBWuIPf9dJvp1X851CDVtqJkNHFQsjuA/viewform")
result = browser.page_source.__contains__("Ordering is closed! Please, DO NOT SKIP LUNCH! Let someone at the Pointe, or any administrator, know immediately if you need lunch. Ordering will open again at 7:30 am.")
if (not result):
    delay(50)
    firstandlast = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input')
    firstandlast.send_keys(firstandlastname)
    nextButton = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    nextButton.click()
    delay(50)
    studentID = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    studentID.send_keys(studentIDUser)
    nextButton = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span')
    nextButton.click()
    sleep(0.15)
    browser.execute_script("document.evaluate('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
    options = ['/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]', '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[4]']
    sleep(0.15)
    browser.execute_script("document.evaluate('" + random.choice(options) + "', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
    sleep(0.15)
    browser.execute_script("document.evaluate('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
    sleep(0.15)
    browser.execute_script("document.evaluate('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[1]/span', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
    sleep(0.15)
    choclateMilk = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[3]/span'
    browser.execute_script("document.evaluate('" + choclateMilk + "', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
    sleep(0.15)
    browser.execute_script("document.evaluate('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();")
    browser.close()
    print("Lunch ordered!")
else:
    print("Too late to order lunch :(")