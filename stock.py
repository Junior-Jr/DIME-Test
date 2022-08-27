from urllib import response
import pandas as pd
import requests
import sqlalchemy

connection_uri = "mysql+pymysql://root:password@127.0.0.1:3306/sys"
db_engine = sqlalchemy.create_engine(connection_uri)

historical_api_url = "https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/AAPL?apikey=fdebee21cb107eb7fb3968255870b8ff"

response = requests.get(historical_api_url)
data = response.json()
# print(data)

stock_symbol = pd.json_normalize(data, sep="_")

stock_historical = pd.json_normalize(data["historical"], sep="_")

print(stock_historical.head())


stock_historical.to_sql("historical", db_engine,
                        schema="sys", if_exists="replace")

pd.read_sql("SELECT * FROM historical", db_engine)
