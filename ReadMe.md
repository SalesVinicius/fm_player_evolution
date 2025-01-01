# FM24 Player Evolution

Este projeto tem como objetivo acompanhar a evolução dos jogadores da base do Juventude no Football Manager 2024.

## Objetivo

O principal objetivo é monitorar a evolução dos jogadores da base do clube utilizando o Genie Scout para obter os seguintes valores:

- **Habilidade Atual (CA)**
- **Habilidade Potencial (PA)**

Esses dados serão analisados periodicamente para entender o desenvolvimento dos atletas ao longo do tempo.

## Ferramentas Utilizadas

- **Football Manager 2024**: Plataforma base para gerenciamento dos jogadores.
- **Genie Scout**: Ferramenta para extração e análise dos dados dos jogadores.
- **Python**: Para processamento, visualização e análise dos dados coletados.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Matplotlib/Seaborn**: Visualização de dados.

## Estrutura do Projeto

1. **Coleta de Dados**:
   - Exportação periódica dos relatórios do Genie Scout.
   - Armazenamento dos dados em formatos como CSV ou Excel.

2. **Processamento de Dados**:
   - Limpeza e organização dos dados exportados.
   - Cálculos de médias, desvios e evolução.

3. **Visualização**:
   - Gráficos de evolução de CA e PA ao longo do tempo.
   - Comparativos entre jogadores e categorias.

4. **Relatórios**:
   - Geração de relatórios periódicos sobre o progresso dos jogadores.

## Melhorias Futuras

- Implementação de Machine Learning para prever a evolução dos jogadores.
- Integração com bases de dados externas para benchmarking.
- Desenvolvimento de uma interface web para visualização dos relatórios.
