import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

flipkart_url = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.price_range.from%3D10000&p%5B%5D=facets.price_range.to%3D20000'

driver.get(flipkart_url)

wait = WebDriverWait(driver, 10) 
model_images_xpath = '//div[contains(@class, "_4WELSP")]//img'
model_images = wait.until(EC.presence_of_all_elements_located((By.XPATH, model_images_xpath)))

save_dir = "flipkart_images"
os.makedirs(save_dir, exist_ok=True)

for index, image in enumerate(model_images):
    try:
        img_url = image.get_attribute('src') or image.get_attribute('data-src')
        
        if img_url:
            # Download image using requests
            response = requests.get(img_url, stream=True)
            response.raise_for_status()
            
            # Save the image to the directory
            file_path = os.path.join(save_dir, f"mobile_image_{index + 1}.jpg")
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            
            print(f"Image {index + 1} saved: {file_path}")
        else:
            print(f"Image {index + 1} does not have a valid URL.")
    except Exception as e:
        print(f"Failed to save image {index + 1}: {str(e)}")

# Close the WebDriver
driver.quit()
