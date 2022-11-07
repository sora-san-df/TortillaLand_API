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
        max_length=50
    )
    foto: str 
    nombre_en_juego: str = Field(
        ...,
        min_length=1,
        max_length=20
        
        )
    integrantes_id: UUID = Field(...)
    edad: int = Field(
        ...,
        gt=1,
        lt=90
        
        )
    pais_origen: str
    pais_residencia: str

#datos mas especificos de los streamers
class Streamers(Integrantes):
    canal_twitch: str 
    media_viewers: str
    #foto perfil del canal de twitch
    canal_image: str 
    #pueblo donde vive
    pueblo: str
    casa: str
    temporada_tortilla: str 

 #personajes secundarios
class Personajes_sec(Integrantes):
    pass 

