from app.database import SessionLocal
from app.models import Cliente

# Cria uma sessão
session = SessionLocal()

# Novo cliente (exemplo)
novo_cliente = Cliente(
    nome="João da Silva",
    cnpj_cpf="12345678901234",
    email="joao@email.com",
    endereco="Rua das Flores, 123",
    telefone="(21) 91234-5678"
)

# Insere no banco
session.add(novo_cliente)

try:
    session.commit()
    print(" Cliente inserido com sucesso!")
except Exception as e:
    session.rollback()
    print(" Erro ao inserir cliente:", e)

session.close()
