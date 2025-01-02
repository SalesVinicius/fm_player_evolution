
import chardet
import os
import csv
import unicodedata
import re
import pandas as pd


#Path Files
src_path = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.dirname(src_path)
data_path = os.path.join(base_path, "data")
genie_scout_path = os.path.join(data_path, "genie_scout")
raw_data_path = os.path.join(genie_scout_path, "01_raw_data")
cleaned_data_path = os.path.join(genie_scout_path, "02_cleaned_data")
ingested_path = os.path.join(genie_scout_path, "03_ingested")

def normalizar_texto(texto):
    if texto is None:
        return ""
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    texto_limpo = re.sub(r'[^\x00-\x7F]+', '', texto_normalizado)  # Remove caracteres não-ASCII
    return texto_limpo


for arquivo in os.listdir(raw_data_path):
    # Descobrindo qual é encoding do documento.  
    # Ler arquivo em modo binário
    
    if arquivo.endswith(".csv"):  # Filtrar apenas arquivos CSV
        caminho_entrada = os.path.join(raw_data_path, arquivo)
        caminho_saida = os.path.join(cleaned_data_path, arquivo)
    
    with open(caminho_entrada, 'rb') as f:
        resultado = chardet.detect(f.read())

    print(f'Encoding do arquivo em: {resultado["encoding"]}')

    with open(caminho_entrada, 'r', encoding=resultado["encoding"]) as entrada, \
            open(caminho_saida, 'w', encoding=resultado["encoding"], newline='') as saida:
        
        leitor = csv.reader(entrada)
        escritor = csv.writer(saida)
        
        # Processar cada linha do CSV
        for linha in leitor:
            linha_normalizada = [normalizar_texto(campo) for campo in linha]
            escritor.writerow(linha_normalizada)
    
    os.remove(caminho_entrada)

    print(f"Arquivo '{arquivo}' processado e salvo em '{cleaned_data_path}'.")


