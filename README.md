# udacity_fsdn_movie_trailer
Movie Trailer Project for Full Stack Developer Nano Degree written in Python

Entertainment Center takes a list of your favorite films and rapidly builds a fan website with photos, descriptions, and videos. 

## Quick start

This project requires that you have a few third party packages installed.

- Clone the repo: `git clone https://github.com/twbs/bootstrap.git`
- Install [Fresh Tomatoes](https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py)
- Install with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): `pip install beautifulsoup or easy_install beautifulsoup`
- Make sure fresh_tomatoes.py, media.py, and entertainment_center.py are all installed in the same directory
- Run entertainment_center.py from IDLE

### How It Works

Rather than type out all of the arguments needed for creating our Movie objects, this solution to the project takes a list of string literals representign our favorite movies and then fetches values for those arguments from Youtube and IMDB via the OMDB API. Because these are done each time the script is run and the results aren't saved, there is a performance hit. That said the code could be refactored to be used with a data source and more technologies to save query responses. A view can also be created to prompt users to add to their list of favorite movies using normalized movie titles as provided by another API (perhaps the OMDB API as well).

## Creators

**Chris Brusznicki**

- <https://github.com/brusznicki>
