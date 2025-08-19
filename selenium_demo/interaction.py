from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)


driver=webdriver.Chrome(options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

# ACTIONS
# article_count=driver.find_element(By.CSS_SELECTOR,value='#articlecount a')
# article_count.click()

# BY LINK
# random_link=driver.find_element(By.LINK_TEXT,value='Michael Phelps')
# random_link.click()

# INPUT ELEMENT
vector_icon=driver.find_element(By.XPATH,value='//*[@id="p-search"]/a/span[1]')
vector_icon.click()

my_input=driver.find_element(By.NAME,value='search')
my_input.send_keys('Python',Keys.ENTER)

# driver.quit()