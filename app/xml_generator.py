import xml.etree.ElementTree as ET
from app.models import NotaFiscal, ItemNota, Cliente, Servico
from app.database import SessionLocal
#from app.xml_generator import gerar_xml_da_nota

gerar_xml_da_nota(nota_id=1)


def gerar_xml_da_nota(nota_id: int, caminho_saida: str = "nota.xml") -> None:
    session = SessionLocal()
    try:
        nota = session.query(NotaFiscal).filter_by(id=nota_id).first()
        if not nota:
            print("❌ Nota não encontrada.")
            return

        cliente = nota.cliente
        itens = nota.itens

        root = ET.Element("notaFiscal", id=str(nota.id))
        ET.SubElement(root, "cliente").text = cliente.nome
        ET.SubElement(root, "dataEmissao").text = nota.data_emissao.isoformat()
        ET.SubElement(root, "total").text = str(nota.total)

        itens_el = ET.SubElement(root, "itens")
        for item in itens:
            servico = item.servico
            item_el = ET.SubElement(itens_el, "item")
            ET.SubElement(item_el, "descricao").text = servico.descricao
            ET.SubElement(item_el, "quantidade").text = str(item.quantidade)
            ET.SubElement(item_el, "valorUnitario").text = str(item.valor_unitario)

        tree = ET.ElementTree(root)
        tree.write(caminho_saida, encoding="utf-8", xml_declaration=True)
        print(f"✅ XML gerado em: {caminho_saida}")

    except Exception as e:
        print("❌ Erro ao gerar XML:", e)

    finally:
        session.close()




