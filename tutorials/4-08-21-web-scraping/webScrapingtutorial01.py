import requests
import bs4

result = requests.get("http://www.example.com")

print(type(result))

x = result.text

print(x)

soup = bs4.BeautifulSoup(x, "lxml")

print(soup)

print(soup.select('title'))
site_paragraphs = soup.select('p')
print(soup.select('h1'))
print(site_paragraphs[0].getText())