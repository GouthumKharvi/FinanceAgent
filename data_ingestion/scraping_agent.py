from bs4 import BeautifulSoup
import requests

def scrape_filings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    filings = soup.find_all('div', class_='filing')
    return [filing.text for filing in filings]
