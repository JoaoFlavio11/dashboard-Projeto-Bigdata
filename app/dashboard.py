import os
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_icon=":bar_chart:", page_title="Gerenciamento de Estoque")

# Obter o caminho absoluto do diretório do script atual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Defina o caminho relativo para o diretório onde os arquivos CSV estão localizados
data_directory = os.path.join(current_dir, "..", "data")

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

# Atribuir DataFrames a variáveis específicas para fácil acesso
df_fornecedor = df_list[0]
df_local = df_list[1]
df_produto = df_list[2]
df_tempo = df_list[3]
df_financas = df_list[4]

# Unir DataFrames para análises e gráficos
df_financas_tempo = pd.merge(df_financas, df_tempo, on="cod_movimentacao")
df_financas_produto = pd.merge(df_financas, df_produto, on="cod_produto")
df_financas_local = pd.merge(df_financas, df_local, on="cod_armazem")
df_financas_fornecedor = pd.merge(df_financas, df_fornecedor, on="cod_fornecedor")

# Gráficos

# Gráfico de barras: Valor de entrada e saída por produto
fig_produto = px.bar(df_financas_produto, x="descricao", y=["valor_entrada", "valor_saida"], 
title="Valor de Entrada e Saída por Produto", labels={"descricao": "Produto", "value": "Valor (R$)"})

# Gráfico de barras: Valor de entrada e saída por armazém
fig_local = px.bar(df_financas_local, x="cidade", y=["valor_entrada", "valor_saida"],
title="Valor de Entrada e Saída por Armazém", labels={"cidade": "Cidade", "value": "Valor (R$)"})

# Gráfico de barras: Valor de entrada e saída por fornecedor
fig_fornecedor = px.bar(df_financas_fornecedor, x="nome_contato", y=["valor_entrada", "valor_saida"],
title="Valor de Entrada e Saída por Fornecedor", labels={"nome_contato": "Fornecedor", "value": "Valor (R$)"})

# Gráfico de linha: Valor de entrada e saída ao longo do tempo
fig_tempo = px.line(df_financas_tempo, x="dia", y=["valor_entrada", "valor_saida"], color="mes",
title="Valor de Entrada e Saída ao Longo do Tempo", labels={"dia": "Dia", "value": "Valor (R$)", "mes": "Mês"})

# Layout da página
st.write("## Gráficos de Gerenciamento de Estoque")

# Exibir gráficos
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

col1.plotly_chart(fig_produto, use_container_width=True)
col2.plotly_chart(fig_local, use_container_width=True)
col3.plotly_chart(fig_fornecedor, use_container_width=True)
col4.plotly_chart(fig_tempo, use_container_width=True)
