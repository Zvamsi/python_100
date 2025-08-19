import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_op=webdriver.ChromeOptions()
chrome_op.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_op)

# GET WEBSITE
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

driver.implicitly_wait(2)
username_input=driver.find_element(By.NAME,value='username')
user_password_input=driver.find_element(By.NAME,value='password')

print(username_input.get_attribute('placeholder'))
print(user_password_input.get_attribute('placeholder'))


username_input.send_keys('Admin',Keys.ENTER)
user_password_input.send_keys('admin123',Keys.ENTER)

driver.maximize_window()
time.sleep(2)

buzz_link=driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a')
buzz_link.click()


time.sleep(2)
news_feed=driver.find_element(By.CSS_SELECTOR,value='.oxd-form textarea')
time.sleep(2)
news_feed.send_keys('The company is buring down..!')
time.sleep(2)
news_feed_submit_button=driver.find_element(By.CSS_SELECTOR,value='.oxd-form .oxd-button')
news_feed_submit_button.click()

# TO UPLOAD A FILE
time.sleep(2)
button_to_open_file_upload=driver.find_element(By.CSS_SELECTOR,value='.orangehrm-buzz-create-post-actions .oxd-glass-button-icon')
button_to_open_file_upload.click()
time.sleep(2)
file_upload=driver.find_element(By.CSS_SELECTOR,value='.oxd-file-input')
file_upload.send_keys('C:/Users/Admin/Downloads/peace.jpg')
time.sleep(2)


share_button=driver.find_element(By.CSS_SELECTOR,value='.oxd-form-actions .oxd-button')
# print(share_button.size)
share_button.click()

time.sleep(5)

pim_link=driver.find_element(By.XPATH,value='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
pim_link.click()

# TO FETCH HOW MANY NUMBER OF RECORDS ARE THERE
num_of_records=driver.find_element(By.CSS_SELECTOR,value='.orangehrm-horizontal-padding span')
st=num_of_records.text
st1=st.split('(')[1]
num_of_emp=int(st1.split(')')[0])

# TO LOCATE EACH RECORD OF EMPLOYEE AND DELETE
for each_record in range(num_of_emp):
    emp_cards = driver.find_element(By.CSS_SELECTOR, value='.oxd-table-card')
    time.sleep(2)
    corner_div = emp_cards.find_element(By.CSS_SELECTOR, value='.oxd-table-cell-actions')
    buttons = corner_div.find_elements(By.CLASS_NAME, value='oxd-icon-button')
    # print(buttons[1].size)
    buttons[1].click()
    time.sleep(2)
    yes_delete = driver.find_element(By.CLASS_NAME, value='oxd-button--label-danger')
    # print(yes_delete.size)
    yes_delete.click()
    # delete_button.click()
    time.sleep(5)

driver.quit()
