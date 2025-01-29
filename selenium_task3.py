from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://www.nuvamawealth.com/oyo/equity/top-long-term-stock-recommendations'

driver.get(url)
# midcap_button_xpath = '//*[@id="oyoSection"]/section[1]/div/div/div[3]/div/div/button'
stock_name_xpath = '//label[@class="ed-lbl reg ng-binding"]'

# midcap_button = driver.find_element(By.XPATH, midcap_button_xpath)
# midcap_button.click()
# time.sleep(3)

stock_names = driver.find_elements(By.XPATH, stock_name_xpath)
print(len(stock_names))
for stock_name in stock_names:
    print(stock_name.text)

driver.close()

'''//*[@id="scheme0"]/div[1]/div[1]/div[1]/label[1]'''
"""ed-lbl schemename ng-binding ng-hide

//label[@class="ed-lbl schemename ng-binding ng-hide"]
"""