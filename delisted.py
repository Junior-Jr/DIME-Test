from urllib import response
import pandas as pd
import requests
import sqlalchemy

connection_uri = "mysql+pymysql://root:password@127.0.0.1:3306/sys"
db_engine = sqlalchemy.create_engine(connection_uri)

delisted_api_url = "https://financialmodelingprep.com/api/v3/delisted-companies?page=0&apikey=fdebee21cb107eb7fb3968255870b8ff"

response = requests.get(delisted_api_url)
data = response.json()

delisted = pd.json_normalize(data, sep="_")

print(delisted.head())

delisted.to_sql("delisted", db_engine,
                schema="sys", if_exists="replace")

pd.read_sql("SELECT * FROM delisted", db_engine)
