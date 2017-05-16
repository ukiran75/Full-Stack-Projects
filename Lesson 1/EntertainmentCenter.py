import Media
import fresh_tomatoes

toy_story = Media.Movie("Toy Story", "A Story of a boy and his toys that comes to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
bahubali = Media.Movie("Bahubali", "A tory of two brothers fighting for the kingdom",
                       "https://www.desiretrees.in/wp-content/uploads/2017/02/Bahubali-Part-2-Baahubali-2-First-Look-Poster-Bahubali-The-Conclusion-HD-Images-Pics-Wallpapers-Shooting-Stills-1.jpg",
                       "https://www.youtube.com/watch?v=qD-6d8Wo3do")
movies = [toy_story, bahubali]
#fresh_tomatoes.open_movies_page(movies)

print(Media.Movie.__doc__)