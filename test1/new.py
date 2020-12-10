import requests, bs4, re

url = 'https://www.espn.com/mma/story/_/id/21807736/jorge-masvidal-douglas-lima-shake-welterweight-rankings'

r = requests.get(url)
soup = bs4.BeautifulSoup(r.text,'lxml')

arr = []
for i in soup.find_all("h3"):
    arr.append(i)

newArr = []
for i in range(len(arr)):
    newArr.append(arr[i].getText())

removeThis = '1234567890. '
final = []

for i in newArr:
    if i not in removeThis:
        final.append(i.strip())


with open("writeMe.txt","w") as f:
    for i in final:
        f.write(i+"\n")
# print(final)
# str = arr[0].getText()
# str = str[2:]
# print(str.strip())