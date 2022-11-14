#Python 
import json
from typing import List
#Pydantic
#fastAPI
from fastapi import APIRouter,status, Body, Path
#datos integrantes
from ..DB import datos_integrantes


router = APIRouter()

@router.get(
    path="/integrantes",
    status_code=status.HTTP_200_OK,
    tags=["integrantes"],
    summary="Mostrar los intengrates de tortilla"
)
def integrantes(): 
    """
    integrantes 

    la funcion integrantes en teoria deberia devolverme un json con los datos de los integrantes(en este caso de ejemplo seria 1)


    Params:
     -None

    Returns: 
    Un json con los datos de los integrantes.
    """
    data = datos_integrantes.db
    return   data