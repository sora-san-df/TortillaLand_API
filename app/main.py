#sys
import sys
#fastapi
from fastapi import FastAPI

#routers
from .routers import Integrantes


app = FastAPI()

app.include_router(Integrantes.router)
