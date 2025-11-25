from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# A mesma URL que você colocou no alembic.ini
# (Lembre-se de conferir se a senha/user/db estão iguais aos seus)
DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost:5432/home_shopping_db"

# O 'engine' é o motor que abre a conexão real com o banco
engine = create_engine(DATABASE_URL)

# O 'SessionLocal' é a fábrica de sessões. 
# Cada requisição vai pedir uma sessão para essa fábrica.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Esta função é a mágica da Injeção de Dependência
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()