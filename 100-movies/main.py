from bs4 import BeautifulSoup
import requests
import os

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text
soup = BeautifulSoup(movies_page, "html.parser")
movies = soup.find_all('h3', attrs={"class": "title"})
movie_titles = [x.get_text() for x in movies]
all_movies = [m for m in movie_titles]
all_movies.reverse()

path = os.path.join(os.path.dirname(__file__), 'movies.txt')

with open(path, 'w', encoding="utf8") as f:
    for movie in all_movies:
        f.write(movie+'\n')
