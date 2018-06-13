# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com'
content = requests.get(url)
html = content.text
soup = BeautifulSoup(html, 'html5lib')

i = 0
for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print('wtf'+story_heading.a.text.replace("\n", " ").strip())
        i = i + 1
    else:
        print(story_heading.contents[0].strip())
        i = i + 1

print()
