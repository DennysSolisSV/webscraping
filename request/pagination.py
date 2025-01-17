import requests

html = ''
for i in range(1,11):
    r = requests.get(f'https://quotes.toscrape.com/page/{i}/')
    html += r.text

with open('quote.txt', 'w', encoding='utf-8') as f:
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">“' in line:
            line = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
            line = line.strip()
            f.write(line)
            f.write('\n')




def get_authors():
    with open('authors.txt', 'w') as f:
        for line in html.split('\n'):
            if '<small class="author" itemprop="author">' in line:
                line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
                line = line.strip()
                f.write(line)
                f.write('\n')



get_authors()