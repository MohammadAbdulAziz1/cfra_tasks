from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities import dict_to_csv

driver = webdriver.Chrome()
flipkart_url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.price_range.from%3D10000&p%5B%5D=facets.price_range.to%3D20000'
model_xpath ='//div[@class="KzDlHZ"]'
model_spec_xpath = '//div[@class="_6NESgJ"]'
price_xpath = '//div[@class="Nx9bqj _4b5DiR"]'

driver.get(flipkart_url)
models = driver.find_elements(By.XPATH, model_xpath)
model_specifications = driver.find_elements(By.XPATH, model_spec_xpath)
prices = driver.find_elements(By.XPATH, price_xpath)

products = []

print(f"{len(models)} items found")
print(f"{len(model_specifications)} items found")
print(f"{len(prices)} items found")

for i in range(len(models)):
    model = models[i].text 
    spec = model_specifications[i].text 
    price = prices[i].text
    product = {
        'Model': model,
        'Spec': spec,
        'Price': price
    }
    products.append(product)


# for product in products:
#     print(product)

fieldnames = ["Model","Spec","Price"]
filename = "product_details.csv"
dict_to_csv(data=products, fieldnames=fieldnames, filename=filename)


driver.close()