class Movie():    # class containing movie attributes

    def __init__(self, movie_title, movie_storyline,
                 movie_posterimage_url, movie_traileryoutube_url):

        # def __init__ is called when we create a new object from movie  # noqa

        self.title = movie_title          # used to access title by the class instances  # noqa
        self.storyline = movie_storyline
        self.poster_image_url = movie_posterimage_url
        self.trailer_youtube_url = movie_traileryoutube_url
