import os
import streamlit as st
import pandas as pd
import plotly.express as px

#configurando a pãgina do streamlit
st.set_page_config(
    layout="wide",
    page_icon=":bar_chart:", 
    page_title="Gerenciamento de Estoque"
)

#caminho do diretório do código
current_dir = os.path.dirname(os.path.abspath(__file__))

#caminho relativo para a pasta onde os .CSV estão "data"
data_directory = os.path.join(current_dir, "..", "data")

#lista dos arquivos CSV
file_list = ["dim_fornecedor.csv", "dim_local.csv", "dim_produto.csv", "dim_tempo.csv", "fato_financas.csv"]

# Lista dos DataFrames
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

#juntar os DataFrames (tabela fato + tabelas de dimesão) para análises e gráficos
df_financas_tempo = pd.merge(df_financas, df_tempo, on="cod_movimentacao")
df_financas_produto = pd.merge(df_financas, df_produto, on="cod_produto")
df_financas_local = pd.merge(df_financas, df_local, on="cod_armazem")
df_financas_fornecedor = pd.merge(df_financas, df_fornecedor, on="cod_fornecedor")

#filtros na sidebar
st.sidebar.subheader("Filtros")

#filtrar por produto
selected_produto = st.sidebar.multiselect(
    "Selecione o(s) produto(s) para remover",
    df_produto['descricao'].unique()
)

#filtrar por armazém
selected_armazem = st.sidebar.multiselect(
    "Selecione o(s) armazém(ns) para remover",
    df_local['cidade'].unique()
)

#filtrar por fornecedor
selected_fornecedor = st.sidebar.multiselect(
    "Selecione o(s) fornecedor(es) para remover",
    df_fornecedor['nome_contato'].unique()
)

#filtrar por mês
selected_mes = st.sidebar.multiselect(
    "Selecione o(s) mês(es) para remover",
    df_tempo['mes'].unique()
)

#aplicar filtros
filtered_df_produto = df_financas_produto[~df_financas_produto['descricao'].isin(selected_produto)]
filtered_df_local = df_financas_local[~df_financas_local['cidade'].isin(selected_armazem)]
filtered_df_fornecedor = df_financas_fornecedor[~df_financas_fornecedor['nome_contato'].isin(selected_fornecedor)]
filtered_df_tempo = df_financas_tempo[~df_financas_tempo['mes'].isin(selected_mes)]

#seção dos gráficos

#Gráfico: Valor de entrada e saída por produto
fig_produto = px.bar(
    filtered_df_produto,
    x="descricao", 
    y=["valor_entrada", "valor_saida"], 
    labels={"descricao": "Produto", "value": "Valor (R$)"}
)

#Gráfico: Valor de entrada e saída por armazém
fig_local = px.bar(
    filtered_df_local, 
    x="cidade", 
    y=["valor_entrada", "valor_saida"],
    labels={"cidade": "Cidade", "value": "Valor (R$)"}
)

#Gráfico de barras: Valor de entrada e saída por fornecedor
fig_fornecedor = px.bar(
    filtered_df_fornecedor, 
    x="nome_contato", 
    y=["valor_entrada", "valor_saida"],
    labels={"nome_contato": "Fornecedor", "value": "Valor (R$)"}
)

#Gráfico de linha: Valor de entrada e saída ao longo do tempo
fig_tempo = px.line(
    filtered_df_tempo,
    x="dia",
    y=["valor_entrada", "valor_saida"], 
    color="mes", 
    labels={"dia": "Dia", "value": "Valor (R$)", "mes": "Mês"}
)

#layout da página
st.title("Gráficos de Gerenciamento de Estoque")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Exibir gráficos
col1.markdown("### Valor de Entrada e Saída por Produto")
col1.plotly_chart(fig_produto, use_container_width=True)

col2.markdown("### Valor de Entrada e Saída por Armazém")
col2.plotly_chart(fig_local, use_container_width=True)

col3.markdown("### Valor de Entrada e Saída por Fornecedor")
col3.plotly_chart(fig_fornecedor, use_container_width=True)

col4.markdown("### Valor de Entrada e Saída ao Longo do Tempo")
col4.plotly_chart(fig_tempo, use_container_width=True)
