import pandas as pd
from clasificacion import run_clasificacion
from regresion import run_regresion
from clustering import run_clustering

def main():
    df = pd.read_csv("data/sdss_sample.csv")

    print("Iniciando clasificación...")
    run_clasificacion(df)

    print("Iniciando regresión...")
    run_regresion(df)

    print("Iniciando clustering...")
    run_clustering(df)

    print("Proceso terminado. Revisa la carpeta outputs/")

if __name__ == "__main__":
    main()