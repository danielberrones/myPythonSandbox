import requests
import bs4

def main():
    'docstring'
    searchParam = 'https://google.com/search?q=Alan+Watts'
    r = requests.get(searchParam)
    # todo
    soup = bs4.BeautifulSoup(r.text,'lxml')
    return soup

main()