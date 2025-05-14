from app.services import criar_nota
from decimal import Decimal

cliente_id = 1

itens = [
    {"servico_id": 1, "quantidade": 1, "valor_unitario": Decimal("250.00")},
    {"servico_id": 2, "quantidade": 1, "valor_unitario": Decimal("450.00")},
]

criar_nota(cliente_id, itens)
