from media import Movie
# this will only import (class movie) from (media file)

from fresh_tomatoes import open_movies_page
# this will import function (open_movies_page)
# from (file fresh_tomatoes)


# Below, Instances will be created from class Movie
# => Movie(title,Description,posterUrl,TrailerUrl)

toy_story = Movie("Toy Story",
                           "A film for a boy whose toys become Alive !!",
                  "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",  # noqa
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")


tom_and_Jerry = Movie("Tom & Jerry",
                      "Kids film 2D",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/TomandJerryTitleCardc.jpg/250px-TomandJerryTitleCardc.jpg",  # noqa
                      "https://www.youtube.com/watch?v=OdAVwckh_EE")


the_day_after_tomorrow = Movie("The day after tomorrow",
                               "A film were you feel freezing",
                               "https://images-na.ssl-images-amazon.com/images/I/51JSE1F1G9L._SY445_.jpg",  # noqa
                               "https://www.youtube.com/watch?v=Ku_IseK3xTc&t=11s")    # noqa

from fresh_tomatoes import open_movies_page


# Below, Instances will be created from class Movie
# => Movie(title,Description,posterUrl,TrailerUrl)

toy_story = Movie("Toy Story",
                  "A film for a boy whose toys become Alive !!",
                  "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",  # noqa
                  "https://www.youtube.com/watch?v=KYz2wyBy3kc")


tom_and_Jerry = Movie("Tom & Jerry",
                      "Kids film 2D",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/TomandJerryTitleCardc.jpg/250px-TomandJerryTitleCardc.jpg",  # noqa
                      "https://www.youtube.com/watch?v=OdAVwckh_EE")


the_day_after_tomorrow = Movie("The day after tomorrow",
                               "A film were you feel freezing",
                               "https://images-na.ssl-images-amazon.com/images/I/51JSE1F1G9L._SY445_.jpg",  # noqa
                               "https://www.youtube.com/watch?v=Ku_IseK3xTc&t=11s")  # noqa

finding_nemo = Movie("Finding Nemo",
                     "Animation Film",
                     "https://www.countynewscenter.com/wp-content/uploads/FindingNemo.jpg",  # noqa
                     "https://www.youtube.com/watch?v=wZdpNglLbt8")

movies_list = [the_day_after_tomorrow, toy_story,
               tom_and_Jerry, finding_nemo]

# will create a list of movies
# that we will sent to the function open_movies_page
# that is in fresh_tomatoes file

open_movies_page(movies_list)
# will open  movies  web page
# using open_movies_page function
# which is in file fresh_tomatoes


finding_nemo = Movie("Finding Nemo",
                     "Animation Film",
                     "https://www.countynewscenter.com/wp-content/uploads/FindingNemo.jpg",  # noqa
                     "https://www.youtube.com/watch?v=wZdpNglLbt8")

movies_list = [the_day_after_tomorrow, toy_story,
               tom_and_Jerry, finding_nemo]

# will create a list of movies
# that we will sent to the function open_movies_page
# that is in fresh_tomatoes file

open_movies_page(movies_list)
# will open  movies  web page
# using open_movies_page function
# which is in file fresh_tomatoes
