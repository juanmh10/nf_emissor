import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import xml.etree.ElementTree as ET
from app.xml_generator import gerar_xml_da_nota # type: ignore
from decimal import Decimal

def test_gerar_xml_valido():
    # Gera a nota no banco
    nota_id = 1  
    caminho_xml = f"tests/nota_{nota_id}.xml"

    # Gera o XML da nota
    gerar_xml_da_nota(nota_id, caminho_saida=caminho_xml)

    # Verifica se o arquivo foi criado
    assert os.path.exists(caminho_xml)

    # Lê e valida o conteúdo do XML
    tree = ET.parse(caminho_xml)
    root = tree.getroot()

    assert root.tag == "notaFiscal"
    assert root.attrib["id"] == str(nota_id)

    cliente = root.find("cliente")
    total = root.find("total")
    itens = root.find("itens")

    assert cliente is not None and len(cliente.text) > 0
    assert total is not None and float(total.text) > 0
    assert itens is not None and len(itens) > 0
 
    os.remove(caminho_xml)
