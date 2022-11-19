#fastAPI
from fastapi import APIRouter,status
from fastapi.middleware.cors import  CORSMiddleware
#Datos integrantes 
from ..DB import datos_integrantes


router = APIRouter()


@router.get(
    path="/integrantes/canales_twitch",
    status_code=status.HTTP_200_OK,
    tags=["canales_de_twitch"],
    summary="Canales dde twitch de los integgrantes"
)

def canales_twitch():
    """
    canales_twitch

    La funcion muestra la info sobre los canales de twitch de los participantes, retornara info como por ejemplo 
    el canal de twitch, la imagen del canal, media de viewers, pueblo al que pertenece, temporada de tortila y como parametro opcional la casa
    
    Parametros:
        - None
    Returns:
    retorna los datos de los canales de twitch de cada integrantes a su vez del pueblo y temporada el que se encuentra. 
    """
    data = datos_integrantes.canales

    return data
