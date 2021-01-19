import bs4, requests

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

def returnReqObj(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    return soup

soup = returnReqObj(url)

td = [i.get_text() for i in soup.find_all('td', class_='titleColumn')]

for i in td:
        print(i.strip('/n'))

        