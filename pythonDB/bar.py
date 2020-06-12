import requests
from bs4 import BeautifulSoup
from collections import Counter


def main(url):
    
    #url = 'http://www.python.org/blog'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')
    htmlTags = [i.name for i in soup.find_all(True)]
    c = Counter(htmlTags)
    for k,v in c.items():
        print(k,v)
    print("This is the length of htmlTags: {}".format(len(htmlTags)))
    print("These are the top 3 most popular tags: {}".format(c.most_common(3)))
    print("The website you entered is: {}".format(url))
    print("Would you like to save this file?")
    answer = int(input("1) Yes\n2) No"))
    if answer == 1:
        print("Okay we are going to save the file for you.")
        with open("linuxRules.txt","w") as f:
            f.write(str(c.items()))
    else:
        print("Have a good day!") 


main(input("Enter URL"))
