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
)


router = APIRouter()


@router.get("/v1/movie")
def get_movies_api(limit: int = 10, offset: int = 0):
    """
    This movies get API allow you to fetch all movie data.
    """
    movies = get_movies(limit, offset)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(movies))


@router.get("/v1/movie/{movie_id}")
def get_movie_api(movie_id: int):
    """
    This movie API allow you to fetch specific movie data.
    """
    movie = get_movie(movie_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(movie))


@router.get("/v1/user")
def get_users_api(limit: int = 10, offset: int = 0):
    """
    This users get API allow you to fetch all user data.
    """
    users = get_users(limit, offset)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(users))


@router.get("/v1/user/{user_id}")
def get_user_api(user_id: int):
    """
    This user API allow you to fetch specific user data.
    """
    user = get_user(user_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(user))


@router.get("/v1/genre")
def get_genres_api(limit: int = 10, offset: int = 0):
    """
    This genres get API allow you to fetch all genre data.
    """
    genres = get_genres(limit, offset)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(genres))


@router.get("/v1/genre/{genre_id}")
def get_genre_api(genre_id: int):
    """
    This genre API allow you to fetch specific genre data.
    """
    genre = get_genre(genre_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(genre))


@router.get("/v1/rating")
def get_ratings_api(limit: int = 10, offset: int = 0):
    """
    This ratings get API allow you to fetch all rating data.
    """
    ratings = get_ratings(limit, offset)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(ratings))


@router.get("/v1/rating/{user_id}")
def get_rating_api(user_id: int):
    """
    This rating API allow you to fetch specific rating data.
    """
    rating = get_rating(user_id)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(rating))
