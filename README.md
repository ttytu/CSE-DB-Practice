# Full Stack Database Practice Project

## Setup 

1. Download & Install Docker Desktop [Docker Desktop](https://www.docker.com/products/docker-desktop/) 
2. Run Docker Desktop 
3. Clone or Download Repository [CSE-DB-Practice](https://github.com/ttytu/CSE3207-Database) 
4. Open repo in IDE `CSE-DB-Practice` 
5. Make shure ports 3307, 8001, 3001 are not preoccupied 
6. Build Docker Image & Run Images in Containers `docker-compose up` 
7. Happy coding! 

## Project Structure

- GitHub 
- Docker 
- Database: MySQL `/mysql`
- API: FastAPI Python `/api`
- Frontend: React JS `/frontend` 

## GitHub

```shell
git clone https://github.com/ttytu/CSE-DB-Practice.git
```

## Dev Env - Docker Compose

- [Docker](https://www.docker.com/) 
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) 

```shell
cd CSE-DB-Practice 
docker-compose build 
docker-compose up 
```

### Project Development Container Ports

- DB server `http://localhost:3307` 
- API server `http://localhost:8001` 
- Frontend server `http://localhost:3001` 

## MySQL 

`/mysql` 

Access database container from MySQL Workbench

- Schema name: fastapi_app
- Host port: `3307`
- Initial root password: P4ssw0rd
- Tables:
  - movie
    - movieId, videoReleaseDate, releaseDate, movieTitle, year, backdrop_path, poster_path
  - movie_genres
    - mgenreId, movieId, genre
  - ratings
    - ratingsId, userId, movieId, ratingScore, timestamp
  - user
    - userId, age, gender, occupation, ZIPCODE 

![image](https://github.com/user-attachments/assets/779e6fb8-08dd-453a-9075-a7caf72a4b19)

## FastAPI 

`/api` 

Access API server container from local browser 

- API docs: http://localhost:8001/v1/docs 
- Edit code in `/CSE3207-Database/api/`
  - Database connector:
    - `/api/database/connector.py`
  - movieLens controllers:
    - `/api/movieLens/controllers.py`
  - movieLens routers:
    - `/api/movieLens/routers.py`
  - FastAPI main app:
    - `/api/main.py`
- FastAPI documentation: https://fastapi.tiangolo.com/

![image](https://github.com/user-attachments/assets/15136cea-dc33-467c-b416-7036efe8c711)

## Frontend React 

`/frontend`

Access web page from local browser 

- http://localhost:3001/ 
- Provided Pages 
  - Home, MovieDetails, MovieSearch, UserDetails
- Provided Components
  - Nav, Footer, Banner, MovieCard, MovieList, etc
- React app with Tailwind CSS
  - https://create-react-app.dev/docs/getting-started
  - https://tailwindcss.com/docs/installation 

![image](https://github.com/user-attachments/assets/c74199ad-8708-47ab-a138-e657f83c3f53)
