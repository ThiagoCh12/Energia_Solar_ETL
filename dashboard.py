import streamlit as st
import pandas as pd
import plotly.express as px

def criar_dashboard(df):
    
    st.set_page_config(layout="wide") #pagina ocupa a tela toda
    
    # Cálculo de métricas principais
    rendimento_medio = df["rendimento_inversor"].mean()
    maior_rendimento = df["rendimento_inversor"].max()
    menor_rendimento = df["rendimento_inversor"].min()
    geracao_total = df["geração_energetica_kwh"].sum()
    temperatura_media = df["temperatura_inversor"].mean()
    
    st.sidebar.title("📌 Navegação")
    opcao = st.sidebar.selectbox(
        "Selecione uma opção para vizualizar isoladamente:",
        ("Home", "Planilha", "Gráfico de barras", "Gráfico Personalizado")
    )
    
    if opcao == "Home":
        
        st.title("☀️ Energia Solar - Dashboard ")
        with st.container(horizontal_alignment="center"):
            
            #colunas para as metricas
            metrica1, metrica2, metrica3, metrica4, metrica5 = st.columns(5, gap="large")
            
            metrica1.metric("🟢Maior Rendimento", f"{maior_rendimento} %")
            metrica2.metric("🔴Menor Rendimento", f"{menor_rendimento} %")  
            metrica3.metric("🟡Rendimento Médio", f"{rendimento_medio:.2f} %")
            metrica4.metric("⚡ Geração Total", f"{geracao_total} kWh")
            metrica5.metric("🔥Temp. Média Inversor", f"{temperatura_media:.1f} °C")
            
            #colunas para os graficos 
            col1, col2, col3 = st.columns([3, 4, 2], gap="small", vertical_alignment="center") 
            
            with col1:
                st.subheader("📊 Resumo da Planilha")
                st.dataframe(df, width="content", hide_index=True)
            
            with col2:
                st.subheader("📈 Rendimento do Inversor")
                st.bar_chart(df, x="data", y="rendimento_inversor", width=0, height=300)
            
            with col3:
                st.subheader("📈 Gráfico Personalizado")
                coluna_x = st.selectbox(
                    "Selecione a coluna X:", 
                    df.columns,
                    index=list(df.columns).index("temperatura_inversor"),
                    key="x")
                coluna_y = st.selectbox(
                    "Selecione a coluna Y:", 
                    df.columns, 
                    index=list(df.columns).index("geração_energetica_kwh"),
                    key="y")
                st.line_chart(df, x=coluna_x, y=coluna_y, width="content", height=200)
    
    elif opcao == "Planilha":
        st.subheader("📊 Resumo da Planilha")
        st.dataframe(df, width="content", hide_index=True)
    
    elif opcao == "Gráfico de barras":
        
        st.subheader("📈 Rendimento do Inversor")
        st.bar_chart(df, x="data", y="rendimento_inversor", width=0, height=300)
    
    elif opcao == "Gráfico Personalizado":
        st.subheader("📈 Gráfico Personalizado")
        coluna_x = st.selectbox("Selecione a coluna X:", 
                                df.columns, 
                                index=list(df.columns).index("temperatura_inversor"), 
                                key="x_sidebar")
        coluna_y = st.selectbox("Selecione a coluna Y:", 
                                df.columns, 
                                index=list(df.columns).index("geração_energetica_kwh"),
                                key="y_sidebar")
        st.line_chart(df, x=coluna_x, y=coluna_y)
        
        
        
        
    

    # with analises:
    #     coluna1, coluna2 = st.columns(2)

    #     with coluna1:
    #         if "data" in df.columns and "geração_energetica_kwh" in df.columns:
    #             fig1 = px.line(df, x="data", y="geração_energetica_kwh",
    #                            title="Geração Diária (kWh)", markers=True,
    #                            line_shape="spline", color_discrete_sequence=["green"])
    #             st.plotly_chart(fig1, use_container_width=True)

    #     with coluna2:
    #         if "temperatura_inversor" in df.columns and "rendimento_inversor" in df.columns:
    #             fig2 = px.scatter(df, x="temperatura_inversor", y="rendimento_inversor",
    #                               color="geração_energetica_kwh",
    #                               title="Rendimento vs Temperatura")
    #             st.plotly_chart(fig2, use_container_width=True)
