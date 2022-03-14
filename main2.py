import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h3", class_="title").get_text()

movie_list = [title.get_text() for title in soup.findAll("h3", class_="title")]
movie_list.reverse()

# write into csv
movie_df = pd.DataFrame(movie_list)
csv_file_name = 'top_100_movies.csv'
movie_df.to_csv(csv_file_name, index=False)

# write into txt
with open("movies.txt", mode="w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")



