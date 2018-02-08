import requests, json
from bs4 import BeautifulSoup
import sys

from check_source import checkSource

url = 'https://www.wikipedia.org/'

if 'none' in checkSource(url):
    print('no cms')
else:
    print('success')

"""
f = open('accounts.txt')

KEY = 'cb6326ba-8058-4476-88cd-33b76ceb490b'
URL = 'sitefinity.com'
api = 'https://api.builtwith.com/free1/api.json?KEY={}&LOOKUP={}'.format(KEY, URL)
res = requests.get(api)
parsed = json.loads(res.text)
print(json.dumps(parsed, indent=2, sort_keys=True))
"""
