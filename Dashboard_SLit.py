# Dashboard1 - Streamlit
# Video aula: https://www.youtube.com/watch?v=P6E_Kts9pxE&t=676s
# Dashboard - KPI´s
# 1 Faturamento por Unidade
# 2 Tipo de Produto mais vendido
# 3 Contribuição por filial
# 4 Desempenho das formas de pagamento
#
# Para rodar: streamlit run dashboard_slit.py

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv",sep=",", decimal=".")
# df.info() - data inicialmente como string (object)

# Ordenação por Datas
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
# df["Date"]

# Seleção de Ano e Mês
df["Month"] = df["Date"].apply(lambda x: str(x.year)+"-"+str(x.month))
month = st.sidebar.selectbox("Mês",df["Month"].unique())
df_filtered = df[df["Month"]==month]
#df_filtered

# Montagem de Dashboard
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Gráfico 1 - Faturamento por Dia
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por Dia")
col1.plotly_chart(fig_date, use_container_width=True)

# Gráfico 2 - Faturamento por Tipo de Produto
fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Faturamento por Tipo de Produto",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

# Gráfico 3 - Faturamento por Filial
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por Filial")
col3.plotly_chart(fig_city, use_container_width=True)

# Gráfico 4 - Faturamento por Tipo de Pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por Tipo de Pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

# Gráfico 5 - Faturamento por Tipo de Pagamento
city_mean = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(city_mean, y="Rating", x="City", title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)