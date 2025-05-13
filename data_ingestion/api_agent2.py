import requests
def fetch_market_data(symbol):
    API_KEY = '3B1F4J4DOWDRYZ7M'  # Real-time API key
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    return response.json()
