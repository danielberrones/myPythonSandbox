import requests
from bs4 import BeautifulSoup

url = 'https://scrapethissite.com/pages/simple/'

# TODO: store country and capitals into array, save to file


r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')
myHTML = soup.html

with open('scrapeThisSite.html','w') as f:
    f.write(str(myHTML))