#python 
from typing import List
#pydantic 
from pydantic import BaseModel
 

class Pueblos(BaseModel):
    color: str 
    construcciones: List[str] #no tengo claro aun las construcciones emblematicas la vdd

