"""Main Program for creation of movies and calling the web view module"""
import  media
import fresh_tomatoes

#Creating the movies objects by passing the movie info
toy_story = media.Movie("Toy Story",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

bahubali = media.Movie("Bahubali: The Conclusion",
                       "https://www.desiretrees.in/wp-content/uploads/2017/02/Bahubali-Part-2-Baahubali-2-First-Look-Poster-Bahubali-The-Conclusion-HD-Images-Pics-Wallpapers-Shooting-Stills-1.jpg",
                       "https://www.youtube.com/watch?v=qD-6d8Wo3do")

guardiansOfGalaxy = media.Movie("Guardians of Galaxy 2",
                                "http://t2.gstatic.com/images?q=tbn:ANd9GcSzRHzPW9j56dGLliOdUV0lzjeUwfALe9Zn2Ys7Kkwj4YsvDpsh",
                                "https://www.youtube.com/watch?v=wUn05hdkhjM")

thorRagnarok = media.Movie("Thor: Ragnarok",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQAmMN0WnVLHXIKsFbj7dp7-HTUmyQ_d46RruMyj7Tv33mqXy7i",
                           "https://www.youtube.com/watch?v=v7MGUNV8MxU")

sourceCode = media.Movie("Source Code",
                         "http://www.gstatic.com/tv/thumb/dvdboxart/8395541/p8395541_d_v8_aa.jpg",
                         "https://www.youtube.com/watch?v=NkTrG-gpIzE")
insideJob = media.Movie("Inside Job",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcTYPDIV0DZjHpzSbsGP1uN3N5w2CLEsNAuybEpFIoybYQbLxJ9k",
                        "https://www.youtube.com/watch?v=FzrBurlJUNk")

#Adding the created movie objects to the list
movies = [toy_story, bahubali, guardiansOfGalaxy, thorRagnarok, sourceCode, insideJob]

#Sending the movies list as an input to web view creation
fresh_tomatoes.open_movies_page(movies)