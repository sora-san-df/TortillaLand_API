#python
from typing import List
#fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware

#routers
from app.routers import Integrantes,canales_twitch, tortillas


app = FastAPI()

#accepted origins for the CORS 
origins: list = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(Integrantes.router)
app.include_router(canales_twitch.router)
app.include_router(tortillas.router)
