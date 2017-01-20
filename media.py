import webbrowser

class Movie(object):
    """This class models movies for fan websites that display information about different films """
    VALID_RATINGS =  ['G','PG','PG-13','R']
    def __init__(self, movie_title, movie_story_line, movie_poster_image, movie_youtube_trailer):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_youtube_trailer
        

    def play_trailer(self):
        """Open a webbrowser and load the url to a youtube trailer for the movie"""
        webbrowser.open(self.youtube_trailer_url)
