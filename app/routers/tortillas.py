#Python
#pydantic
#fastAPI
from fastapi import APIRouter, status
from fastapi.middleware.cors import  CORSMiddleware
#datos tortillitas
from ..DB import datos_tortillas


router = APIRouter()

@router.get(
    path="/tortillas",
    tags=["Tortillas"],
    summary="todas las tortillas papa",
    status_code=status.HTTP_200_OK
)
def tortillas():
    """
    tortillas

    la funcion tortillas nos devuelven los datos de las tortillas (KEKW)
    deben devolver el tipo de tortilla que es, que propiedas da, el id de la tortilla, y una foto de la tortilla
    """

    data = datos_tortillas.tortillas

    return data 