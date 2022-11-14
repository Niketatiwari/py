import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

def get_soup(url):
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text)
    return None

def get_news(item):
    data = {}
    heading = item.find("h2", class_= "newsHdng")
    source = item.find('span', class_= 'posted-by')
    content = item.find('p', class_= 'newscont')
    if heading is not None:
        data['heading'] = heading.text.strip()
    if source is not None:
        data['source'] = source.text.strip()
    if content is not None:
        data['content'] = content.text.strip()
    return data

def get_news_list(soup):
    headlines = []
    news = soup.find_all('div', class_='news-listing')
    for item in news:
        headlines.append(get_news(items))
    return headlines


def main():
    pos = 1
    base_url = "https://www.mdtv.com/latest/"
    while True:
        url = f'{base_url}?page={pos}'
        print('➡️',url)
        soup = get_soup(url)
        if soup is None:
            break

