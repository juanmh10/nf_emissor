from app.database import SessionLocal
from app.models import Cliente, Servico

def inserir_dados_base():
    session = SessionLocal()
    cliente = Cliente(
        nome="Cliente Teste",
        endereco="Rua Teste",
        email="teste@email.com",
        cnpj_cpf="12345678901234",
        telefone="(00) 90000-0000"
    )
    servico1 = Servico(
        descricao="Serviço A",
        preco_unitario=250.00,
        codigo_tributo="1001"
    )
    servico2 = Servico(
        descricao="Serviço B",
        preco_unitario=100.00,
        codigo_tributo="1002"
    )
    session.add_all([cliente, servico1, servico2])
    session.commit()
    session.close()
