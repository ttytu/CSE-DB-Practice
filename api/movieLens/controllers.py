from fastapi import HTTPException, status
from database.connector import DatabaseConnector


# User Controllers


def get_users(limit: int = 10, offset: int = 0) -> list[dict]:
    database = DatabaseConnector()
    users = database.query_get(
        """
        SELECT
            user.userId,
            user.age,
            user.gender,
            user.occupation,
            user.ZIPCODE
        FROM user
        LIMIT %s OFFSET %s;
        """,
        (limit, offset),
    )
    return users


def get_user(id: int) -> dict:
    database = DatabaseConnector()
    users = database.query_get(
        """
        SELECT
            user.userId,
            user.age,
            user.gender,
            user.occupation,
            user.ZIPCODE
        FROM user
        WHERE id = %s
        """,
        (id),
    )
    if len(users) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return users[0]


# Movie Controllers


def get_movies(limit: int = 10, offset: int = 0) -> list[dict]:
    database = DatabaseConnector()
    movies = database.query_get(
        """
        SELECT
            movie.movieId,
            movie.movieTitle,
            movie.releaseDate,
            movie.videoReleaseDate,
            movie.IMDbURL
        FROM movie
        LIMIT %s OFFSET %s
        """,
        (limit, offset),
    )
    return movies


def get_movie(id: int) -> dict:
    database = DatabaseConnector()
    movies = database.query_get(
        """
        SELECT
            movie.movieId,
            movie.movieTitle,
            movie.releaseDate,
            movie.videoReleaseDate,
            movie.IMDbURL
        FROM movie
        WHERE id = %s
        """,
        (id),
    )
    if len(movies) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    return movies[0]


# Rating Controllers


def get_ratings(limit: int = 10, offset: int = 0) -> list[dict]:
    database = DatabaseConnector()
    ratings = database.query_get(
        """
		SELECT
			rating.ratingId,
			rating.userId,
			rating.movieId,
			rating.ratingScore,
			rating.timestamp
		FROM rating
		LIMIT %s OFFSET %s
		""",
        (limit, offset),
    )
    return ratings


def get_rating(user_id: int) -> list[dict]:
    database = DatabaseConnector()
    ratings = database.query_get(
        """
		SELECT
			rating.ratingId,
			rating.userId,
			rating.movieId,
			rating.ratingScore,
			rating.timestamp
		FROM rating
		WHERE userId = %s
		""",
        (user_id),
    )
    if len(ratings) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
    return ratings


# Genre Controllers


def get_genres(limit: int = 10, offset: int = 0) -> list[dict]:
    database = DatabaseConnector()
    genres = database.query_get(
        """
		SELECT
			genre.genreId,
			genre.movieId,
			genre.genre
		FROM genre
		LIMIT %s OFFSET %s
		""",
        (limit, offset),
    )
    return genres


def get_genre(movie_id: int) -> list[dict]:
    database = DatabaseConnector()
    genres = database.query_get(
        """
		SELECT
			genre.genreId,
			genre.movieId,
			genre.genre
		FROM genre
		WHERE movieId = %s
		""",
        (movie_id),
    )
    if len(genres) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found")
    return genres
