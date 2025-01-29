import csv
import os
from utilities import dict_to_csv

with open('StatewiseTestingDetails.csv', mode='r') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

states = set(row['State'] for row in rows)

script_name = os.path.splitext(os.path.basename(__file__))[0]
output_folder = script_name
os.makedirs(output_folder, exist_ok=True)

for state in states:
    state_rows = [row for row in rows if row['State'] == state]

    state_file_name = state.replace(" ", "_") + ".csv"
    output_path = os.path.join(output_folder, state_file_name)

    if state_rows:  
        fieldnames = state_rows[0].keys() 
        
        dict_to_csv(data = state_rows, fieldnames=fieldnames, filename=output_path)

print(f"All files have been saved in the folder: {output_folder}")
