# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com'
content = requests.get(url)
html = content.text

soup = BeautifulSoup(html, 'html5lib')

headings = []
for heading in soup.find_all(class_="story-heading"):
    headings.append(repr(heading.get_text()))

headings2 = [heading.get_text().replace('\n', ' ').strip() for heading in soup.find_all(class_="story-heading")]

print(type(headings))
for h in headings2:
    print(h)

print(len(headings))
print(headings[138])
