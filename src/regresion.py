import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def run_regresion(df):
    X = df[['u', 'g', 'r', 'i', 'z']]
    y = df['redshift']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/metricas_regresion.txt", "w", encoding="utf-8") as f:
        f.write("=== MÉTRICAS DE REGRESIÓN ===\n\n")
        f.write(f"MSE: {mse:.4f}\n")
        f.write(f"MAE: {mae:.4f}\n")
        f.write(f"RMSE: {rmse:.4f}\n")
        f.write(f"R2: {r2:.4f}\n")

    plt.figure(figsize=(8, 6))

    error = np.abs(y_test - y_pred)

    scatter = plt.scatter(
        y_test,
        y_pred,
        c=error,
        cmap="viridis",
        alpha=0.7
    )

    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())

    plt.plot(
        [min_val, max_val],
        [min_val, max_val],
        color="red",
        linestyle="--",
        label="Predicción perfecta"
    )

    plt.colorbar(scatter, label="Error absoluto")
    plt.xlabel("Valores reales")
    plt.ylabel("Valores predichos")
    plt.title("Regresión lineal - Real vs Predicho")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("outputs/regresion_real_vs_predicho.png")
    plt.close()

    print(
        f"Regresión terminada. "
        f"MSE: {mse:.4f}, MAE: {mae:.4f}, RMSE: {rmse:.4f}, R2: {r2:.4f}"
    )