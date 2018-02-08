import requests, json
from bs4 import BeautifulSoup

def checkSource(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    try:
        text = soup.find('meta', attrs={'name':'Generator'})
        cms = text['content']
    except:
        cms = "none"
    return cms
