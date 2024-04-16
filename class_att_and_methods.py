class Song:
    count = 0
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        # Increment the count by one every time a new Song instance is created
        Song.count += 1
        # Add the genre and artist of the current song to their respective lists
        self.add_to_genres()
        # Update genre and artist counts
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

