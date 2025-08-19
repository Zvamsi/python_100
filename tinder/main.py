from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=chrome_options)

driver.get('https://demoqa.com/')

widgets=driver.find_element(By.XPATH,value='//*[@id="app"]/div/div/div[2]/div/div[4]')
driver.execute_script("arguments[0].scrollIntoView(true);", widgets)
widgets.click()

slider = driver.find_element(By.XPATH, '//*[@id="item-3"]')
driver.execute_script("arguments[0].click();",slider)


# scrooler=driver.find_element(By.XPATH,value='//*[@id="sliderContainer"]/div[1]/span/input')
# scrooler.value=100


