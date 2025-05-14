from app.database import SessionLocal
from app.models import NotaFiscal, ItemNota
from datetime import datetime
from decimal import Decimal

# Cria a sessão
session = SessionLocal()

# Dados simulados (IDs já existentes no banco)
cliente_id = 1
servico1_id = 1
servico2_id = 2

# Preços simulados (devem estar compatíveis com o banco)
preco1 = Decimal("250.00")
preco2 = Decimal("450.00")

# Cria a nota fiscal (total somado dos serviços)
nova_nota = NotaFiscal(
    cliente_id=cliente_id,
    data_emissao=datetime.utcnow(),
    total=preco1 + preco2
)

# Adiciona ao banco (ainda sem commit)
session.add(nova_nota)
session.flush()  # Garante que nova_nota.id esteja disponível

# Cria os itens da nota
item1 = ItemNota(
    nota_id=nova_nota.id,
    servico_id=servico1_id,
    quantidade=1,
    valor_unitario=preco1
)

item2 = ItemNota(
    nota_id=nova_nota.id,
    servico_id=servico2_id,
    quantidade=1,
    valor_unitario=preco2
)

# Adiciona os itens
session.add_all([item1, item2])

# Commit e encerramento
try:
    session.commit()
    print("✅ Nota fiscal e itens inseridos com sucesso!")
except Exception as e:
    session.rollback()
    print("❌ Erro ao inserir nota fiscal:", e)

session.close()
