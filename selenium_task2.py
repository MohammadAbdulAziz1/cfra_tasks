# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from utilities import dict_to_csv

# driver = webdriver.Chrome()
# url = 'https://www.moneycontrol.com/markets/global-indices/'
# stock_name_xpath = '//span[@class="marketData_web_mE_nm__jSXqk"]'
# open_xpath= '//table[contains(@class, "marketData_web_table")]/tbody/tr/td[7]'
# high_xpath = '//table[contains(@class, "marketData_web_table")]/tbody/tr/td[5]'
# low_xpath= '//table[contains(@class, "marketData_web_table")]/tbody/tr/td[6]'
# prev_close_xpath= '//table[contains(@class, "marketData_web_table")]/tbody/tr/td[8]'

# driver.get(url)
# print("this is done")
# stock_names = driver.find_elements(By.XPATH, stock_name_xpath)
# highs = driver.find_elements(By.XPATH, high_xpath)
# lows = driver.find_elements(By.XPATH, low_xpath)
# opens = driver.find_elements(By.XPATH, open_xpath)
# prev_closes = driver.find_elements(By.XPATH, prev_close_xpath)

# stock_details = []

# for i in range(len(highs)):
#     stock_name = stock_names[i].text
#     high = highs[i].text
#     low = lows[i].text
#     open = opens[i].text
#     prev_close = prev_closes[i].text
#     details = {
#         'Stock_name' : stock_name,
#         'High' : high,
#         'Low' : low,
#         'Open' : open,
#         'Prev_close' : prev_close
#     }
#     stock_details.append(details)

# fieldnames = ["Stock_name","High","Low","Open","Prev_close"]
# filename = "stock_details.csv"
# dict_to_csv(data=stock_details, fieldnames=fieldnames, filename=filename)

# driver.close()

