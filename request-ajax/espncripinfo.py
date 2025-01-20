import requests
import json

with open('request-ajax/news.txt', 'w') as f:
    for i in range(1,6):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page={i}'
        res = requests.get(url)
        data = json.loads(res.text)


        for new in data:
            f.write(new['author']+ ' | ' + new['summary'])
            f.write('\n')