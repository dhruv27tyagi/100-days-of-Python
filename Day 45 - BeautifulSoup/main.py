from bs4 import BeautifulSoup
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'lxml')
print(soup.title)

all_anchor_tags = soup.find_all(name="a")

print(all_anchor_tags)

for tag in all_anchor_tags:
    tag.get("href") 