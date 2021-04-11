## scrape http://books.toscrape.com/ to get all books with a 2 star rating

import requests
import bs4

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
two_star_titles = []
num = 1
# page_num = 12
# print(base_url.format(page_num))

for i in range(1,51):
    res = requests.get(base_url.format(i))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if (len(book.select('.star-rating.Five')) != 0):
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

for items in two_star_titles:
    print("#"+str(num)+" "+items)
    num += 1

#res = requests.get(base_url.format(1))
#soup = bs4.BeautifulSoup(res.text, 'lxml')
#products = soup.select('.product_pod')
#example = products[0]
#print(len(example.select(".star-rating.Two")))