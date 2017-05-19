import webbrowser
class Movie():
    """This class stores the info about the movie"""


    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self,movie_name,movie_story_line,movie_poster,movie_trailer):
        self.title = movie_name
        self.storyLine = movie_story_line
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)