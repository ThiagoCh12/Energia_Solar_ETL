from etl import ler_dados
from db import conectar_banco, inserir_dados, ler_dados_banco   
from dashboard import criar_dashboard

def main():
    
    caminho = "DataModel.xlsx"
    df = ler_dados(caminho)

    engine = conectar_banco()
    inserir_dados(df, engine, "energia_solar")
    df_banco = ler_dados_banco(engine, "energia_solar")
    print(df_banco.head())

    criar_dashboard(df_banco)

if __name__ == "__main__":
    main()