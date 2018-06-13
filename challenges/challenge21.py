# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com'
content = requests.get(url)
html = content.text
soup = BeautifulSoup(html, 'html5lib')

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        with open('ch21_art.txt', 'a') as open_file:
            open_file.write(story_heading.a.text)
    else:
        with open('ch21_art.txt', 'a') as open_file:
            open_file.write(story_heading.contents[0])
