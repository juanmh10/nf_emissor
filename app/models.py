from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime
from app.database import Base 
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    cnpj_cpf = Column(String(14), unique=True, nullable=False)
    telefone = Column(String(20), nullable=False)  

 
class Servico(Base):
    __tablename__ = 'servicos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(Text, nullable=False)
    preco_unitario = Column(Numeric(10, 2), nullable=False)
    codigo_tributo = Column(String(10), nullable=False)



class NotaFiscal(Base):
    __tablename__ = 'notas_fiscais'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    data_emissao = Column(DateTime, default=datetime.utcnow)
    total = Column(Numeric(10, 2), nullable=False)

    cliente = relationship("Cliente", backref="notas")
    itens = relationship("ItemNota", back_populates="nota")



class ItemNota(Base):
    __tablename__ = 'itens_nota'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nota_id = Column(Integer, ForeignKey('notas_fiscais.id'), nullable=False)
    servico_id = Column(Integer, ForeignKey('servicos.id'), nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Numeric(10, 2), nullable=False)

    nota = relationship("NotaFiscal", back_populates="itens")
    servico = relationship("Servico", backref="itens")

