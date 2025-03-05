## CSE Database Practice Project

### Setup 

1. Download & Install Docker Desktop [Docker Desktop](https://www.docker.com/products/docker-desktop/) 
2. Run Docker Desktop 
3. Clone or Download Repository [CSE-DB-Practice](https://github.com/ttytu/CSE3207-Database) 
4. Open repo in IDE `CSE-DB-Practice` 
5. Make shure ports 3307, 8001, 3001 are not preoccupied 
6. Build Docker Image & Run Images in Containers `docker-compose up` 
7. Happy coding! 

--- 

### Project Structure

- GitHub 
- Docker 
- Database: MySQL `/mysql`
- API: FastAPI Python `/api`
- Frontend: React JS `/frontend` 

--- 

### GitHub

```shell
git clone https://github.com/ttytu/CSE3207-Database.git
```

--- 

### Dev Env - Docker Compose

- [Docker](https://www.docker.com/) 
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) 

```shell
cd CSE3207-Database 
docker-compose build 
docker-compose up 
```

#### Project Development Container Ports

- DB server `http://localhost:3307` 
- API server `http://localhost:8001` 
- Frontend server `http://localhost:3001` 

--- 

### MySQL 

`/mysql` 

--- 

### FastAPI 

`/api` 

--- 

### Frontend React 

`/frontend`

--- 

