import streamlit as st

def criar_dashboard(df):
    st.set_page_config(layout="wide")  # página ocupa a tela toda
    
    # Cálculo de métricas principais
    rendimento_medio = df["rendimento_inversor"].mean()
    maior_rendimento = df["rendimento_inversor"].max()
    menor_rendimento = df["rendimento_inversor"].min()
    geracao_total = df["geração_energetica_kwh"].sum()
    
    st.sidebar.title("📌 Navegação")
    opcao = st.sidebar.selectbox(
        "Selecione uma opção para visualizar isoladamente:",
        ("Home", "Planilha", "Gráfico de barras", "Gráfico Personalizado")
    )
    
    if opcao == "Home":
        st.title("☀️ Energia Solar - Dashboard ")
        
        # colunas para as métricas (com borda em cada coluna)
        metrica1, metrica2, metrica3 = st.columns(3, gap="large", border=False)
        
        with metrica1:
            st.metric("🟢 Maior Rendimento", f"{maior_rendimento} %", border=True)
            st.metric("🔴 Menor Rendimento", f"{menor_rendimento} %", border=True)  
        with metrica2:
            st.metric("🟡 Rendimento Médio", f"{rendimento_medio:.2f} %", border=True)
            st.metric("⚡ Geração Total", f"{geracao_total} kWh", border= True)
        with metrica3:
            with st.container(border=True):
                st.subheader("🔥 Temperatura do Inversor")
                st.line_chart(df, x="data", y="temperatura_inversor", height=250)
        
        # colunas para os gráficos 
        col1, col2 = st.columns([3, 4], gap="large")
        
        with col1:
            with st.container(border=True):
                st.subheader("📈 Rendimento do Inversor")
                st.bar_chart(df, x="data", y="rendimento_inversor", height=200)
            
            with st.container(border=True):
                st.subheader("📈 Gráfico Personalizado")
                coluna_x = st.selectbox(
                    "Selecione a coluna X:", 
                    df.columns,
                    index=list(df.columns).index("temperatura_inversor"),
                    key="x"
                )
                coluna_y = st.selectbox(
                    "Selecione a coluna Y:", 
                    df.columns, 
                    index=list(df.columns).index("geração_energetica_kwh"),
                    key="y"
                )
                st.line_chart(df, x=coluna_x, y=coluna_y, height=200)

        with col2:
            with st.container(border=True):
                st.subheader("📊 Resumo da Planilha")
                st.dataframe(df, use_container_width=True, hide_index=True)
    
    elif opcao == "Planilha":
        with st.container(border=True):
            st.subheader("📊 Resumo da Planilha")
            st.dataframe(df, use_container_width=True, hide_index=True)
    
    elif opcao == "Gráfico de barras":
        with st.container(border=True):
            st.subheader("📈 Rendimento do Inversor")
            st.bar_chart(df, x="data", y="rendimento_inversor", height=300)
    
    elif opcao == "Gráfico Personalizado":
        with st.container(border=True):
            st.subheader("📈 Gráfico Personalizado")
            coluna_x = st.selectbox(
                "Selecione a coluna X:", 
                df.columns, 
                index=list(df.columns).index("temperatura_inversor"), 
                key="x_sidebar"
            )
            coluna_y = st.selectbox(
                "Selecione a coluna Y:", 
                df.columns, 
                index=list(df.columns).index("geração_energetica_kwh"),
                key="y_sidebar"
            )
            st.line_chart(df, x=coluna_x, y=coluna_y)
