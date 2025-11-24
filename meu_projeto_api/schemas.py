from pydantic import BaseModel, Field
from typing import Annotated

# Schema base para configurações comuns
class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid' # Não permite campos extras no request
        from_attributes = True # Permite mapear de modelos de banco de dados

# Schema para a nossa Categoria
class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria', example='Mercearia', max_length=20)]