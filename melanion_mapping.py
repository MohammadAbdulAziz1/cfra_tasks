import os
import csv
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import dict_to_csv, setup_webdriver

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

def create_download_folder(script_path):
    root = os.path.dirname(script_path)
    download_folder = os.path.join(root, script_path.replace('.py', ''))
    os.makedirs(download_folder, exist_ok=True)
    return download_folder

def download_file(isin_url, download_folder):
    for isin, url in isin_url.items():
        file_path = os.path.join(download_folder, f"{isin}.csv")
        headers = {'User-Agent': USER_AGENT}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded successfully and saved to {file_path}")
        else:
            raise Exception(f"Failed to download file for ISIN {isin}. HTTP Status Code: {response.status_code}")
    return file_path

def extract_isin_and_currency(driver, url, xpath):
    driver.get(url)
    elements = driver.find_elements(By.XPATH, xpath)
    return [element.text for element in elements[:2]]

def get_matching_firstbridge_ids(csv_file, isin):
    # matching_ids = []
    isin_fbids = {}
    with open(csv_file, 'r') as infile:
        csv_reader = csv.DictReader(infile)
        # for row in csv_reader:
            # if isin == row.get('isin', '').strip():
            #     matching_ids.append(row.get('firstbridge_id', ''))
        for i in csv_reader:
            isin = i['isin']
            firstbridge_id = i['firstbridge_id']
            if isin not in isin_fbids.keys():
                isin_fbids[isin] = []
            # else:
            isin_fbids[isin].append(firstbridge_id)
    return isin_fbids

def process_csv_file(file_path, limit=3):
    with open(file_path, 'r') as infile:
        csv_reader = csv.DictReader(infile)
        for i, row in enumerate(csv_reader):
            if i < limit:
                print(f"Date: {row['Date']}, NAV: {row['NAV']}, AUM: {row['AUM']}")
                return row
    return {}

def prepare_final_data(isin, currency, isin_fbids, csv_row):
    final_data = []
    
    for firstbridge_id in isin_fbids[isin]:
        final_data.append({
            'isin': isin,
            'currency': currency,
            'firstbride_id': firstbridge_id,
            'date': csv_row['Date'],
            'nav': csv_row['NAV'],
            'aum': float(csv_row['AUM']) * 1000000
        })
    return final_data


script_path = __file__
download_folder = create_download_folder(script_path)

driver = setup_webdriver(download_folder)
melanion_url = 'https://melanion.com/bitcoin-equities-etf/'
isin_and_currency_xpath = '//div[2][@class="data-row"]/div/p'

scraped_data = extract_isin_and_currency(driver, melanion_url, isin_and_currency_xpath)
driver.quit()

isin = scraped_data[0].strip()
currency = scraped_data[1].strip()

base_url = 'https://melanion.com/wp-content/uploads/documents/Nav-Aum-Heading.csv'
isin_url = {isin: base_url}
print("isin_url : ",isin_url)

file_path = download_file(isin_url, download_folder)

firstbridge_info_file = 'Melanion Capital_etf.csv'
isin_fbids = get_matching_firstbridge_ids(firstbridge_info_file, isin)

if not isin_fbids:
    print("No matching ISIN found in the CSV file.")

csv_row = process_csv_file(file_path)
if not csv_row:
    raise Exception("Failed to process the downloaded CSV file.")

final_data = prepare_final_data(isin, currency, isin_fbids, csv_row)
fieldnames = ['isin', 'currency', 'firstbride_id', 'date', 'nav', 'aum']
dict_to_csv(data=final_data, fieldnames=fieldnames, filename='melanion_mapping.csv')
print("Final data successfully saved to melanion_mapping.csv")

