import requests
import unicodedata
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


response = requests.get(url=URL)
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        try:
            file.write(f"{strip_accents(movie)}\n")
        except UnicodeEncodeError:
            file.write(f"{movie.split()[0]} Unicode character in title\n")
