import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 1. Configuración de la página (ancho completo para aprovechar el espacio)
st.set_page_config(
    page_title="Dashboard Ejecutivo de Ventas",
    page_icon="📈",
    layout="wide"
)

# 2. Función con caché para simular la carga de datos optimizada
@st.cache_data
def cargar_datos():
    # Simulamos un dataset de ventas de una empresa con varias regiones
    np.random.seed(42)
    fechas = pd.date_range(start="2025-01-01", end="2025-12-31", freq="D")
    
    data = {
        "Fecha": np.random.choice(fechas, 1000),
        "Region": np.random.choice(["Norte", "Sur", "Este", "Oeste"], 1000),
        "Producto": np.random.choice(["Software A", "Hardware B", "Servicios C"], 1000),
        "Ventas": np.random.uniform(500, 5000, 1000).round(2),
        "Unidades": np.random.randint(1, 20, 1000)
    }
    return pd.DataFrame(data)

df_raw = cargar_datos()

# 3. Panel Lateral (Sidebar) para Filtros profesionales
st.sidebar.header("🎛️ Filtros Globales")
region_seleccionada = st.sidebar.selectbox(
    "Selecciona la Región:", 
    options=["Todas"] + list(df_raw["Region"].unique())
)

# Filtrar datos según la selección del usuario
if region_seleccionada != "Todas":
    df = df_raw[df_raw["Region"] == region_seleccionada]
else:
    df = df_raw

# 4. Título Principal
st.title("📊 Dashboard Ejecutivo de Ventas")
st.markdown("Panel de control interactivo con análisis financiero y métricas de rendimiento en tiempo real.")

# 5. Métricas Clave (KPIs) en columnas
total_ventas = df["Ventas"].sum()
total_unidades = df["Unidades"].sum()
ticket_promedio = df["Ventas"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Ventas Totales", f"${total_ventas:,.2f}", delta="+12.4% vs año ant.")
col2.metric("Unidades Vendidas", f"{total_unidades:,}", delta="+5.1%")
col3.metric("Ticket Promedio", f"${ticket_promedio:,.2f}", delta="-1.2%")

st.markdown("---")

# 6. Gráficos Interactivos Avanzados con Plotly (Organizados en 2 columnas)
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("📈 Evolución de Ventas en el Tiempo")
    # Agrupar por fecha para el gráfico de línea
    df_tiempo = df.groupby("Fecha")["Ventas"].sum().reset_index()
    fig_linea = px.line(
        df_tiempo, x="Fecha", y="Ventas", 
        template="plotly_white",
        color_discrete_sequence=["#29b5e8"]
    )
    fig_linea.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig_linea, use_container_width=True)

with col_graf2:
    st.subheader("📦 Ventas por Línea de Producto")
    # Agrupar por producto para el gráfico de barras
    df_prod = df.groupby("Producto")["Ventas"].sum().reset_index()
    fig_barra = px.bar(
        df_prod, x="Producto", y="Ventas", 
        color="Producto",
        template="plotly_white"
    )
    fig_barra.update_layout(margin=dict(l=0, r=0, t=30, b=0), showlegend=False)
    st.plotly_chart(fig_barra, use_container_width=True)

# 7. Sección Desplegable para Datos Detallados
with st.expander("🔍 Ver tabla de datos detallados"):
    st.dataframe(df, use_container_width=True)