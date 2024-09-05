from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
n = len(movies)

with open("movies.txt", "w") as file:
    for i in range(n - 1, -1, -1):
        file.write(f"{movies[i]}\n")