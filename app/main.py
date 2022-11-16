#sys
import sys
#fastapi
from fastapi import FastAPI

#routers
from .routers import Integrantes,canales_twitch, tortillas


app = FastAPI()

app.include_router(Integrantes.router)
app.include_router(canales_twitch.router)
app.include_router(tortillas.router)
