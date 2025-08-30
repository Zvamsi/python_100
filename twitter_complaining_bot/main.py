import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_UPLOAD_SPEED=40
PROMISED_DOWNLOAD_SPEED=100

chrome_op=webdriver.ChromeOptions()
chrome_op.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_op)
driver.maximize_window()

driver.get('https://www.speedtest.net/')

time.sleep(3)
policy_continue=driver.find_element(By.XPATH,value='//*[@id="onetrust-accept-btn-handler"]')
policy_continue.click()

go_button=driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
go_button.click()

time.sleep(40)

ad_close=driver.find_element(By.CLASS_NAME,value='close-btn')
driver.execute_script('arguments[0].click();',ad_close)

download_speed=float(driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
print(download_speed)
upload_speed=float(driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
print(upload_speed)
if PROMISED_DOWNLOAD_SPEED>download_speed and PROMISED_UPLOAD_SPEED>upload_speed:
    driver.get('https://x.com/home')

    time.sleep(5)
    number_input=driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    number_input.send_keys('email_id',Keys.ENTER)
    time.sleep(2)
    user_name=driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    user_name.send_keys('username',Keys.ENTER)
    time.sleep(2)
    password_input=driver.find_element(By.XPATH,value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password_input.send_keys('password',Keys.ENTER)
    time.sleep(5)
    input_field=driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    input_field.send_keys(f'My internet speed is low, UPload speed : {upload_speed}MB whereas promised speed is {PROMISED_UPLOAD_SPEED} and Download speed is:{download_speed}MB whereas promised speed is {PROMISED_DOWNLOAD_SPEED}',Keys.ENTER)
    time.sleep(1)
    post_button=driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    post_button.click()
else:
    print('Everything is great..!')