
# Pipeline de Machine Learning para Datos Astronómicos

#  Descripción del proyecto

Este proyecto implementa un pipeline completo de Machine Learning aplicado a datos astronómicos, abordando tres enfoques principales:

- Clasificación supervisada (KNN)
- Regresión (Regresión Lineal)
- Clustering no supervisado (KMeans)

Además, se incorporan buenas prácticas como:
- organización modular del código
- generación de métricas
- visualización de resultados
- automatización parcial con Jenkins

# Objetivo

Desarrollar un pipeline reproducible de Machine Learning que permita analizar datos astronómicos mediante modelos de clasificación, regresión y clustering, generando resultados interpretables y visualmente comprensibles.


# Estructura del proyecto
ml_astronomico/
│
├── data/
│ └── sdss_sample.csv
│
├── src/
│ ├── clasificacion.py
│ ├── regresion.py
│ ├── clustering.py
│ ├── main.py
│
├── outputs/
│ ├── metricas_clasificacion.txt
│ ├── metricas_regresion.txt
│ ├── metricas_clustering.txt
│ ├── matriz_confusion.png
│ ├── regresion_real_vs_predicho.png
│ ├── clusters_kmeans.png
│ ├── clases_reales.png
│ ├── matriz_cluster_vs_clase.png
│
├── tests/
│ └── test_data.py
│
├── Jenkinsfile
├── requirements.txt
└── README.md

# Tecnologías utilizadas

- Python 3.12
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Pytest
- Jenkins

# Modelos implementados

1. Clasificación (KNN)

- Algoritmo: K-Nearest Neighbors (k=5)
- Variables: u, g, r, i, z
- Escalado: StandardScaler

**Resultados:**
- Accuracy: 0.9767
- F1-score promedio: 0.98

**Conclusión:**
El modelo presenta un desempeño alto, logrando una clasificación precisa de los objetos astronómicos.

---

2. Regresión (Redshift)

- Algoritmo: Regresión Lineal

**Métricas:**
- MSE: 0.2985
- MAE: 0.4205
- RMSE: 0.5463
- R²: 0.5153

**Conclusión:**
El modelo presenta un desempeño moderado, indicando que la relación entre las variables no es completamente lineal.

---

3. Clustering (KMeans)

- Algoritmo: KMeans
- Número de clusters: 3

**Métricas:**
- Silhouette Score: 0.5337
- Inercia: 544.7201

**Conclusión:**
Se obtuvo una buena separación entre clusters, evidenciando la capacidad del modelo para identificar patrones en los datos.

---

Visualizaciones generadas

El proyecto genera automáticamente:

- Matriz de confusión (clasificación)
- Gráfico real vs predicho (regresión)
- Clusters generados (KMeans)
- Clases reales
- Matriz cluster vs clase

Estas visualizaciones permiten interpretar los resultados de manera clara y comparativa.

---

Ejecución del proyecto

1. Crear entorno virtual

```bash
python -m venv venv

2. Activar el entorno:
venv\Scripts\activate

3. Instalar dependencias:
pip install -r requirements.txt

4. Ejecutar el pipeline
python src/main.py
#Opcional: 
Ejecutar la dasboahrd
python src/dasboard.py

5. Pruebas
pytest

 Automatización

Se incluye un Jenkinsfile mediante DOCKER que permite:

construir el entorno
ejecutar el pipeline
generar resultados automáticamente
📌 Conclusiones generales
La clasificación mostró un desempeño sobresaliente, con alta precisión en la identificación de clases.
La regresión evidenció limitaciones, lo que sugiere el uso de modelos más complejos.
El clustering permitió identificar patrones relevantes en los datos sin supervisión.
El proyecto demuestra la aplicabilidad de técnicas de Machine Learning en problemas reales.

-------------------------------------------------------> Dashboard interactivos.<-------------------------------------------------------

El proyecto incluye un dashboard desarrollado en **Streamlit**, diseñado para presentar de manera visual y comparativa los resultados obtenidos en los modelos de clasificación, regresión y clustering aplicados al dataset astronómico.

Este dashboard permite consolidar en una sola interfaz:

- métricas principales de clasificación, regresión y clustering
- indicadores clave de desempeño (Accuracy, R² y Silhouette Score)
- visualizaciones comparativas de los resultados generados por cada modelo
- una estructura ejecutiva que facilita la interpretación académica del proyecto

Su objetivo es complementar el análisis técnico del pipeline de Machine Learning mediante una presentación más clara, organizada e intuitiva.

📎 Autor

Sebastian Urrego Argaez
Ingeniería Informática
Institución Universitaria de Envigado

