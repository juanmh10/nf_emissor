from app.database import SessionLocal
from app.models import NotaFiscal, ItemNota
from datetime import datetime
from decimal import Decimal



#Criar nota
def criar_nota(cliente_id:int, itens: list[dict]) -> None:
    session = SessionLocal()
    try:
        #Somando as notas
        total = sum(item["valor_unitario"] * item["quantidade"] for item in itens)


        #criando notas
        nota_nova = NotaFiscal(
            cliente_id = cliente_id,
            data_emissao = datetime.utcnow(),
            total=total
        )

        session.add(nota_nova)
        session.flush()

        for item in itens:
            novo_item = ItemNota(
                nota_id = nota_nova.id,
                servico_id = item["servico_id"],
                quantidade = item["quantidade"],
                valor_unitario = item["valor_unitario"]
            )
            session.add(novo_item)

        session.commit()
        print(f"Nota criada com sucesso!")
    
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar a nota:", e)
    

    finally:
        session.close()
