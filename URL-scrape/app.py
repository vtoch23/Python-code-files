from urllib.request import urlopen
import re

url = "https://openai.com/blog/chatgpt"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

#print(title)

from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
text = text.replace(",,", "\n")
soup.find_all("img", src="/static/dionysus.jpg")

print(soup.title.string)
print(text)

image1, image2 = soup.find_all("img")
print(image1, image2)
print(image1["src"])