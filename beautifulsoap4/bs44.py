from bs4 import BeautifulSoup 
import requests
r = requests.get('https://quotes.toscrape.com/')
html = r.text

soup = BeautifulSoup(html, 'html.parser')

# print(soup.title.string)
# print(soup.title.parent)
# print(soup.title.parent.name)


# print(soup.find_all('span'))

# for tag in soup.findAll('a'):
#     print(tag)

# quotes
with open('beautifulsoap4/bs4quotes.txt', 'w') as f:
    for tag in soup.findAll('span', {'class':'text'}):
        f.write(tag.text)
        f.write('\n')

# author names
with open('beautifulsoap4/bs4authornames.txt', 'w') as f:
    for tag in soup.findAll('small', {'class':'author'}):
        f.write(tag.text)
        f.write('\n')
