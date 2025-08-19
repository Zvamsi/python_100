from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie=driver.find_element(By.ID,value='cookie')

def buy_stuff():
    money = int(driver.find_element(By.ID, value='money').text)
    if money>2000:
        option='buyMine'
    elif money>500:
        option='buyFactory'
    elif money>100:
        option='buyGrandma'
    else:
        option='buyCursor'
    buy_cursor = driver.find_element(By.ID, value=option)
    buy_cursor.click()
    threading.Timer(10,buy_stuff).start()

# buy_stuff()


while True:
    cookie.click()




