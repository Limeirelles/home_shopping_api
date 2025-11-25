from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

# Esta é a classe base do SQLAlchemy.
# Todas as nossas tabelas vão herdar dela.
# Define qual será o nome real da tabela lá no Postgres.
Base = declarative_base()

class CategoriaModel(Base):
    __tablename__ = 'categorias' 

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False, unique=True)
    
    # Relacionamento: Uma categoria pode ter vários produtos
    produtos = relationship("ProdutoModel", back_populates="categoria")

class ProdutoModel(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    marca = Column(String(50), nullable=True)
    
    # Chave Estrangeira: Todo produto pertence a uma categoria
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    
    # Relacionamentos
    categoria = relationship("CategoriaModel", back_populates="produtos")
    itens = relationship("ItemCompraModel", back_populates="produto")

class CompraModel(Base):
    __tablename__ = 'compras'

    id = Column(Integer, primary_key=True, autoincrement=True)
    # default=datetime.now garante que se não passarmos data, ele pega a de agora
    data_compra = Column(DateTime, default=datetime.now, nullable=False)
    local = Column(String(100), nullable=False) # Ex: Supermercado X
    forma_pagamento = Column(String(50)) # Ex: Crédito, Débito
    observacoes = Column(String(200), nullable=True)

    # Relacionamento: Uma compra tem vários itens
    itens = relationship("ItemCompraModel", back_populates="compra")

class ItemCompraModel(Base):
    __tablename__ = 'itens_compra'

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # As duas chaves que amarram tudo
    compra_id = Column(Integer, ForeignKey('compras.id'), nullable=False)
    produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    
    quantidade = Column(Float, nullable=False) # Float permite 1.5 kg, por exemplo
    preco_unitario = Column(Float, nullable=False)
    
    # Relacionamentos para facilitar o acesso aos dados
    compra = relationship("CompraModel", back_populates="itens")
    produto = relationship("ProdutoModel", back_populates="itens")