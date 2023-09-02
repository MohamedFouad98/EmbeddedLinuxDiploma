import requests



# Making our request

Price_USD = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = Price_USD.json()
bitcoin_price_USD = data['bpi']['USD']['rate_float']     
response = requests.get('http://www.floatrates.com/daily/usd.json')
data = response.json()
rate=data['egp']['rate']
amount_egp=rate*bitcoin_price_USD
print(amount_egp)
