import chardet

# Descobrindo qual é encoding do documento.  
# Ler arquivo em modo binário
with open('./data/genie_scout/2025-02-01.csv', 'rb') as f:
    resultado = chardet.detect(f.read())

print(resultado['encoding'])