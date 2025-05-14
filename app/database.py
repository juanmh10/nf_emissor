from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

Base = declarative_base()
# variaveis do ambiente .env
load_dotenv()


#ler variaveis
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#cria conexao
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


#CRIA ENGINE SQLAHEMY
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

# Testa a conexão
for attempt in range(3):
    try:
        with engine.connect() as connection:
            print("Conexão bem-sucedida!")
            break
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        if attempt < 2:
            print("Tentando novamente...")
        else:
            print("Falha ao conectar ao banco de dados após 3 tentativas.")
            break
        