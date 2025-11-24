from fastapi import FastAPI , Body
from meu_projeto_api.schemas import Categoria
from typing import Annotated

app = FastAPI(title='Minha API de Compras')

# Nosso endpoint "Olá, Mundo!" que já existia
@app.get('/')
def read_root():
    return {'message': 'API de Compras rodando!'}


# --- NOVO CÓDIGO ABAIXO ---

@app.post('/categorias')
async def create_categoria(
    categoria: Annotated[Categoria, Body(embed=True)]
):
    # Por enquanto, vamos apenas retornar a categoria recebida
    # para confirmar que a validação funcionou.
    return categoria