import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



root = os.path.dirname(__file__)
download_folder = os.path.join(root, __file__.replace('.py', ''))
os.makedirs(download_folder, exist_ok=True)

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_folder,  #
    "download.prompt_for_download": False,          
    "download.directory_upgrade": True,             
    "safebrowsing.enabled": True                    
    }
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)


bajaj_finance_url = 'https://www.bajajamc.com/downloads?portfolio'
monthly_portfolio_xpath = '//div[@class="view-footer"]/button[1]'
select_year_xpath = '//select[@id="edit-term-node-tid-depth--19--level-0"]'
select_month_xpath = '//select[@id="edit-term-node-tid-depth--19--level-1"]'
download_button_xpath = '//div[@id="quicktabs-tabpage-downloads_disclosure_tabs-4"]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/span/a'

driver.get(bajaj_finance_url)

monthly_portfolio_button = driver.find_element(By.XPATH, monthly_portfolio_xpath)
monthly_portfolio_button.click()
time.sleep(3)

year_dropdown = driver.find_element(By.XPATH, select_year_xpath)
all_options = year_dropdown.find_elements(By.CLASS_NAME, "has-children")
for option in all_options:
    if option.text == "2024-25":
        option.click()

month_dropdown = driver.find_element(By.XPATH, select_year_xpath)
all_options = month_dropdown.find_elements(By.XPATH, '//select[@id="edit-term-node-tid-depth--19--level-1"]/option')
for option in all_options:
    if option.text == "November":
        option.click()

download_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, download_button_xpath)))
download_button.click()

time.sleep(10)  

driver.quit()
