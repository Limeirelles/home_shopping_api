from fastapi import FastAPI, Body, Depends
from sqlalchemy.orm import Session # <--- Importante para tipagem
from meu_projeto_api.schemas import Categoria
from meu_projeto_api.models import CategoriaModel # <--- Nosso modelo do banco
from meu_projeto_api.database import get_db # <--- Nossa nova função de conexão
from typing import Annotated

app = FastAPI(title='Minha API de Compras')

@app.get('/')
def read_root():
    return {'message': 'API de Compras rodando!'}

@app.post('/categorias')
async def create_categoria(
    categoria: Annotated[Categoria, Body(embed=True)],
    db: Session = Depends(get_db) # <--- AQUI ACONTECE A MÁGICA
):
    # 1. Criamos o objeto do banco (Model) com os dados recebidos do schema
    novo_registro = CategoriaModel(nome=categoria.nome)
    
    # 2. Adicionamos na "cesta" da sessão
    db.add(novo_registro)
    
    # 3. Confirmamos a transação (efetiva no banco)
    db.commit()
    
    # 4. Atualizamos o objeto com o ID que o banco gerou
    db.refresh(novo_registro)
    
    # 5. Retornamos o objeto salvo
    return novo_registro

# para ir sempre ao Swagger(/docs), usar no terminal o comando: uvicorn meu_projeto_api.main:app --reload
