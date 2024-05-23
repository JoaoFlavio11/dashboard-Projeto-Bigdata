import os
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_icon=":bar_chart:", page_title="Gerenciamento de Estoque")

# Obter o caminho absoluto do diretório do script atual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Defina o caminho relativo para o diretório onde os arquivos CSV estão localizados
data_directory = os.path.join(current_dir, "..", "..", "data")

# Lista com os nomes dos arquivos CSV
file_list = ["dim_fornecedor.csv", "dim_local.csv", "dim_produto.csv", "dim_tempo.csv", "fato_financas.csv"]

# Lista para armazenar os DataFrames
df_list = []

# Iterar sobre a lista de arquivos e ler cada um com a codificação apropriada
for file in file_list:
    file_path = os.path.join(data_directory, file)
    try:
        df = pd.read_csv(file_path, sep=";", decimal=".", encoding='latin1')  # Use 'latin1' ou 'iso-8859-1'
        df_list.append(df)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {file_path}")

# Layout da página
cols = st.columns(3)  # Três colunas para distribuir as tabelas

# Exibir os primeiros registros de cada DataFrame com o nome do arquivo em colunas
for i, (file, df) in enumerate(zip(file_list, df_list)):
    col = cols[i % 3]  # Alternar entre as colunas
    col.markdown(f"## Tabela: {file}")
    col.write(df.head())
