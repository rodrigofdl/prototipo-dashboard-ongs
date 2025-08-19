import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ===============
# Dados fictícios
# ===============

# Dados dos documentos (donut chart)
doc_preenchidos = 15
doc_total = 25

donut_data = pd.DataFrame(
    {
        "Status": ["Preenchidos", "Faltantes"],
        "Quantidade": [doc_preenchidos, doc_total - doc_preenchidos],
    }
)

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
        "Data": pd.date_range(start="2024-01-01", end="2024-12-31", freq="M"),
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

# Configuração da página
st.set_page_config(page_title="Dashboard ONG", layout="wide")

# CSS para fundo branco e barra superior
st.markdown(
    """
    <style>
        .stApp {
            background-color: white;
            color: black;
        }

        .block-container {
            background-color: white;
            color: black;
        }

        header[data-testid="stHeader"] {
            background: white;
        }

        h1, h2, h3, h4, h5, h6, p, span, div {
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header com logo, título, emblema e métrica
col1, col2, col3, col4 = st.columns([1, 3, 1, 1])

with col1:
    st.image("logo-exemplo.jpg", width=100)

with col2:
    st.markdown(
        """
        <h1 style="color:black;">
            <a href="https://github.com/rodrigofdl/prototipo-dashboard-ongs" style="text-decoration:none; color:black;">
                ONG Exemplo de Dashboard
            </a>
        </h1>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.image("emblema-ouro.jpg", width=80)

with col4:
    st.metric(label="Nota Geral:", value=f"{nota_geral:.1f}", delta=f"{variacao:+.1f}")

# =================================
# Gráficos de Rosca (Donut) e Pizza
# =================================
col1, col2 = st.columns(2)

with col1:
    # Gráfico de Rosca (Donut) - Documentos
    fig_donut = go.Figure(
        data=[
            go.Pie(
                labels=donut_data["Status"],
                values=donut_data["Quantidade"],
                hole=0.6,
                marker_colors=["#f4842b", "#262a2b"],
            )
        ]
    )

    # Adicionar anotação no centro
    fig_donut.add_annotation(
        text=f"<b>{doc_preenchidos}/{doc_total}</b><br><span style='font-size:14px'>Concluído</span>",
        x=0.5,
        y=0.5,
        font_size=20,
        showarrow=False,
    )
    fig_donut.update_traces(
        textposition="outside",
        textinfo="label+percent",
        hovertemplate="<b>Quantidade: </b>%{value}<extra></extra>",
    )
    fig_donut.update_layout(
        title=dict(
            text="Documentos Preenchidos",
            x=0.31,
            font=dict(color="black", size=22)
        ),
        font=dict(size=14, color="black"),
        showlegend=False,
        paper_bgcolor="#f5f5f5",
        plot_bgcolor="#f5f5f5",
    )

    st.plotly_chart(fig_donut, use_container_width=True)

with col2:
    # Gráfico de Pizza - Termos
    total_termos = termos["Quantidade"].sum()
    termo_principal = termos.loc[termos["Quantidade"].idxmax(), "Tipo"]

    fig_pie = go.Figure(
        data=[
            go.Pie(
                labels=termos["Tipo"],
                values=termos["Quantidade"],
                marker_colors=["#CC5500", "#FFBF00", "#f4842b"],
            )
        ]
    )
    fig_pie.update_traces(
        textposition="outside",
        textinfo="label+value",
        hovertemplate="<b>Porcentagem: </b>%{percent}<extra></extra>",
    )
    fig_pie.update_layout(
        title=dict(
            text="Distribuição de Termos",
            x=0.33,
            font=dict(color="black", size=22)
        ),
        font=dict(size=14, color="black"),
        showlegend=False,
    paper_bgcolor="#f5f5f5",
    plot_bgcolor="white",
    )

    st.plotly_chart(fig_pie, use_container_width=True)

# ================================
# Gráfico de Linha - Visualizações
# ================================

# Gráfico de linha com pontos
fig_line = px.line(
    visualizacoes,
    x="Data",
    y="Visualizações",
    markers=True,  # Adiciona pontos na linha
)

# Customização da linha
fig_line.update_traces(
    line=dict(color="#f4842b", width=3),
    marker=dict(size=9),
    hovertemplate="<b>Visualizações:</b> %{y:,}<extra></extra>",
)
fig_line.update_layout(
    title=dict(
        text="Visualizações ao longo do tempo",
        x=0.42,
        font=dict(color="black", size=22)
    ),
    xaxis_title="Data",
    yaxis_title="Número de Visualizações",
    font=dict(size=14, color="black"),
    hovermode="x unified",
    showlegend=False,
    paper_bgcolor="#f5f5f5",
    plot_bgcolor="#f5f5f5",
)

# Ajustes detalhados nos eixos
fig_line.update_xaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor="rgba(0,0,0,0.1)",
    color="black",
    tickcolor="black",
    tickfont=dict(color="black"),
    title_font=dict(color="black"),
)

fig_line.update_yaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor="rgba(0,0,0,0.1)",
    color="black",
    tickcolor="black",
    tickfont=dict(color="black"),
    title_font=dict(color="black"),
)


st.plotly_chart(fig_line, use_container_width=True)
