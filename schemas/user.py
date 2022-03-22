import imp
from pydantic import BaseModel
from typing import Optional

#definiendo tipos de datos a insertar en la bdd
class User(BaseModel):
    id:Optional[str]
    nombre: str
    correo: str
    contrasena: str