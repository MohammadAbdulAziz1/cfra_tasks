import csv
from datetime import datetime
from selenium import webdriver


def dict_to_csv(data,fieldnames,filename):
    with open(filename, mode='wt', newline='') as file:
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()  
        writer.writerows(data)

def setup_webdriver(download_folder):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(options=options)
