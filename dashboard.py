import os
import re
import html
import streamlit as st
from PIL import Image
from styles import aplicar_estilos

# =========================================================
# CONFIGURACIÓN
# =========================================================
st.set_page_config(
    page_title="Dashboard Ejecutivo de Machine Learning",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(aplicar_estilos(), unsafe_allow_html=True)

# =========================================================
# FUNCIONES
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


def texto_html_seguro(texto: str) -> str:
    return html.escape(texto)


def existe_archivo(path: str) -> bool:
    return os.path.exists(path) and os.path.isfile(path)


def extraer_valor(texto: str, patron: str, default: str = "N/A") -> str:
    match = re.search(patron, texto, re.IGNORECASE)
    return match.group(1).strip() if match else default


def render_metric_card(titulo: str, contenido: str) -> None:
    contenido_seguro = texto_html_seguro(contenido)
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{titulo}</div>
        <div class="metric-body"><pre>{contenido_seguro}</pre></div>
    </div>
    """, unsafe_allow_html=True)


def mostrar_grafica(titulo: str, ruta: str, analisis: str) -> None:
    st.markdown(f'<div class="graph-title">{titulo}</div>', unsafe_allow_html=True)

    if existe_archivo(ruta):
        st.image(Image.open(ruta), use_container_width=True)
    else:
        st.warning(f"No se encontró el archivo: {os.path.basename(ruta)}")

    st.markdown(
        f'<div class="analysis-box">{analisis}</div>',
        unsafe_allow_html=True
    )

# =========================================================
# RUTAS
# =========================================================
RUTA_METRICAS_CLASIFICACION = "outputs/metricas_clasificacion.txt"
RUTA_METRICAS_REGRESION = "outputs/metricas_regresion.txt"
RUTA_METRICAS_CLUSTERING = "outputs/metricas_clustering.txt"

RUTA_IMG_CONFUSION = "outputs/matriz_confusion.png"
RUTA_IMG_REGRESION = "outputs/regresion_real_vs_predicho.png"
RUTA_IMG_CLUSTER = "outputs/clusters_kmeans.png"
RUTA_IMG_CLASES_REALES = "outputs/clases_reales.png"
RUTA_IMG_MATRIZ_CLUSTER = "outputs/matriz_cluster_vs_clase.png"

# =========================================================
# CARGA DE DATOS
# =========================================================
metricas_clasificacion = leer_texto(RUTA_METRICAS_CLASIFICACION)
metricas_regresion = leer_texto(RUTA_METRICAS_REGRESION)
metricas_clustering = leer_texto(RUTA_METRICAS_CLUSTERING)

accuracy = extraer_valor(metricas_clasificacion, r"Accuracy:\s*([0-9.]+)")
r2_val = extraer_valor(metricas_regresion, r"R2:\s*([0-9.]+)")
silhouette = extraer_valor(metricas_clustering, r"Silhouette Score:\s*([0-9.]+)")

# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("Panel de navegación")

vista = st.sidebar.radio(
    "Explora el dashboard",
    [
        "📊 Resumen general",
        "🧠 Clasificación",
        "📈 Regresión",
        "🧩 Clustering"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Proyecto:** ML astronómico")
st.sidebar.markdown("**Modelos evaluados:** 3")
st.sidebar.markdown("**Automatización:** Docker + Jenkins")
st.sidebar.markdown("Sebastian Urrego Argaez")
st.sidebar.markdown("--2026--BIGDATA")

# =========================================================
# CABECERA PRINCIPAL
# =========================================================
st.markdown(
    '<div class="hero-title">Dashboard Ejecutivo de Machine Learning Astronómico</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="hero-subtitle">
Análisis comparativo de clasificación, regresión y clustering sobre datos astronómicos,
presentado con una estructura clara, académica y orientada a resultados.
</div>
""", unsafe_allow_html=True)

top1, top2, top3 = st.columns(3)

with top1:
    st.metric("Accuracy", accuracy)

with top2:
    st.metric("R²", r2_val)

with top3:
    st.metric("Silhouette", silhouette)

st.markdown("<hr>", unsafe_allow_html=True)

