import os
import streamlit as st
import pandas as pd

#configurando a pãgina do streamlit
st.set_page_config(
    layout="wide",
    page_icon=":bar_chart:", 
    page_title="Tabelas do Estoque"
)

#caminho do diretório do código
current_dir = os.path.dirname(os.path.abspath(__file__))

#caminho relativo para a pasta onde os .CSV estão "data"
data_directory = os.path.join(current_dir, "..", "..", "data")

#listados arquivos CSV
file_list = ["dim_fornecedor.csv", "dim_local.csv", "dim_produto.csv", "dim_tempo.csv", "fato_financas.csv"]

#lista dos DataFrames
df_list = []

#varrer a lista de arqiovos para ler cada arquivo
for file in file_list:
    file_path = os.path.join(data_directory, file)
    try:
        df = pd.read_csv(file_path, sep=";", decimal=".", encoding='latin1')
        df_list.append(df)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {file_path}")

#atribuir DataFrames a variáveis específicas para fácil acesso
df_fornecedor = df_list[0]
df_local = df_list[1]
df_produto = df_list[2]
df_tempo = df_list[3]
df_financas = df_list[4]

#unir DataFrames (tabela fato + tabelas de dimensão) para análises 
df_financas_produto = pd.merge(df_financas, df_produto, on="cod_produto")
df_financas_local = pd.merge(df_financas, df_local, on="cod_armazem")

#layout da página
st.title("Tabelas de Gerenciamento de Estoque")
cols = st.columns(3)  #3 colunas para distribuir as tabelas

#mostrar os primeiros registros de cada DataFrame com o nome do arquivo em colunas
for i, (file, df) in enumerate(zip(file_list, df_list)):
    col = cols[i % 3]  # Alternar entre as colunas
    col.markdown(f"### Tabela: {file}")
    col.write(df.head())

