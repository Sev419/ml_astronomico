import os
import streamlit as st
from PIL import Image

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Dashboard Ejecutivo de Machine Learning",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# FUNCIONES AUXILIARES
# =========================================================
def leer_texto(path: str, default: str = "No disponible") -> str:
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                contenido = f.read().strip()
                return contenido if contenido else default
        return default
    except Exception as e:
        return f"Error al leer archivo: {e}"


def existe_archivo(path: str) -> bool:
    return os.path.exists(path) and os.path.isfile(path)


def mostrar_grafica(titulo: str, ruta_imagen: str, analisis: str) -> None:
    st.markdown(f'<div class="graph-title">{titulo}</div>', unsafe_allow_html=True)

    if existe_archivo(ruta_imagen):
        imagen = Image.open(ruta_imagen)
        st.image(imagen, use_container_width=True)
    else:
        st.warning(f"No se encontró el archivo: {os.path.basename(ruta_imagen)}")

    st.markdown(
        f'<div class="analysis-box">{analisis.strip()}</div>',
        unsafe_allow_html=True
    )

# =========================================================
# RUTAS
# =========================================================
RUTA_METRICAS_CLASIFICACION = "outputs/metricas_clasificacion.txt"
RUTA_METRICAS_REGRESION = "outputs/metricas_regresion.txt"

RUTA_IMG_REGRESION = "outputs/regresion_real_vs_predicho.png"
RUTA_IMG_CONFUSION = "outputs/matriz_confusion.png"
RUTA_IMG_CLUSTER = "outputs/clusters_kmeans.png"

# =========================================================
# CARGA DE DATOS
# =========================================================
metricas_clasificacion = leer_texto(RUTA_METRICAS_CLASIFICACION)
metricas_regresion = leer_texto(RUTA_METRICAS_REGRESION)

