from fastapi import HTTPException, status
from database.connector import DatabaseConnector


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
			movie.year, 
			movie.backdrop_path,
			movie.poster_path
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
			movie.year, 
			movie.backdrop_path,
			movie.poster_path
		FROM movie
		WHERE movie.movieId = %s
		""",
		(id),
	)
	if len(movies) == 0:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
	return movies[0]


def get_movie_rating(movie_id: int) -> list[dict]:
	database = DatabaseConnector()
	ratings = database.query_get(
		"""
		SELECT
			ratings.ratingId,
			ratings.userId,
			ratings.movieId,
			ratings.ratingScore,
			ratings.timestamp
		FROM ratings
		WHERE ratings.movieId = %s
		""",
		(movie_id),
	)
	if len(ratings) == 0:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
	return ratings


def get_average_rating(movie_id: int) -> float:
	database = DatabaseConnector()
	rating = database.query_get(
		"""
		SELECT
			AVG(ratings.ratingScore)
		AS average_rating
		FROM ratings
		WHERE ratings.movieId = %s
		""",
		(movie_id),
	)
	if len(rating) == 0:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No ratings found for this movie")
	return rating[0]['average_rating']


def get_movie_genre(movie_id: int) -> list[dict]:
	database = DatabaseConnector()
	genres = database.query_get(
		"""
		SELECT
			movie_genres.mgenreId,
			movie_genres.movieId,
			movie_genres.genre
		FROM movie_genres
		WHERE movie_genres.movieId = %s
		""",
		(movie_id),
	)
	if len(genres) == 0:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found")
	return genres


def search_movies(query: str, limit: int = 10, offset: int = 0) -> list[dict]:
	database = DatabaseConnector()
	movies = database.query_get(
		"""
		SELECT
			movie.movieId,
			movie.movieTitle,
			movie.releaseDate,
			movie.videoReleaseDate,
			movie.year, 
			movie.backdrop_path,
			movie.poster_path
		FROM movie
		WHERE movie.movieTitle LIKE %s
		LIMIT %s OFFSET %s
		""",
		(f"%{query}%", limit, offset),
	)
	return movies


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
		WHERE user.userId = %s
		""",
		(id),
	)
	if len(users) == 0:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
	return users[0]


def get_user_rated_movies(user_id: int) -> list[dict]:
	database = DatabaseConnector()
	movies = database.query_get(
		"""
		SELECT
			movie.movieId,
			movie.movieTitle,
			movie.releaseDate,
			movie.videoReleaseDate,
			movie.year, 
			movie.backdrop_path,
			movie.poster_path,
			ratings.ratingScore,
			ratings.timestamp
		FROM movie
		INNER JOIN ratings ON movie.movieId = ratings.movieId
		WHERE ratings.userId = %s
		""",
		(user_id),
	)
	if len(movies) == 0:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movies not found")
	return movies


# Genre Controllers


def get_genres(limit: int = 10, offset: int = 0) -> list[dict]:
	database = DatabaseConnector()
	genres = database.query_get(
		"""
		SELECT
			movie_genres.mgenreId,
			movie_genres.movieId,
			movie_genres.genre
		FROM movie_genres
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
			movie_genres.mgenreId,
			movie_genres.movieId,
			movie_genres.genre
		FROM movie_genres
		WHERE movie_genres.mgenreId = %s
		""",
		(movie_id),
	)
	if len(genres) == 0:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Genre not found")
	return genres


# Rating Controllers


def get_ratings(limit: int = 10, offset: int = 0) -> list[dict]:
	database = DatabaseConnector()
	ratings = database.query_get(
		"""
		SELECT
			ratings.ratingId,
			ratings.userId,
			ratings.movieId,
			ratings.ratingScore,
			ratings.timestamp
		FROM ratings
		LIMIT %s OFFSET %s
		""",
		(limit, offset),
	)
	return ratings


def get_rating(id: int) -> dict:
	database = DatabaseConnector()
	ratings = database.query_get(
		"""
		SELECT
			ratings.ratingId,
			ratings.userId,
			ratings.movieId,
			ratings.ratingScore,
			ratings.timestamp
		FROM ratings
		WHERE ratings.ratingId = %s
		""",
		(id),
	)
	if len(ratings) == 0:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rating not found")
	return ratings[0]


def get_user_movie_rating(user_id: int, movie_id: int) -> dict:
	database = DatabaseConnector()
	ratings = database.query_get(
		"""
		SELECT
			ratings.ratingId,
			ratings.userId,
			ratings.movieId,
			ratings.ratingScore,
			ratings.timestamp
		FROM ratings
		WHERE ratings.userId = %s AND ratings.movieId = %s
		""",
		(user_id, movie_id),
	)
	if len(ratings) == 0:
		return None
	return ratings[0]
