import requests
from bs4 import BeautifulSoup

url = "http://www.mouthshut.com/televisions/Sony-108cm-43-Ultra-HD-4K-Smart-LED-TV-reviews-925872893"

page = requests.get(url)

#print(page.content)

soup = BeautifulSoup(page.content, "lxml")

for item in soup.find_all("div", {"class":"more reviewdata"}):
    print(item.get_text())