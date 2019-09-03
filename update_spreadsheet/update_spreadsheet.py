import pandas
new_data = pandas.read_json('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo')
try:
    old_data = pandas.read_excel('market.xls')
except FileNotFoundError:
    old_data = pandas.DataFrame()
