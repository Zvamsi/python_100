from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)

driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name=driver.find_element(By.NAME,value='fName')
print(first_name.get_attribute('placeholder'))

last_name=driver.find_element(By.NAME,value='lName')
print(last_name.get_attribute('placeholder'))

email=driver.find_element(By.NAME,value='email')
print(email.get_attribute('placeholder'))

button=driver.find_element(By.CSS_SELECTOR,value='form button')
print(button.size)


# WRITING ON THE FIELDS

first_name.send_keys('vamshi',Keys.ENTER)
last_name.send_keys('A',Keys.ENTER)
email.send_keys('python@gmail.com')
button.click()

# driver.quit()