# =========================================================
# RESUMEN GENERAL
# =========================================================
if vista == "📊 Resumen general":
    st.markdown('<div class="section-title">Resumen general del pipeline</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-description">
    Esta vista integra las métricas principales del proyecto y las visualizaciones comparativas
    de clasificación, regresión y clustering en una estructura ejecutiva de doble panel.
    </div>
    """, unsafe_allow_html=True)

    izquierda, derecha = st.columns([1, 1.25], gap="large")

    with izquierda:
        st.markdown('<div class="section-title">Métricas del proyecto</div>', unsafe_allow_html=True)

        render_metric_card("Clasificación (KNN)", metricas_clasificacion)
        render_metric_card("Clustering (KMeans)", metricas_clustering)
        render_metric_card("Regresión lineal", metricas_regresion)

    with derecha:
        st.markdown('<div class="section-title">Visualización comparativa de resultados</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="section-description">
        Las siguientes pestañas conservan la estructura de navegación por páginas para comparar
        visualmente el comportamiento de cada modelo implementado.
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(["Clasificación", "Regresión", "Clustering"])

        with tab1:
            mostrar_grafica(
                "Matriz de confusión - Modelo KNN",
                RUTA_IMG_CONFUSION,
                """
                La alta concentración de valores en la diagonal principal evidencia una clasificación
                consistente y un alto nivel de precisión entre las clases.
                """
            )

        with tab2:
            mostrar_grafica(
                "Regresión lineal - Valores reales vs predichos",
                RUTA_IMG_REGRESION,
                """
                La gráfica muestra que el modelo captura parte de la tendencia del redshift, aunque
                se observan zonas de concentración y dispersión que reflejan limitaciones del ajuste lineal.
                """
            )

        with tab3:
            sub1, sub2 = st.columns(2)

            with sub1:
                mostrar_grafica(
                    "Clusters generados con KMeans",
                    RUTA_IMG_CLUSTER,
                    """
                    La separación visual de los grupos apoya la interpretación exploratoria de los datos
                    y respalda la existencia de patrones internos relevantes.
                    """
                )

            with sub2:
                mostrar_grafica(
                    "Matriz Cluster vs Clase Real",
                    RUTA_IMG_MATRIZ_CLUSTER,
                    """
                    Esta comparación permite relacionar los agrupamientos obtenidos con las clases originales
                    del dataset y fortalece la interpretación del clustering.
                    """
                )

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown('<div class="section-title">Conclusión general</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="summary-box">
    El dashboard organiza el proyecto en una estructura de doble panel que facilita la lectura comparativa
    entre métricas y resultados visuales. La clasificación presenta el mejor desempeño global, la regresión
    ofrece una aproximación útil aunque moderada, y el clustering aporta valor exploratorio mediante la
    identificación de agrupamientos y su contraste con las clases reales.
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# VISTA CLASIFICACIÓN
# =========================================================
elif vista == "🧠 Clasificación":
    st.markdown('<div class="section-title">Análisis del modelo de clasificación</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-description">
    Esta vista presenta el comportamiento del modelo KNN a partir de sus métricas y su matriz de confusión.
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.15], gap="large")

    with c1:
        render_metric_card("Métricas de clasificación", metricas_clasificacion)

    with c2:
        mostrar_grafica(
            "Matriz de confusión - KNN",
            RUTA_IMG_CONFUSION,
            """
            El predominio de aciertos en la diagonal principal confirma que el modelo clasifica correctamente
            la mayoría de las observaciones y mantiene un desempeño sólido.
            """
        )

# =========================================================
# VISTA REGRESIÓN
# =========================================================
elif vista == "📈 Regresión":
    st.markdown('<div class="section-title">Análisis del modelo de regresión</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-description">
    Esta vista presenta las métricas del modelo de regresión lineal y la relación entre valores reales y predichos.
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.15], gap="large")

    with c1:
        render_metric_card("Métricas de regresión", metricas_regresion)

    with c2:
        mostrar_grafica(
            "Valores reales vs predichos",
            RUTA_IMG_REGRESION,
            """
            La dispersión observada indica que el modelo aproxima parcialmente la tendencia general del redshift,
            aunque persisten señales de subajuste en ciertos rangos.
            """
        )

# =========================================================
# VISTA CLUSTERING
# =========================================================
elif vista == "🧩 Clustering":
    st.markdown('<div class="section-title">Análisis del modelo de clustering</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="section-description">
    Esta vista muestra las métricas de KMeans y las visualizaciones necesarias para interpretar
    los agrupamientos encontrados y su relación con las clases reales.
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.15], gap="large")

    with c1:
        render_metric_card("Métricas de clustering", metricas_clustering)

    with c2:
        mostrar_grafica(
            "Clusters generados con KMeans",
            RUTA_IMG_CLUSTER,
            """
            Los grupos obtenidos muestran una separación visual adecuada y respaldan el valor
            exploratorio del modelo no supervisado.
            """
        )

    st.markdown("<hr>", unsafe_allow_html=True)

    d1, d2 = st.columns(2, gap="large")

    with d1:
        mostrar_grafica(
            "Clases reales del dataset",
            RUTA_IMG_CLASES_REALES,
            """
            Esta visualización facilita la comparación entre la estructura original del dataset
            y la agrupación generada por el modelo.
            """
        )

    with d2:
        mostrar_grafica(
            "Matriz Cluster vs Clase Real",
            RUTA_IMG_MATRIZ_CLUSTER,
            """
            La matriz permite analizar la correspondencia entre los clusters obtenidos y las etiquetas
            originales, fortaleciendo la interpretación del agrupamiento.
            """
        )

st.success("Dashboard cargado correctamente.")