import requests
from bs4 import BeautifulSoup
from time import sleep

def main(url):
    '''Returns request and soup objects'''
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    text = [i.get_text() for i in soup.find_all('p')]
    return r,soup,text


def prints(txt):
    '''Iterates through text in p tags'''
    for i in range(len(txt)):
        print(txt[i])
        input("\n\t —- Hit enter —- \n\n")



if __name__ == '__main__':
    main(url)
