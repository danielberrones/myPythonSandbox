import bs4, requests

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

def scrapeMovies(url):
    '''Scrape IMBDB Top 250 Movies'''
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text,'lxml')

    tableData = [i.get_text() for i in soup.find_all('td', class_='titleColumn')]
    
    with open('file1.txt','w') as f:
        for i in td:
            f.write(str(i.strip('/n')))


scrapeMovies(url)
