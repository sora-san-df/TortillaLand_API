#python
from typing import List
#fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware

#routers
from app.routers import Integrantes,canales_twitch, tortillas


app = FastAPI()

#accepted origins for the CORS 
# origins: list = [
#     "https://cq0ykg.deta.dev/docs",
#     "https://cq0ykg.deta.dev/integrantes",
#     "https://cq0ykg.deta.dev/canales_twitch"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
)

app.include_router(Integrantes.router)
app.include_router(canales_twitch.router)
app.include_router(tortillas.router)
