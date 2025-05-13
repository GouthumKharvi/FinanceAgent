import requests
def fetch_market_data(symbol):
    API_KEY = 'FB0N65M3645SUUA1'  
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    return response.json()
