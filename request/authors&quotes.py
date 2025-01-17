import requests

html = ''
for i in range(1,11):
    r = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    html += r.text

with open('authors&quotes.txt', 'w', encoding='utf-8') as f:
    for line in html.split('\n'):
        author = '' 
        quote = ''

        if '<span class="text" itemprop="text">“' in line:
            line = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
            quote = line.strip()

        if '<small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            author = line.strip()

        line = author + ' ,' + quote

        f.write(line)
        f.write('\n')
        

    

