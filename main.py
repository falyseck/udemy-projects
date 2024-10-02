from bs4 import BeautifulSoup
import requests
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(response, "html.parser")

titles = soup.find_all(name="h3", class_="title")
text=[]
for title in titles:
    text.append(title.getText())

# Write to file with corrected numbering
with open('movies_list.txt', 'w', encoding='utf-8') as file:
    for i, movie in enumerate(reversed(text), 1):  # Reversed to get correct order
        if ")" in movie:
            new_line = f"{i}) {movie.split(') ', 1)[1]}\n"  # Correct numbering

        else:
            new_line = f"{movie}\n"
        file.write(new_line)