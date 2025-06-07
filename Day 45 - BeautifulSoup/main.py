from bs4 import BeautifulSoup
import requests 

response = requests.get("https://news.ycombinator.com/")

#print(response.text)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)
article_tag = soup.find("span", class_ = "titleline")
print(article_tag)
article_text = article_tag.getText()
print(article_text)