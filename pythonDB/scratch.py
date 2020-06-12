import requests
from bs4 import BeautifulSoup


url = 'https://finance.yahoo.com/quote/CECO?p=CECO&.tsrc=fin-srch'

r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
print(soup.prettify())
print(r.status_code)

indicators = [
    "Previous Close",
    "Open",
    "Bid",
    "Ask",
    "Day's Range",
    "52 Week Range",
    "Volume",
]

htmlText = r.text

splitList = htmlText.split('Previous Close')

print("Found: ", splitList[1].split("\">")[1])
