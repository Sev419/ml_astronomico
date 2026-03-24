import os
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def run_clustering(df):
    X = df[['u', 'g', 'r', 'i', 'z']]

    model = KMeans(n_clusters=3, random_state=42, n_init=10)
    clusters = model.fit_predict(X)

    os.makedirs("outputs", exist_ok=True)

    plt.scatter(df['u'], df['g'], c=clusters)
    plt.xlabel("u")
    plt.ylabel("g")
    plt.title("Clusters con KMeans")
    plt.savefig("outputs/clusters_kmeans.png")
    plt.close()

    if 'class' in df.columns:
        class_codes = df['class'].astype('category').cat.codes
        plt.scatter(df['u'], df['g'], c=class_codes)
        plt.xlabel("u")
        plt.ylabel("g")
        plt.title("Clases reales")
        plt.savefig("outputs/clases_reales.png")
        plt.close()

    with open("outputs/metricas_clustering.txt", "w", encoding="utf-8") as f:
        f.write("KMeans ejecutado con 3 clusters\n")

    return clusters     