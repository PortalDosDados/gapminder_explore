import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================
st.set_page_config(
    page_title="Gapminder - Análise de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================
# TÍTULO E DESCRIÇÃO
# =========================
st.title("Análise de Dados com Gapminder")
st.write(
    "Aplicação simples para explorar dados de população, "
    "PIB per capita e expectativa de vida ao longo do tempo."
)

# =========================
# CARREGAMENTO DOS DADOS
# =========================
df = px.data.gapminder()

# =========================
# EXIBIÇÃO DOS DADOS
# =========================
st.subheader("Visualização dos dados")
st.dataframe(df)

# =========================
# FILTRO INTERATIVO
# =========================
ano = st.slider(
    "Selecione o ano",
    min_value=int(df["year"].min()),
    max_value=int(df["year"].max()),
    step=5,
    value=int(df["year"].min()),
)

df_filtrado = df[df["year"] == ano]

# =========================
# GRÁFICO
# =========================
fig = px.scatter(
    df_filtrado,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    log_x=True,
    size_max=60,
    title=f"PIB per capita vs Expectativa de Vida ({ano})",
)

st.plotly_chart(fig, use_container_width=True)
