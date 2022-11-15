#Python
from uuid import UUID
#pydantic
from pydantic import BaseModel, Field
#fastapi


#datos de los integrantes 
class Integrantes(BaseModel):
    nombre_real: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example='Raul Garcia P'
    )
    foto: str = Field(default=None)
    nombre_en_juego: str = Field(
        ...,
        min_length=1,
        max_length=20,
        example="SrAuron"
        
        )
    integrantes_id: UUID = Field(
        ...,
        example="5361a11b-615c-42bf-9bdb-e2c3790ada14")
        
    edad: str = Field(...)
    pais_origen: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Andorra"
    )
    pais_residencia: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Francia"
    )

#datos mas especificos de los streamers
class Streamers(Integrantes):
    canal_twitch: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="Vegetta777"
    )
    media_viewers: str = Field(
        default=None,
        example="1000"
        )
    #foto perfil del canal de twitch
    canal_image: str = Field(...)
    #pueblo donde vive
    pueblo: str = Field(
        ...,
        example="Pueblo Verde"
        )
    casa: str = Field(default=None)
    temporada_tortilla: str  = Field(
        ...,
        example="1"
        )

 #personajes secundarios
class Personajes_sec(Integrantes):
    pass 

