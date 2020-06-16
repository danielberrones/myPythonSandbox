import requests
from bs4 import BeautifulSoup

def getStarted():
    url = "https://www.quora.com/What-cool-things-can-you-do-with-web-scraping-software"
    r = requests.get(url)
    return r

def getSoup(Myparameter):
    soup = BeautifulSoup(Myparameter.text,"lxml")
    pTags = [i.getText() for i in soup.find_all("p")]
    # save to file
    with open("deleteMe.txt","w") as f:
        for i in pTags:
            f.write(str(i))


getSoup(getStarted)

# for i in pTags:
#     print(i)



