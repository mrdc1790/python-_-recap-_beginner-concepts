# soup.select('div') -> all elements with 'div tag'
# soup.select('#some_id') -> elements containing id='some_id'
# soup.select('.some_class') -> elements containing class = 'some_class'
# soup.select('div span') -> any elements named span within a div element
# soup.select('div > span') -> any elements named span directly within a div element, with nothing in between
# LOOK UP MORE SOUP DOCUMENTATION

import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Julius_Caesar")
soup = bs4.BeautifulSoup(res.text, "lxml")
print(type(soup))
toctext = soup.select('.toctext')
print(type(toctext))
first_category = soup.select('.toctext')[0]
print(type(first_category))
for item in soup.select('.toctext'):
    print(item.text)