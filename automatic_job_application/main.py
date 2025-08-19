from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv,find_dotenv


find_dotenv()
data=load_dotenv()
password=os.getenv('PASSWORD')
email=os.getenv('EMAIL')


Chrome_options=webdriver.ChromeOptions()
Chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=Chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4284105797&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom')

driver.maximize_window()




# SEARCH FOR A JOB
# job_search_input=driver.find_element(By.XPATH,value='//*[@id="jobs-search-box-keyword-id-ember30"]')
#
# job_search_input.send_keys('Python developer intern',Keys.ENTER)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver.implicitly_wait(2)
# job_link=driver.find_element(By.CLASS_NAME,value='job-card-job-posting-card-wrapper__footer-item-icon')
# job_link.click()





sign_in_button=driver.find_element(By.XPATH,value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_button.click()

email_input=driver.find_element(By.XPATH,value='//*[@id="base-sign-in-modal_session_key"]')
password_input=driver.find_element(By.XPATH,value='//*[@id="base-sign-in-modal_session_password"]')
sign_in_button=driver.find_element(By.XPATH,value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')

# FILLING LOGIN CREDENTIALS TO LOGIN
email_input.send_keys(email)
password_input.send_keys(password)
sign_in_button.click()

# EASY APPLY
easy_apply=driver.find_element(By.XPATH,value='//*[@id="jobs-apply-button-id"]/span')
driver.implicitly_wait(2)
easy_apply.click()

# NEXT BUTTON
driver.implicitly_wait(2)
next_button=driver.find_element(By.CSS_SELECTOR,value='.ph5 .artdeco-button')
driver.execute_script("arguments[0].click();", next_button)

next_button.click()

next_button2=driver.find_element(By.CSS_SELECTOR,value='footer .ph5 .artdeco-button')
next_button2.click()