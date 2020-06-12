import requests
from bs4 import BeautifulSoup
from sys import argv

script, url = argv

url1 = "".join(url)

r = requests.get(url1)


soup = BeautifulSoup(r.text,'lxml')

i=1
with open('new.txt','w') as f:
    for links in soup.find_all('a'):
        f.write(str(links.get('href')))
        f.write('\n')
        f.write(str(i))
        i += 1

f.close()

with open('new.txt','r') as f:
    for x in range(len('new.txt')):
        print(f.readline())