# =========================================================
# ESTILOS CSS
# =========================================================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #676767 0%, #b7b7b7 45%, #7a624f 100%);
    }

    .block-container {
        max-width: 1420px;
        margin: 1.2rem auto 2rem auto;
        background: rgba(244, 246, 248, 0.96);
        padding: 2rem 2rem 2.2rem 2rem;
        border-radius: 24px;
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.18);
        border: 1px solid rgba(255,255,255,0.25);
    }

    h1, h2, h3 {
        color: #243447;
    }

    .hero-title {
        font-size: 2rem;
        font-weight: 700;
        color: #243447;
        text-align: center;
        margin-bottom: 0.35rem;
    }

    .hero-subtitle {
        font-size: 1rem;
        color: #4e5b61;
        text-align: center;
        margin-bottom: 1.4rem;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #243447;
        margin-top: 0.2rem;
        margin-bottom: 0.8rem;
    }

    .section-description {
        background: #eef2f5;
        border-left: 5px solid #8b6f47;
        padding: 14px 16px;
        border-radius: 12px;
        color: #2f3e46;
        font-size: 0.96rem;
        line-height: 1.5;
        margin-bottom: 1rem;
    }

    .metric-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0px 4px 14px rgba(0, 0, 0, 0.08);
        border: 1px solid #d9dde2;
        min-height: 220px;
        margin-bottom: 0.5rem;
    }

    .metric-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #243447;
        margin-bottom: 0.8rem;
    }

    .metric-body {
        color: #2e2e2e;
        font-size: 0.95rem;
        line-height: 1.6;
        white-space: pre-wrap;
    }

    .compare-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0px 4px 14px rgba(0, 0, 0, 0.08);
        border-top: 5px solid #6b4f3b;
        border-left: 1px solid #d9dde2;
        border-right: 1px solid #d9dde2;
        border-bottom: 1px solid #d9dde2;
        min-height: 285px;
        margin-bottom: 0.5rem;
    }

    .compare-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #243447;
        margin-bottom: 0.7rem;
    }

    .compare-text {
        font-size: 0.95rem;
        color: #2e2e2e;
        line-height: 1.58;
    }

    .graph-title {
        font-size: 1.02rem;
        font-weight: 700;
        color: #243447;
        margin-bottom: 0.8rem;
    }

    .analysis-box {
        margin-top: 0.9rem;
        background: #f7f9fb;
        border-radius: 10px;
        padding: 12px;
        font-size: 0.94rem;
        color: #2f2f2f;
        line-height: 1.55;
        border: 1px solid #e3e8ed;
    }

    .summary-box {
        background: #ffffff;
        border-radius: 16px;
        padding: 20px;
        border-left: 6px solid #8b6f47;
        box-shadow: 0px 4px 14px rgba(0, 0, 0, 0.08);
        color: #2e2e2e;
        line-height: 1.65;
    }

    hr {
        border: none;
        border-top: 1px solid #d0d4d8;
        margin: 1.4rem 0 1.2rem 0;
    }

    [data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #d9dde2;
        padding: 14px;
        border-radius: 16px;
        box-shadow: 0px 4px 14px rgba(0, 0, 0, 0.08);
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# ENCABEZADO
# =========================================================
st.markdown(
    '<div class="hero-title">Dashboard Ejecutivo de Machine Learning Astronómico</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero-subtitle">
Visualización comparativa de clasificación, regresión y clustering en una estructura ejecutiva,
ordenada y clara.
</div>
""", unsafe_allow_html=True)

# =========================================================
# KPIs
# =========================================================
k1, k2, k3 = st.columns(3)

with k1:
    st.metric("Modelos evaluados", "3", "Clasificación / Regresión / Clustering")

with k2:
    st.metric("Tipo de análisis", "Comparativo", "Supervisado y no supervisado")

with k3:
    st.metric("Estado del dashboard", "Cargado", "Visualización consolidada")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================================================
# MÉTRICAS DE DESEMPEÑO
# =========================================================
st.markdown('<div class="section-title">Métricas de desempeño</div>', unsafe_allow_html=True)

st.markdown("""
<div class="section-description">
En esta sección se presentan las métricas principales de los modelos supervisados implementados,
permitiendo identificar su nivel de ajuste y capacidad de desempeño sobre los datos analizados.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="metric-title">Clasificación (KNN)</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric-body">{metricas_clasificacion}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="metric-title">Regresión lineal</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="metric-body">{metricas_regresion}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# =========================================================
# COMPARACIÓN DE MODELOS
# =========================================================
st.markdown('<div class="section-title">Comparación de modelos</div>', unsafe_allow_html=True)

st.markdown("""
<div class="section-description">
La comparación se organiza de forma ejecutiva para mostrar el propósito, el aporte analítico
y las principales fortalezas de cada modelo dentro del pipeline desarrollado.
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="compare-card">
        <div class="compare-title">Clasificación</div>
        <div class="compare-text">
            <strong>Tipo:</strong> Supervisado<br>
            <strong>Modelo:</strong> KNN<br>
            <strong>Objetivo:</strong> Diferenciar clases astronómicas.<br><br>
            <strong>Análisis:</strong><br>
            Este modelo presenta el mejor desempeño general del tablero. La precisión obtenida
            indica que las variables seleccionadas contienen información suficiente para separar
            adecuadamente las clases después del preprocesamiento aplicado.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="compare-card">
        <div class="compare-title">Regresión</div>
        <div class="compare-text">
            <strong>Tipo:</strong> Supervisado<br>
            <strong>Modelo:</strong> Regresión lineal<br>
            <strong>Objetivo:</strong> Estimar la variable continua <em>redshift</em>.<br><br>
            <strong>Análisis:</strong><br>
            El modelo presenta una capacidad predictiva útil, aunque moderada. La dispersión de los
            resultados sugiere que parte del comportamiento del fenómeno no sigue una relación
            estrictamente lineal.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="compare-card">
        <div class="compare-title">Clustering</div>
        <div class="compare-text">
            <strong>Tipo:</strong> No supervisado<br>
            <strong>Modelo:</strong> KMeans<br>
            <strong>Objetivo:</strong> Detectar agrupamientos naturales.<br><br>
            <strong>Análisis:</strong><br>
            Este enfoque aporta valor exploratorio al pipeline, ya que permite identificar patrones
            internos en los datos y complementar la lectura obtenida con los modelos supervisados.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# =========================================================
# VISUALIZACIÓN COMPARATIVA DE RESULTADOS
# =========================================================
st.markdown(
    '<div class="section-title">Visualización comparativa de resultados</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="section-description">
Las gráficas se presentan en formato horizontal para facilitar la comparación visual entre los resultados
obtenidos por cada uno de los enfoques implementados.
</div>
""", unsafe_allow_html=True)

g1, g2, g3 = st.columns(3)

with g1:
    mostrar_grafica(
        "Regresión: valores reales vs. predichos",
        RUTA_IMG_REGRESION,
        """
        Los puntos cercanos a la referencia ideal reflejan un mejor ajuste del modelo.
        La dispersión observada indica que la regresión logra capturar parte del comportamiento
        de la variable objetivo, aunque todavía existen desviaciones importantes.
        """
    )

with g2:
    mostrar_grafica(
        "Clasificación: matriz de confusión",
        RUTA_IMG_CONFUSION,
        """
        La concentración de aciertos en la diagonal principal respalda la consistencia del modelo.
        Este comportamiento es coherente con un desempeño favorable y una adecuada separación entre clases.
        """
    )

with g3:
    mostrar_grafica(
        "Clustering: distribución de grupos",
        RUTA_IMG_CLUSTER,
        """
        La segmentación por colores permite observar cómo KMeans organiza los registros con base en
        similitudes internas. Esta lectura fortalece la interpretación exploratoria del conjunto de datos.
        """
    )

st.markdown("<hr>", unsafe_allow_html=True)

# =========================================================
# CONCLUSIÓN GENERAL
# =========================================================
st.markdown('<div class="section-title">Conclusión general</div>', unsafe_allow_html=True)

st.markdown("""
<div class="summary-box">
El dashboard presenta una estructura más limpia, corporativa y funcional. En términos comparativos,
la clasificación evidencia el mejor desempeño global, la regresión cumple una función predictiva con
espacio de mejora, y el clustering complementa el análisis con una perspectiva exploratoria.
La organización visual actual prioriza claridad, jerarquía informativa y lectura ejecutiva.
</div>
""", unsafe_allow_html=True)

st.success("Dashboard cargado correctamente.")