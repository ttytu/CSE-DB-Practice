from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from movieLens.routers import router as router


# Set API info
app = FastAPI(
    title="Example API",
    description="This is an example API of FastAPI",
    contact={
        "name": "Masaki Yoshiiwa",
        "email": "masaki.yoshiiwa@gmail.com",
    },
    docs_url="/v1/docs",
    redoc_url="/v1/redoc",
    openapi_url="/v1/openapi.json",
)

# Set CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:4000",
    "http://localhost:19006",
    # Add your frontend URL here...
]

# Set middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
User APIs
Provides user CRUD APIs.
"""

app.include_router(router)
