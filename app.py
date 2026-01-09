import streamlit as st
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
# FUNÇÃO DE CARREGAMENTO (CACHE)
# =========================
@st.cache_data
def load_data():
    df = px.data.gapminder()
    return df


# =========================
# CARREGAMENTO DOS DADOS
# =========================
df = load_data()

# =========================
# TÍTULO E DESCRIÇÃO
# =========================
st.title("Análise de Dados com Gapminder")
st.write(
    "Exploração interativa de dados históricos de população, "
    "PIB per capita e expectativa de vida."
)

# =========================
# SIDEBAR - FILTROS
# =========================
st.sidebar.header("Filtros")

ano = st.sidebar.slider(
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

# =========================
# TABELA
# =========================
st.subheader("Dados filtrados")
st.dataframe(df_filtrado)
