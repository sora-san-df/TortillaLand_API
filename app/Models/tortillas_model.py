#python
from uuid import UUID
from typing import List
#pydantic
from pydantic import BaseModel, Field
#fastapi

#datos de las tortillas
class Tortillas(BaseModel):
    tipo: str = Field(
        ...,
        example="tortilla de pimiento")
    propiedades: List[str] = Field(
        ...,
        example="resistencia al fuego, velocidad")
    tortilla_id: UUID = Field(...)
    foto_tortilla: str  = Field(default=None)

#Ingredientes de tortillas
class Ingredientes(Tortillas):
    foto_ingredientes: List[str] = Field(...)
