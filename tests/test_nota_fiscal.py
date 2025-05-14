import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services import criar_nota
from decimal import Decimal

def test_criar_nota():
    cliente_id = 1 
    itens = [
        {"servico_id": 1, "quantidade": 1, "valor_unitario": Decimal("250.00")},
        {"servico_id": 2, "quantidade": 2, "valor_unitario": Decimal("100.00")},
    ]

    try:
        criar_nota(cliente_id, itens)
    except Exception:
        assert False, "Erro ao criar nota fiscal"
