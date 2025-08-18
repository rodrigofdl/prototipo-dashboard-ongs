import streamlit as st
import pandas as pd
import altair as alt

# Configuração da página
st.set_page_config(layout="wide")

# ===============
# Dados fictícios
# ===============

# Documentos preenchidos
doc_total = 25
doc_preenchidos = 15

# Distribuição de termos
termos = pd.DataFrame(
    {
        "Tipo": ["Termo Municipal", "Termo Estadual", "Emenda Parlamentar"],
        "Quantidade": [2, 1, 3],
    }
)

# Visualizações ao longo do tempo
visualizacoes = pd.DataFrame(
    {
        "Data": pd.date_range("2024-01-01", periods=12, freq="M"),
        "Visualizações": [120, 150, 180, 200, 220, 250, 240, 260, 280, 300, 320, 350],
    }
)

# Nota geral (exemplo)
nota_geral = 8.2
nota_anterior = 7.8
variacao = round(nota_geral - nota_anterior, 2)

# =============
# Visualizações
# =============

# Logo + Nome ONG + Nível + Nota Geral
col1, col2, col3, col4 = st.columns([1, 3, 1, 1])
with col1:
    st.image("logo-exemplo.jpg", width=100)
with col2:
    st.markdown(
        "# [ONG Exemplo de Dashboard](https://github.com/rodrigofdl/prototipo-dashboard-ongs)"
    )
with col3:
    st.image("emblema-ouro.png", width=80)
with col4:
    st.metric(
        label="Nota Geral: ",
        value=nota_geral,
        delta=f"{variacao}",  # se negativo, o Streamlit mostra em vermelho
    )
    
# Gráficos de rosca + pizza
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    donut_data = pd.DataFrame(
        {
            "Status": ["Preenchidos", "Faltantes"],
            "Quantidade": [doc_preenchidos, doc_total - doc_preenchidos],
        }
    )
    donut_chart = (
        alt.Chart(donut_data)
        .mark_arc(innerRadius=50)
        .encode(theta="Quantidade", color="Status", tooltip=["Status", "Quantidade"])
    ).properties(title="Documentos Preenchidos")
    st.altair_chart(donut_chart, use_container_width=True)

with col2:
    pie_chart = (
        alt.Chart(termos)
        .mark_arc()
        .encode(theta="Quantidade", color="Tipo", tooltip=["Tipo", "Quantidade"])
    ).properties(title="Distribuição de Termos")
    st.altair_chart(pie_chart, use_container_width=True)

# Gráfico de Linha
st.markdown("---")

line_chart = (
    alt.Chart(visualizacoes)
    .mark_line(point=True)
    .encode(x="Data", y="Visualizações", tooltip=["Data", "Visualizações"])
).properties(title="Visualizações ao longo do tempo")

st.altair_chart(line_chart, use_container_width=True)
