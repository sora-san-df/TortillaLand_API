#Python 
#Pydantic
#fastAPI
from fastapi import APIRouter,status
from fastapi.middleware.cors import  CORSMiddleware
#datos integrantes
from ..DB import datos_integrantes



router = APIRouter()
#accepted origins for the CORS 
origins: list = [
    "*"
]

router.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@router.get(
    path="/integrantes",
    status_code=status.HTTP_200_OK,
    tags=["integrantes"],
    summary="Mostrar los intengrates de tortilla"
)
def integrantes(): 
    """
    integrantes 

    La funcion integrantes nos devuelve lso datos basicos de los integrantes de tortillaland, como nombre, edad, pais de residencia,
    pais donde vive actualmente, etc. El modelo Streamer tiene datos mas especficos de sus canales de twitch

    Params:
     - None

    Returns: 
    Un json con los datos de los integrantes.
    """
    data = datos_integrantes.db
    return   data