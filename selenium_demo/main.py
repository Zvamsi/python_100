from selenium import webdriver
from selenium.webdriver.common.by import By



# KEEP ON OPENING CHROME
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

# CREATING A BRIDGE
driver=webdriver.Chrome(options=chrome_options)
# driver.get('https://www.amazon.in/gp/product/B0F8BPGLKF/ref=ox_sc_act_image_2?smid=A1WYWER0W24N8S&psc=1')
driver.get('https://www.python.org/')

# GETTING THE PRICE AND NAME OF A PRODUCT
# price_element=driver.find_element(By.CLASS_NAME,value='a-price-whole').text
# name_element=driver.find_element(By.ID,'productTitle').text
#
# print(f'The {name_element} has dropped to {price_element}\ncheck it out..')

# GETTING INPUT FIELD
# input_field=driver.find_element(By.NAME,'field-keywords')
# print(input_field.get_attribute('placeholder'))

# discount=driver.find_element(By.ID,value='buy-now-button').get_attribute('title')
# print(discount)

# random_text=driver.find_element(By.XPATH,value='//*[@id="aod-ingress-link"]/span[3]/span[2]/span[2]')
# print(random_text.text)

# GETTING EVENTS
div=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[2]/div[2]')
events_time=div.find_elements(By.CSS_SELECTOR, value='li time')
events_name=div.find_elements(By.CSS_SELECTOR,value='li a')

event_time_list=[item.text for item in events_time]
print(event_time_list)
event_title_list=[item.text for item in events_name]
print(event_title_list)
final_dict={}
for i in range(len(event_title_list)):
    final_dict.update({i:{'time':event_time_list[i],'name':event_title_list[i]}})
print(final_dict)

final2_dict={i:{'time':event_time_list[i],'name':event_title_list[i]} for i in range(len(event_title_list))}
print(final2_dict)


# driver.close()
driver.quit()