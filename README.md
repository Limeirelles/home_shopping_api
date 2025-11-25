# Home Shopping API 🛒

API RESTful desenvolvida para gerenciamento e controle de compras domésticas, migrando uma planilha complexa para um sistema robusto de banco de dados.


## 🚀 Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI:** Framework moderno e de alta performance para construção de APIs.
- **SQLAlchemy:** ORM para manipulação de banco de dados.
- **Alembic:** Gerenciamento de migrações de banco de dados (Versionamento de Schema).
- **Pydantic:** Validação de dados e serialização robusta.
- **PostgreSQL:** Banco de dados relacional.
- **Docker & Docker Compose:** Containerização do ambiente de banco de dados.

## ⚙️ Funcionalidades Implementadas (Até o momento)

- [x] Estrutura de pastas escalável.
- [x] Configuração de ambiente com Docker (Banco de Dados).
- [x] Migrações automáticas com Alembic.
- [x] Modelagem de dados (Categorias, Produtos, Compras, Itens).
- [x] CRUD de Categorias (Create & Read).
- [x] Validação de Schemas de entrada e saída.

## 🔧 Como Rodar o Projeto

1. Clone o repositório:
```bash
git clone [https://github.com/SEU_USUARIO/home_shopping_api.git](https://github.com/SEU_USUARIO/home_shopping_api.git)

2. Configure o ambiente virtual:
```bash 
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

3. Suba o banco de dados com Docker:
```bash 
docker compose up -d

4. Execute as migrações:
```bash
alembic upgrade head

5. Rode a API:
```bash
uvicorn meu_projeto_api.main:app --reload

📄 Documentação
Acesse a documentação interativa (Swagger UI) em: http://localhost:8000/docs