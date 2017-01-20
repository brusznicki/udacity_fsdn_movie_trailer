from bs4 import BeautifulSoup
import fresh_tomatoes
import json
import media
import re
import urllib
import urllib2


def get_trailer_youtube_url(movie_title):
    # Takes a movie title and returns URL to first trailer result on youtube
    video_youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    # Set rick roll as default value in case google isn"t responsive
    query = urllib.quote(movie_title + "trailer")
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    # Uses "html.parser" for cross platform compatibility, you can swap out
    # and use whatever parser you'd like.
    if soup:
        video = soup.findAll(attrs={"class":"yt-uix-tile-link"})[0]
        # Take the first result. We trust you google
        video_youtube_url = "https://www.youtube.com" + video["href"]
    return video_youtube_url


def get_story_line_and_poster_image_url(movie_title):
    # Takes a movie title and uses OMDB API to get poster and plot
    # OMDB API: https://www.omdbapi.com/
    imdb_title = re.sub(r"\s+", "+", movie_title)
    # reformats title for use in API query
    imdb_search_prefix = "http://www.omdbapi.com/?t="
    imdb_search_suffix = "&y=&plot=short&r=json"
    imdb_search_string = imdb_search_prefix + imdb_title + imdb_search_suffix
    imdb_data = json.load(urllib2.urlopen(imdb_search_string))
    if "Plot" in imdb_data:  # Not every JSON response contains Plot or Poster
        story_line = imdb_data["Plot"]
    else:
        story_line = "A movie about " + movie_title
    if "Poster" in imdb_data:
        poster_image_url = imdb_data["Poster"]
    else:
        # Use the IMDB "photo not found" image
        poster_image_url = """ http://ia.media-imdb.com/images/G/01/imdb/images
                               /nopicture/32x44/film-3119741174._CB522736599_
                               .png"""

    return story_line, poster_image_url


movie_titles = ["Rudy",  # A list of movies we want to show on movie page.
                "Heat",
                "The Neverending Story",
                "Prometheus",
                "Time Bandits",
                "Ice Pirates",
                "Flight of The Navigator",
                "Flash Gordon",
                "Ghost in the Shell",
                "The Big Lebowski",
                "Trainspotting",
                "Lock, Stock, and Two Smoking Barrels"
                ]
# Initialize the list of Movie Objects
movies = []

for movie_title in movie_titles:
    trailer_youtube_url = get_trailer_youtube_url(movie_title)
    story_line, poster_image_url = (
        get_story_line_and_poster_image_url(movie_title))
    movies.append(media.Movie(movie_title,
                              story_line,
                              poster_image_url,
                              trailer_youtube_url))

fresh_tomatoes.open_movies_page(movies)
