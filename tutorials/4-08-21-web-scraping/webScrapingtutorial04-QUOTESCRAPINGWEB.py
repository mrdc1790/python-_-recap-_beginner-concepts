import requests
from bs4 import BeautifulSoup

### DOESNT WORK FOR MULTIPLE PAGES ###

i = 0
authorSet = []
quotesArray = []
tagsArray = []
result = []
page_num = 1

res = requests.get(f"http://quotes.toscrape.com/page/{page_num}/")
soup = BeautifulSoup(res.text, 'lxml')
sentenceAuthor = soup.select('.author')
topTenTagsBox = soup.find_all("span", class_="tag-item")
nextOrNot = soup.select('.next')[0]('span')[0]
print(nextOrNot)

for x in topTenTagsBox:
    result.extend(x.find_all('a', class_="tag"))

for line in sentenceAuthor:
    authorSet.append((soup.select('.author')[i]).text)
    quotesArray.append((soup.select('.quote')[i]('span')[0]).text)
    tagsArray.append((result[i].text))
    if next==None:
        break
    else:
        i+=1

for count, item in enumerate(quotesArray, 0):
    print(item+" - "+authorSet[count],end="\n")

print("The top ten categories: ")
for i in tagsArray:
    print("\t\t\t-"+str(i))