import requests
from bs4 import BeautifulSoup


url = "https://www.quora.com/What-cool-things-can-you-do-with-web-scraping-software"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
pTags = [i.getText() for i in soup.find_all("p")]

for i in pTags:
    print(i)

with open("deleteMe.txt","w") as f:
    for i in pTags:
        f.write(str(i))

        