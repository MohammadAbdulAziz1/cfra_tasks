import csv

dag_list = [
    "s3://my_bucket_funds/airflow/dags/sources/holdings/asia/value_etf_MY_stable.py", 
    "s3://my_bucket_funds/airflow/dags/sources/holdings/us/parnassus_stable.py",
    "s3://my_bucket_funds/airflow/dags/sources/holdings/asia/cathay_TW_stable.py",
    "s3://my_bucket_funds/airflow/dags/sources/holdings/australia/vaughan_nelson_stable.py"
]


dags = []
for i in dag_list:
    components = i.split('/')
    dags.append({
        'PRODUCT_TYPE': components[-3],
        'REGIONS': components[-2],
        'DAG_NAMES': components[-1]
    })
fieldnames=['PRODUCT_TYPE', 'REGIONS', 'DAG_NAMES']  
filename ='stable_dags_list.csv'
  

# print("Data saved to stable_dags_list.csv")

