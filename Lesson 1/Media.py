import webbrowser

class Movie():
    """This class stores the info about the movie"""

    def __init__(self,movie_name,movie_poster,movie_trailer):
        self.title = movie_name
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer