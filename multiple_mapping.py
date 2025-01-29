import csv
file_path = '/home/tgadmin/Desktop/aziz/cfra_tasks/etfs_with_t_minus_three_data_16_Dec_2024_19_15_Europe.csv'

composite_tickers_dict = {}
with open(file_path, 'rt') as file:
    rd = csv.DictReader(file)
    for i in rd:
        composite_ticker = i['composite_ticker']
        firstbridge_id = i['firstbridge_id']
        if composite_ticker not in composite_tickers_dict.keys():
            composite_tickers_dict[composite_ticker] = []
        # else:
        composite_tickers_dict[composite_ticker].append(firstbridge_id)
print(composite_tickers_dict)