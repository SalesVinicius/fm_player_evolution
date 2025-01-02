# %%
import pandas as pd
import sqlalchemy
import os
import pandas as pd
import shutil
from io import StringIO
import pytesseract
from PIL import Image
import cv2

# # %%
# engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

# #Path Files
# src_path = os.path.dirname(os.path.abspath(__file__))
# base_path = os.path.dirname(src_path)
# data_path = os.path.join(base_path, "data")
# genie_scout_path = os.path.join(data_path, "genie_scout")
# raw_data_path = os.path.join(genie_scout_path, "01_raw_data")
# cleaned_data_path = os.path.join(genie_scout_path, "02_cleaned_data")
# ingested_path = os.path.join(genie_scout_path, "03_ingested")
# for arquivo in os.listdir(raw_data_path):

#     if arquivo.endswith(".csv"):  # Filtrar apenas arquivos CSV
#         caminho_entrada = os.path.join(raw_data_path, arquivo)
#         caminho_saida = os.path.join(ingested_path, arquivo)
    
#     nome_sem_extensao = arquivo.rsplit('.', 1)[0]
#     df = pd.read_csv(caminho_entrada, sep=';', encoding='ISO-8859-1')
#     df['dt_Game'] = nome_sem_extensao
#     df.to_sql('tb_Juventude',engine,if_exists="replace",index="False")

#     shutil.move(caminho_entrada, caminho_saida)



# %%
# Defina o caminho do executável do tesseract (caso não esteja no PATH)
# Se necessário, descomente a linha abaixo e defina o caminho correto
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Carregar a imagem em escala de cinza
imagem = cv2.imread('caminho_para_imagem.png', cv2.IMREAD_GRAYSCALE)

# Aplicar um filtro de threshold para melhorar o contraste
_, imagem_binaria = cv2.threshold(imagem, 150, 255, cv2.THRESH_BINARY)

dados = fr'C:\Users\T-GAMER\Documents\DS\vbola\Projetos\fm_player_evolution\data\fmrte\2025-02-1 S20.jpg'
# Carregue a imagem
imagem = Image.open(dados)

# Use o pytesseract para extrair texto da imagem
texto_extraido = pytesseract.image_to_string(imagem)

# Exibir o texto extraído para verificar a qualidade do OCR
print(texto_extraido)
# %%
linhas = texto_extraido.split('\n')
dados = [linha.split() for linha in linhas if linha.strip()]  # Ignora linhas vazias

# Crie o DataFrame
df = pd.DataFrame(dados[1:], columns=dados[0])  # Usa a primeira linha como cabeçalho

# Exiba o DataFrame
print(df)
# %%
dados = fr'C:\Users\T-GAMER\Documents\DS\vbola\Projetos\fm_player_evolution\data\fmrte\2025-02-1 S20.jpg'
# Carregar a imagem em escala de cinza
imagem = cv2.imread(dados, cv2.IMREAD_GRAYSCALE)

# Aplicar um filtro de threshold para melhorar o contraste
_, imagem_binaria = cv2.threshold(imagem, 150, 255, cv2.THRESH_BINARY)

# Usar o pytesseract para extrair texto da imagem processada
texto_extraido = pytesseract.image_to_string(imagem_binaria)
print(texto_extraido)
# %%
