import requests
import json
url = 'https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page=1'
res = requests.get(url)
data = json.loads(res.text)


for new in data:
    print(new)
    print('------------------')