import requests
from bs4 import BeautifulSoup
import time

#function to track price from google

def get_latest_crypto_price(coin):
    url = 'https://www.google.com/search?q=' + (coin) + 'price'
    # make a request to the website
    HTML = requests.get(url)
    # Parsse the HTML
    sp = BeautifulSoup(HTML.text, 'html.parser')
    # find the current price
    textk = sp.find('div', attrs={
        'class': 'BNeawe iBp4i AP7Wnd'
    }).find({
        'div': 'BNeawe iBp4i AP7Wnd'
    }).text
    return textk


price = get_latest_crypto_price('bitcoin')
print('BITCOIN price : ' + price)
