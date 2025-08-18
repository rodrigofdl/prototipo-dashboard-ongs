# 📊 Dashboard de ONGs (Protótipo)

Este projeto é um **protótipo de dashboard** desenvolvido com **Streamlit** e **Altair**, que apresenta informações de Organizações Não Governamentais (ONGs) de forma visual e intuitiva.  

O objetivo é demonstrar como dados de transparência podem ser apresentados em um formato acessível, com indicadores de desempenho, gráficos e evolução temporal.  

## 🚀 Funcionalidades

- ✅ Exibição do **logo e nome da ONG** (com link para a página oficial).  
- ✅ Indicador de **nível** (ex.: bronze, prata, ouro, diamante).  
- ✅ **Nota geral** com variação em relação ao período anterior.  
- ✅ **Gráfico de rosca** mostrando a proporção de documentos preenchidos.  
- ✅ **Gráfico de pizza** com a distribuição dos tipos de termos/contratos.  
- ✅ **Gráfico de linha** exibindo a evolução das visualizações ao longo do tempo.  

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Altair](https://altair-viz.github.io/)  
- [Pandas](https://pandas.pydata.org/)  

## 📂 Estrutura do projeto

prototipo-dashboard-ongs/  
│── app.py  # Código principal do dashboard  
│── requirements.txt  # Dependências do projeto  
│── emblema-ouro.png  # Imagem do emblema de ouro
│── logo-exemplo.jpg  # Imagem do logo de exemplo
│── README.md  # Documentação do projeto  
│── .gitignore  

## ▶️ Como executar o projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/rodrigofdl/prototipo-dashboard-ongs.git
    cd dashboard-ongs
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    .venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    
4. Execute o dashboard:
    ```bash
    streamlit run app.py
    ```

5. O navegador abrirá automaticamente em:
    ```arduino
    http://localhost:8501
    ```

## 📸 Exemplo de visualização

Logo + Nome da ONG (clicável)

Indicadores com evolução da nota

Gráficos interativos (rosca, pizza e linha)

## 👨‍💻 Autor

Projeto desenvolvido por Rodrigo Felisberto  
📧 Email: rodrigo.fdlira@gmail.com
