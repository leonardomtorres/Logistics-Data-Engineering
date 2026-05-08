import pandas as pd
from sqlalchemy import create_engine
import unicodedata
import csv

print("Iniciando extração...")


# EXTRAÇÃO


df = pd.read_csv(
    "data/raw/amazon_delivery.csv",
    encoding="latin1",
    on_bad_lines="skip"
)

print("Transformando dados...")


# TRANSFORMAÇÃO


df.drop_duplicates(inplace=True)

df.columns = [c.strip().replace(" ", "_") for c in df.columns]

if "Order_Date" in df.columns:
    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"],
        errors="coerce"
    )

df["lucro"] = 10.0


# LIMPEZA TEXTO


for col in df.select_dtypes(include=["object", "string"]).columns:

    df[col] = df[col].astype(str)

    df[col] = df[col].apply(
        lambda x: unicodedata.normalize("NFKD", str(x))
        .encode("ascii", errors="ignore")
        .decode("utf-8")
        .strip()
    )


# REMOVE NULOS


for col in df.select_dtypes(include=["object", "string"]).columns:
    df[col] = df[col].fillna("")

for col in df.select_dtypes(include=["float64", "int64"]).columns:
    df[col] = df[col].fillna(0)


# SALVA CSV


csv_path = "data/processed/dados_tratados.csv"

df.to_csv(
    csv_path,
    index=False,
    encoding="utf-8",
    quoting=csv.QUOTE_MINIMAL
)

print("CSV tratado salvo.")


# POSTGRESQL


print("Enviando para PostgreSQL...")

engine = create_engine(
    "postgresql+psycopg2://etl_user:etl123@127.0.0.1:5432/logistics"
)


# CARGA


try:

    df.to_sql(
        "fato_entrega",
        engine,
        if_exists="replace",
        index=False,
        chunksize=1000
    )

    print("===================================")
    print("ETL CONCLUÍDA COM SUCESSO")
    print("===================================")

except Exception as e:

    print("===================================")
    print("ERRO AO ENVIAR:")
    print(repr(e))
    print("===================================")
