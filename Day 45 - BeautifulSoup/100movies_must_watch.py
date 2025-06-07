import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")


#titles = soup.select("div.article-title-description_text h3.title")

#for title in titles:
#    print(title.get_text())

sections = soup.find_all("section", class_="gallery__content-item")
print(f"Found {len(sections)} sections")                       

titles = []
for section in sections:
    title_tag = section.find("h3", class_="title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        
        #print(title_tag.get_text(strip=True))
        titles.append(title)

final_list = titles[::-1]

with open("100 movies to watch.txt", "w", encoding="utf-8") as file:
    for movie in final_list:
        file.write(movie + "\n")