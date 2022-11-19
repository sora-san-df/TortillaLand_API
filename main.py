#starletee
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
#fastapi
from fastapi import FastAPI

#routers
from app.routers import Integrantes,canales_twitch, tortillas

#adding the CORS middleware

origins=[
    "*",
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=origins)
]

app = FastAPI(middleware=middleware)


app.include_router(Integrantes.router)
app.include_router(canales_twitch.router)
app.include_router(tortillas.router)
