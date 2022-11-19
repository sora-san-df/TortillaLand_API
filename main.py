# #starletee
# from starlette.middleware import Middleware
# from starlette.middleware.cors import CORSMiddleware
#fastapi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#routers
from app.routers import Integrantes,canales_twitch, tortillas

#adding the CORS middleware

app = FastAPI()

origins =[
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(Integrantes.router)
app.include_router(canales_twitch.router)
app.include_router(tortillas.router)
