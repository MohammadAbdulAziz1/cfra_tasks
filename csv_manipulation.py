import csv
from datetime import datetime
# from utilities import process_csv


input_file = 'etfs_with_t_minus_three_data_16_Dec_2024_19_15_Europe.csv'  
output_files = {
    'in_range': 'in_range.csv',
    'out_of_range': 'out_of_range.csv',
    'private': 'private_data.csv',
}
date_range = (datetime.strptime('2024-11-16', '%Y-%m-%d'), datetime.strptime('2024-12-11', '%Y-%m-%d'))
private_sponsors = {'Index IQ', 'Vanguard', 'UBS'}
date_column = 'as_of_date'
sponsor_column = 'sponsor'

def read_csv(file_path):
    with open(file_path, 'r') as infile:
        return list(csv.DictReader(infile))


def write_csv(file_path, fieldnames, rows):
    with open(file_path, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def filter_by_date(rows, date_column, start_date, end_date):
    in_range = []
    out_range = []
    for row in rows:
        as_of_date = datetime.strptime(row[date_column], '%Y-%m-%d')
        if start_date <= as_of_date <= end_date:
            in_range.append(row)
        else:
            out_range.append(row)
    return in_range, out_range


def filter_by_sponsor(rows, sponsor_column, private_sponsors):
    private_data = []
    remaining_data = []
    for row in rows:
        if row[sponsor_column] in private_sponsors:
            private_data.append(row)
        else:
            remaining_data.append(row)
    return private_data, remaining_data


def process_csv(input_file, output_files, date_range, private_sponsors, date_column, sponsor_column):
    rows = read_csv(input_file)
    if rows:
        fieldnames = list(rows[0].keys())
    else:
        fieldnames = []


    private_data, remaining_rows = filter_by_sponsor(rows, sponsor_column, private_sponsors)

    in_range, out_range = filter_by_date(remaining_rows, date_column, *date_range)

    if in_range:
        write_csv(output_files['in_range'], fieldnames, in_range)
    if out_range:
        write_csv(output_files['out_of_range'], fieldnames, out_range)
    if private_data:
        write_csv(output_files['private'], fieldnames, private_data)


process_csv(input_file, output_files, date_range, private_sponsors, date_column, sponsor_column)
