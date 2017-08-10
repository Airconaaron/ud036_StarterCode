class Movie ():
    def __init__(self, title, description, poster, trailer):
        """
        This is a class that will store each of our movies.
        Each instance will have the name, description,
        poster image and youtube url.
        """
        self.title = title
        self.description = description
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
