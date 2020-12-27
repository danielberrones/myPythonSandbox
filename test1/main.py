import requests
import bs4

url = '/Users/danielberrones/Downloads/ufc.html'

class myHTMLObj:
    def __init__(self, url):
        self.url = url
    def returnSoup(self):
        self.url = '/Users/danielberrones/Downloads/ufc.html'
        self.soup = bs4.BeautifulSoup(self.url,'lxml')
        # print(self.soup.find_all("a"))
        self.fighters = []
        for i in self.soup.find_all("div",class_="fightCardFighterName"):
            self.fighters.append(i)
        # self.fighterName = self.soup.find_all("div",class_="fightCardBout")
        # print(self.fighterName)
        print(self.fighters)

    
def main():
    obj = myHTMLObj(url)
    obj.returnSoup()

main()
