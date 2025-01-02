# %%
import pandas as pd
import sqlalchemy
import os
import pandas as pd
import shutil
from datetime import datetime


engine = sqlalchemy.create_engine("sqlite:///../data/database.db")
hoje = datetime.today().strftime('%Y-%m-%d')
#Path Files
src_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.dirname(src_path)
data_path = os.path.join(base_path, "data")
fmrte_path = os.path.join(data_path, "fmrte")
raw_data_path = os.path.join(fmrte_path, "01_raw_data")
cleaned_data_path = os.path.join(fmrte_path, "02_cleaned_data")
ingested_path = os.path.join(fmrte_path, "03_ingested")

for arquivo in os.listdir(raw_data_path):
    if arquivo.endswith(".txt"):  # Filtrar apenas arquivos CSV
        caminho_entrada = os.path.join(raw_data_path, arquivo)
        pass
        
# Carregar o arquivo .txt com espaços como delimitador
    df = pd.read_csv(caminho_entrada, delimiter='\t')

# Salvar como .csv
    data_game = input('Data no jogo')
    df['dt_Game'] = data_game
    df['dt_ingestao'] = hoje
    df.to_sql('tb_BaseJuventude',engine,if_exists="replace",index="False")
    
    elenco = input('P -> Profissional. R-> Reserva. S ->Sub20')
    caminho_saida = os.path.join(ingested_path, data_game) + elenco + ".csv"
    df.to_csv(caminho_saida, index=False,sep=';')



# %%
