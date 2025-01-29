"""https://www.myetf.com.my/en/MyETF-Series/MyETF-DJIM25/Downloads?cat=DailyFundValues_NAV."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = 'https://www.myetf.com.my/en/MyETF-Series/MyETF-DJIM25/Downloads?cat=DailyFundValues_NAV.'

driver.get(url)
time.sleep(3)
print("Accessable")