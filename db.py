from sqlalchemy import create_engine
import pandas as pd

def conectar_banco():
    
    url = "postgresql://postgres:123@localhost:5432/etl_db" # substitua pelos seus dados
    engine = create_engine(url)
    print("Conexão com o banco de dados estabelecida.")
    return engine

def inserir_dados(df: pd.DataFrame, engine, tabela: str):
    df.to_sql(tabela, engine, if_exists='replace', index=False)
    print(f"Dados inseridos com sucesso.")


def ler_dados_banco(engine, tabela: str) -> pd.DataFrame:
    
    return pd.read_sql(f"SELECT * FROM {tabela}", engine)