import os
import streamlit as st
import pandas as pd

#configurando a pãgina do streamlit
st.set_page_config(
    layout="wide",
    page_icon=":bar_chart:", 
    page_title="Tabelas Filtradas do Estoque"
)

#caminho do diretório do código
current_dir = os.path.dirname(os.path.abspath(__file__))

#caminho relativo para a pasta onde os .CSV estão "data"
data_directory = os.path.join(current_dir, "..", "..", "data")

#lista dos arquivos CSV
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

#juntar os DataFrames (tabela fato + tabelas de dimesão) para análises e gráficos
df_financas_produto = pd.merge(df_financas, df_produto, on="cod_produto")
df_financas_local = pd.merge(df_financas, df_local, on="cod_armazem")

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

#aplicar filtros
filtered_df_produto = df_financas_produto[~df_financas_produto['descricao'].isin(selected_produto)]
filtered_df_local = df_financas_local[~df_financas_local['cidade'].isin(selected_armazem)]

#layout da página
st.title("Dados Filtrados")
col1, col2 = st.columns(2)

#tabela de produtos filtrados
with col1:
    st.markdown("## Aplique o filtro na tabela: Produtos")
    if filtered_df_produto.empty:
        st.markdown("### Nenhum produto selecionado para remoção.")
    else:
        st.write(filtered_df_produto)
        with st.expander("Mostrar Resumo Estatístico dos Produtos Filtrados"):
            st.write(filtered_df_produto.describe())

#tabela de armazéns filtrados
with col2:
    st.markdown("## Aplique o filtro na tabela: Armazéns")
    if filtered_df_local.empty:
        st.markdown("### Nenhum armazém selecionado para remoção.")
    else:
        st.write(filtered_df_local)
        with st.expander("Mostrar Resumo Estatístico dos Armazéns Filtrados"):
            st.write(filtered_df_local.describe())
