import requests
from utilities import dict_to_csv

url = "https://www.ncfunds.com/etf/load.php?f=428"
response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    
    holdings = data.get("holdings", [])
    print(len(holdings))
    holdings_list = []
    for holding in holdings:
        holdings_list.append(holding)

else:
    print(f"could not access the {url}")   

fieldnames = ["ticker","cusip","sedol","descr1","price","quantity","marketvalue","percentmv","netassets"]
filename = "ncfunds.csv"
dict_to_csv(data=holdings_list, fieldnames=fieldnames, filename=filename)

        
        


