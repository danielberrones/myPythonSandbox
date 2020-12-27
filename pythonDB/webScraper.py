from collections import Counter
from bs4 import BeautifulSoup
from time import sleep
import requests


class WebScraper:
    def __init__(self, url):
        self.url = url

    def scraper(self):
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text,'lxml')

        self.box = [self.iterator.name for self.iterator in self.soup.find_all(True)]
        self.c = Counter(self.box)
        print("Success!\n")
        sleep(.5)

        #--------------------------------------------------
        # self.filename = input("Enter a filename: ")
        #--------------------------------------------------

        print("Here are the search results:")
        sleep(2)
        print("\t--> There are {} HTML Tags contained in the URL: {}".format(len(self.c),self.url))
        sleep(1)

        i = 1
        for k,v in self.c.items():
            print("\n\t\tHTML Tag #{}: ".format(i),k,v)
            i +=1

        self.mostCommon = self.c.most_common()
        self.yvalue = {y[0] for y in self.mostCommon}
        self.xvalue = {x[1] for x in self.mostCommon}

        print(self.yvalue)
        print(len(self.yvalue))

        print("\nThe most frequently used HTML tags: {} ".format(self.mostCommon))


    def newMethod(self):
        self.r = requests.get(self.url)
        self.soup = BeautifulSoup(self.r.text,'lxml')

        self.box = [self.iterator.getText() for self.iterator in self.soup.find_all("p")]
        return self.box
        # for i in self.box:
        #     print(self.box[i])
        #     input('Press enter to continue.')

def main():
    # create obj
    webScraperObject = WebScraper(input("Enter a URL: "))
    # scraper() is method in WebScraper class
    # webScraperObject.scraper()
    # calls new method
    webScraperObject.newMethod()


if __name__ == '__main__':
    main()










# THIS IS THE ORIGINAL DOCUMENT BELOW ME.  I AM TINKERING ABOVE
#
# from collections import Counter
# from bs4 import BeautifulSoup
# from time import sleep
# import requests
#
#
# class WebScraper:
#     def __init__(self, url):
#         self.url = url
#
#     def scraper(self):
#         self.r = requests.get(self.url)
#         self.soup = BeautifulSoup(self.r.text,'lxml')
#
#         self.box = [self.iterator.name for self.iterator in self.soup.find_all(True)]
#         self.c = Counter(self.box)
#         print("Success!\n")
#         sleep(1)
#
#         #--------------------------------------------------
#         # self.filename = input("Enter a filename: ")
#         #--------------------------------------------------
#
#         print("Here are the search results:")
#         sleep(1)
#         print("\t--> There are {} HTML Tags contained in the URL: {}".format(len(self.c),self.url))
#         sleep(3)
#
#         i = 1
#         for k,v in self.c.items():
#             print("\n\t\tHTML Tag #{}: ".format(i),k,v)
#             i +=1
#
#         self.mostCommon = self.c.most_common()
#         self.yvalue = {y[0] for y in self.mostCommon}
#         self.xvalue = {x[1] for x in self.mostCommon}
#
#         print(self.yvalue)
#         print(len(self.yvalue))
#
#         print("\nThe most frequently used HTML tags: {} ".format(self.mostCommon))
#
#
# def main():
#     scrapeThis = WebScraper(input("Enter a URL: "))
#     scrapeThis.scraper()
#
#
# if __name__ == '__main__':
#     main()
