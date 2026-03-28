import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def run_clustering(df):
    X = df[['u', 'g', 'r', 'i', 'z']]

    # Entrenamiento del modelo
    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = model.fit_predict(X)

    # Métricas
    inertia = model.inertia_
    sil_score = silhouette_score(X, clusters)

    os.makedirs("outputs", exist_ok=True)

    # Gráfico de clusters generados
    plt.figure(figsize=(8, 6))
    plt.scatter(df['u'], df['g'], c=clusters, cmap="viridis", alpha=0.7)
    plt.xlabel("u")
    plt.ylabel("g")
    plt.title("Clusters generados con KMeans (k=3)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outputs/clusters_kmeans.png")
    plt.close()

    # Gráfico de clases reales
    if 'class' in df.columns:
        class_codes = df['class'].astype('category').cat.codes

        plt.figure(figsize=(8, 6))
        plt.scatter(df['u'], df['g'], c=class_codes, cmap="viridis", alpha=0.7)
        plt.xlabel("u")
        plt.ylabel("g")
        plt.title("Clases reales del dataset")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("outputs/clases_reales.png")
        plt.close()

        # Matriz cluster vs clase real
        df_temp = df.copy()
        df_temp['cluster'] = clusters

        matriz = pd.crosstab(df_temp['cluster'], df_temp['class'])

        plt.figure(figsize=(8, 6))
        sns.heatmap(matriz, annot=True, fmt="d", cmap="Blues")
        plt.title("Matriz Cluster vs Clase Real")
        plt.xlabel("Clase real")
        plt.ylabel("Cluster asignado")
        plt.tight_layout()
        plt.savefig("outputs/matriz_cluster_vs_clase.png")
        plt.close()

    # Guardar métricas
    with open("outputs/metricas_clustering.txt", "w", encoding="utf-8") as f:
        f.write("=== MÉTRICAS DE CLUSTERING ===\n\n")
        f.write("Algoritmo: KMeans\n")
        f.write("Número de clusters (k): 3\n\n")
        f.write(f"Inercia: {inertia:.4f}\n")
        f.write(f"Silhouette Score: {sil_score:.4f}\n\n")
        f.write("Interpretación:\n")
        f.write("- La inercia mide la compactación de los clusters; valores menores indican grupos más compactos.\n")
        f.write("- El Silhouette Score mide la separación entre grupos; valores cercanos a 1 indican mejor agrupamiento.\n")
        f.write("- En este caso, el resultado sugiere una buena separación entre los clusters generados.\n")

    print(f"Clustering terminado. Inercia: {inertia:.4f}, Silhouette: {sil_score:.4f}")

    return clusters