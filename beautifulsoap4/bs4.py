from bs4 import BeautifulSoup as bsoup
import requests
r = requests.get('https://quotes.toscrape.com/')
html = r.text

soup = bsoup(html, 'html.parser')

print(soup)