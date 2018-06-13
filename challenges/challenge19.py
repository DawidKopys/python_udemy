# Using the requests and BeautifulSoup Python libraries, print to the screen the full
# text of the article on this website:
# http://content.time.com/time/magazine/article/0,9171,2005869,00.html
from bs4 import BeautifulSoup
import requests

base_url = 'http://content.time.com'
url = 'http://content.time.com/time/magazine/article/0,9171,2005869,00.html'
content_html = requests.get(url).text
soup = BeautifulSoup(content_html, 'html5lib')

txt = soup.find(class_='entry-content group')
txt = txt.find_all('p')
for par in txt:
    print(par.get_text())

url = base_url + soup.find(class_='next').get('href')
print(url)
content_html = requests.get(url).text
soup = BeautifulSoup(content_html, 'html5lib')

txt = soup.find(class_='entry-content group')
txt = txt.find_all('p')
for par in txt:
    print(par.get_text())
