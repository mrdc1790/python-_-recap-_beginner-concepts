import requests
from bs4 import BeautifulSoup

res = requests.get('https://en.wikipedia.org/wiki/Julius_Caesar')

soup = BeautifulSoup(res.text, 'lxml')

brutus_Profilepic_SET = soup.select('.infobox-image')
brutus_Profilepic_TAG = soup.select('.image')[3]
brutus_Bust = soup.select('.image')
print(type(brutus_Profilepic_SET))
print(type(brutus_Profilepic_TAG))

image_link_julius = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Sulla_Glyptothek_Munich_309.jpg/170px-Sulla_Glyptothek_Munich_309.jpg")
f = open('lucius_Sulla_marbleStatue.jpg', 'wb')
f.write(image_link_julius.content)
f.close()

## ^ craziness up above get more learned in this
