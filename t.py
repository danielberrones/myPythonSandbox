import tkinter as tk
import requests
import bs4
from random import choice

# main tkinter window
root = tk.Tk()

# requests object
url = "http://www.yahoo.com/news"
r = requests.get(url)

# soup object
soup = bs4.BeautifulSoup(r.text,'lxml')
pTags = [i.getText() for i in soup.find_all("p")]

# return random <p> tag
def returnRandomElement():
    randElement = choice(pTags)
    if len(randElement) <= 0:
        returnRandomElement()
    else:
        return randElement

def main():
    tk.Label(root,text="Yahoo News",font=("Helvetica", 45),background="gold").grid(row=0,ipadx=100)
    for i in range(2):
        tk.Label(root,text=returnRandomElement(),wraplength=500,font=("Helvetica", 20), background="whitesmoke").grid(row=i+1)
    tk.Button(root, text="Exit",command=root.destroy,font=("Helvetica", 22)).grid(row=1,column=2)


main()
root.mainloop()