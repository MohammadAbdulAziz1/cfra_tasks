import xlrd
import csv
import os
from utilities import dict_to_csv

file_paths = [
    "holdings-daily-sg-en-d07.xlsx",
    "holdings-daily-sg-en-es3.xlsx",
    "holdings-daily-sg-en-s27.xlsx",
]

script_name = os.path.splitext(os.path.basename(__file__))[0]
output_folder = script_name
os.makedirs(output_folder, exist_ok=True)
output_csv = os.path.join(output_folder, f"{script_name}_combined_data.csv")

column_mapping = {
    'Name': 'constituent_name',
    'Weight (%)': 'weighting_sponsor',
    'Identifier': 'constituent_ticker',
    'ISIN': 'isin',
    'SEDOL': 'sedol',
    'Shares Held': 'quantity_held',
    'Base Market Value': 'market_value_held',
    'Local Currency': 'local_currency',
    'Local Price': 'local_price',
    'Holdings As of': 'as_of_date',
}

all_data = []

for file_path in file_paths:
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)

    headers = sheet.row_values(0)
    
    header_mapping = {header: column_mapping.get(header, header) for header in headers}

    for row_idx in range(1, sheet.nrows):
        row_data = sheet.row_values(row_idx)
        row_dict = {header_mapping[headers[col_idx]]: row_data[col_idx] for col_idx in range(len(row_data))}
        
        if 'weighting_sponsor' in row_dict:
            try:
                row_dict['weighting_sponsor'] = float(row_dict['weighting_sponsor']) / 100
            except ValueError:
                row_dict['weighting_sponsor'] = 0
        
        all_data.append(row_dict)

if all_data:
    fieldnames = list(all_data[0].keys())
    dict_to_csv(data=all_data, fieldnames=fieldnames, filename=output_csv)

    print(f"Combined data has been saved to {output_csv}")
else:
    print("No data found to write to CSV.")
