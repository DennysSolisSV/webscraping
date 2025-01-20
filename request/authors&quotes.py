import requests

html = ''
text = ''
author = '' 
quote = ''
for i in range(1,11):
    r = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    html += r.text

with open('request/authors&quotes.csv', 'w', encoding='utf-8') as f:
    for line in html.split('\n'):
        


        if '<span class="text" itemprop="text">“' in line:
            line = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
            quote = line.strip()

            text = 'comodine' + quote

        
        if '<small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            author = line.strip()
            text =  f"{author}, {quote}"
            f.write(text)
            f.write('\n')
        

    

