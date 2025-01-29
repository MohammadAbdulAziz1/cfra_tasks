import pandas as pd
import os

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

combined_data = pd.DataFrame()

for file_path in file_paths:
    df = pd.read_excel(file_path)
    df.rename(columns=column_mapping, inplace=True)
    
    df['weighting_sponsor'] = df['weighting_sponsor'] / 100
    
    combined_data = pd.concat([combined_data, df], ignore_index=True)

combined_data.to_csv(output_csv, index=False)

print(f"Combined data has been saved to {output_csv}")