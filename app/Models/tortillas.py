#python
from uuid import UUID
#pydantic
from pydantic import BaseModel
#fastapi

#datos de las tortillas
class Tortillas(BaseModel):
    tipo: str
    propiedades: str
    tortilla_id: UUID
    foto_tortilla: str 

#Ingredientes de tortillas
class Ingredientes(Tortillas):
    foto_ingredientes: str 
