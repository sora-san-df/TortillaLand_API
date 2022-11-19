#python
from typing import List
#fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#routers
from app.routers import Integrantes,canales_twitch, tortillas


app = FastAPI()
#adding the CORS middleware
origins=[
    "https://cq0ykg.deta.dev/integrantes",
    "https://cq0ykg.deta.dev/integrantes/canales_twitch",
    "https://cq0ykg.deta.dev/tortillas"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["accept"]
)



app.include_router(Integrantes.router)
app.include_router(canales_twitch.router)
app.include_router(tortillas.router)
