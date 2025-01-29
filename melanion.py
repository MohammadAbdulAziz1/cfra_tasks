"""Task 3:
https://www.melanion.com/etf/melanion-etf
Go to the above link and close all the pop-up and take isin and currency value.

Go to Top 10 Constituents and get date from As of

Fetch all the rows from Top 10 Constituents and write it to a csv with the respective headers.

Add three new columns such as date, currency and isin and populate the same values scraped in step 1 and step 2 to all rows.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utilities import dict_to_csv

driver = webdriver.Chrome()

url = "https://www.melanion.com/etf/melanion-etf"
driver.get(url)
time.sleep(5)


table_header_xpath = '//table[@id="companiesTable"]/thead/tr/th'
table_body_xpath = '//*[@id="companiesTable"]/tbody/tr'


table_headers = driver.find_elements(By.XPATH, table_header_xpath)
table_header_list = [header.text.strip() for header in table_headers]


additional_headers = ["Date", "Currency", "ISIN"]
table_header_list.extend(additional_headers)


table_data = driver.find_elements(By.XPATH, table_body_xpath)


table_data_list = []
for row in table_data:
    cells = row.find_elements(By.XPATH, './td')
    row_data = {}
    
    for i in range(len(cells)):
        row_data[table_header_list[i]] = cells[i].text.strip()
    
    row_data["Date"] = "2025-01-06"  
    row_data["Currency"] = "INR" 
    row_data["ISIN"] = "0123456789"  
    table_data_list.append(row_data)

# Write data to CSV
dict_to_csv(data=table_data_list, fieldnames=table_header_list, filename='melanion.csv')

print("Data successfully saved to 'melanion.csv'")
driver.quit()
