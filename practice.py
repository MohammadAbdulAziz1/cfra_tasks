from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://the-internet.herokuapp.com/dropdown'
driver.get(url)
dropdown_xpath = '//select[@id="dropdown"]/option'
options = driver.find_elements(By.XPATH, dropdown_xpath)
for option in options:
    print("Value is: %s" % option.get_attribute("value"))
    time.sleep(3)
    option.click()

print("done")

# time.sleep(30)

# driver.close()

# file_download_xpath = '//div[@id="content"]/div/a'
# options = driver.find_elements(By.XPATH, file_download_xpath)
# for option in options:
#     print("Value is: %s" % option.get_attribute("value"))
#     time.sleep(3)
#     option.click()

# print("done")

time.sleep(30)

driver.close()