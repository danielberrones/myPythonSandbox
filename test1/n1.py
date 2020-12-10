import requests, bs4, re

url = 'https://www.espn.com/mma/story/_/id/21807736/jorge-masvidal-douglas-lima-shake-welterweight-rankings'

r = requests.get(url)
soup = bs4.BeautifulSoup(r.text,'lxml')

arr = []
for i in soup.find_all("h2"):
    arr.append(i)

newArr = []
for i in range(len(arr)):
    newArr.append(arr[i].getText())

arr1 = []
for i in soup.find_all("h3"):
    arr1.append(i)

newArr2 = []
for i in range(len(arr)):
    newArr2.append(arr1[i].getText())

print(newArr[0])
for i in range(10):
    print(newArr2[i])


