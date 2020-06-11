import tkinter as tk
import requests
import bs4
from random import choices

# main tkinter window
root = tk.Tk()

# requests object
url = "http://www.yahoo.com/news"
r = requests.get(url)

# soup object
soup = bs4.BeautifulSoup(r.text,'lxml')
pTags = [i.getText() for i in soup.find_all("p")]

# random element from pTags
def returnRandomElement():
    randElement = choices(pTags)
    return randElement

# pack elements
def packLabel():
    userCount = int(input("Enter total labels "))
    for i in range(userCount):
        tk.Label(root, text=f"{returnRandomElement()}{i+1}").grid(row=i)

def packEntry():
    userCount = int(input("Enter total Entry: "))
    for i in range(userCount):
        tk.Entry(root).grid(row=i,column=1)

def packButton():
    userCount = int(input("Enter total buttons: "))
    for i in range(userCount):
        tk.Button(root, text=f"LETS GET STARTED!{i+1}").grid(row=i,column=2)

# call functions
packLabel()
packEntry()
packButton()



# tk.Label(root, text="First").grid(row=0)
# tk.Label(root, text="Second").grid(row=1)

# e1 = tk.Entry(root)
# e2 = tk.Entry(root)

# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)

root.mainloop()