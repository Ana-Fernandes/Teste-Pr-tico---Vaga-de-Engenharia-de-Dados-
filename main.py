import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from datetime import datetime

# Carregar variáveis do .env
load_dotenv()

API_KEY = os.getenv('API_KEY')
CITY = os.getenv('CITY')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Coleta da API
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# Tratamento
df = pd.DataFrame([{
    "cidade": data["name"],
    "temperatura": data["main"]["temp"],
    "umidade": data["main"]["humidity"],
    "descricao": data["weather"][0]["description"],
    "velocidade_vento": data["wind"]["speed"],
    "data_coleta": datetime.fromtimestamp(data["dt"])
}])

print(df)

# Conexão com PostgreSQL
conn_str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(conn_str)

# Salvar no banco
df.to_sql("clima_atual", engine, if_exists="append", index=False)
print("Dados salvos com sucesso no banco de dados.")
