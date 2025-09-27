import pandas as pd

def ler_dados(caminho_arquivo: str) -> pd.DataFrame:

    df = pd.read_excel(caminho_arquivo)
    df['data'] = pd.to_datetime(df['data']).dt.date
    df = df.dropna(how='all')
    df = df.fillna("N/A")
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    return df

