from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from movieLens.models import Movie, MovieGenre, User, Rating
from movieLens.controllers import (
    get_movies,
    get_movie,
    get_users,
    get_user,
    get_genres,
    get_genre,
    get_ratings,
    get_rating, 
    get_user_rating,
    get_movie_rating, 
    get_movie_genre
)


movie_router = APIRouter()
user_router = APIRouter()
genre_router = APIRouter()
rating_router = APIRouter()


# Movie Controllers

@movie_router.get("/v1/movie")
def get_movies_api(limit: int = 10, offset: int = 0):
    """
    This movies get API allow you to fetch all movie data.
    """
    movies = get_movies(limit, offset)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(movies))


@movie_router.get("/v1/movie/{movie_id}")
def get_movie_api(movie_id: int):
    """
    This movie API allow you to fetch specific movie data.
    """
    movie = get_movie(movie_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(movie))


@movie_router.get("/v1/movie/{movie_id}/rating")
def get_movie_rating_api(movie_id: int):
	"""
	This rating API allow you to fetch specific rating data.
	"""
	rating = get_movie_rating(movie_id)
	return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(rating))


@movie_router.get("/v1/movie/{movie_id}/genre")
def get_movie_genre_api(movie_id: int):
	"""
	This genre API allow you to fetch specific genre data.
	"""
	genre = get_movie_genre(movie_id)
	return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(genre))


# User Controllers

@user_router.get("/v1/user")
def get_users_api(limit: int = 10, offset: int = 0):
    """
    This users get API allow you to fetch all user data.
    """
    users = get_users(limit, offset)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(users))


@user_router.get("/v1/user/{user_id}")
def get_user_api(user_id: int):
    """
    This user API allow you to fetch specific user data.
    """
    user = get_user(user_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user))


@user_router.get("/v1/user/{user_id}/rating")
def get_user_rating_api(user_id: int):
	"""
	This rating API allow you to fetch specific rating data.
	"""
	rating = get_user_rating(user_id)
	return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(rating))


# Genre Controllers

@genre_router.get("/v1/genre")
def get_genres_api(limit: int = 10, offset: int = 0):
    """
    This genres get API allow you to fetch all genre data.
    """
    genres = get_genres(limit, offset)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(genres))


@genre_router.get("/v1/genre/{genre_id}")
def get_genre_api(genre_id: int):
    """
    This genre API allow you to fetch specific genre data.
    """
    genre = get_genre(genre_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(genre))


# Rating Controllers

@rating_router.get("/v1/rating")
def get_ratings_api(limit: int = 10, offset: int = 0):
    """
    This ratings get API allow you to fetch all rating data.
    """
    ratings = get_ratings(limit, offset)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(ratings))


@rating_router.get("/v1/rating/{rating_id}")
def get_rating_api(rating_id: int):
	"""
	This rating API allow you to fetch specific rating data.
	"""
	rating = get_rating(rating_id)
	return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(rating))
