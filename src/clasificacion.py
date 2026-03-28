import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)


def run_clasificacion(df):
    X = df[['u', 'g', 'r', 'i', 'z']]
    y = df['class']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report_text = classification_report(y_test, y_pred)

    os.makedirs("outputs", exist_ok=True)

    with open("outputs/metricas_clasificacion.txt", "w", encoding="utf-8") as f:
        f.write("=== MÉTRICAS DE CLASIFICACIÓN ===\n\n")
        f.write(f"Accuracy: {acc:.4f}\n\n")
        f.write("=== MATRIZ DE CONFUSIÓN ===\n")
        f.write(str(cm))
        f.write("\n\n")
        f.write("=== REPORTE DE CLASIFICACIÓN ===\n")
        f.write(report_text)
        f.write("\n")

    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    fig, ax = plt.subplots(figsize=(8, 6))
    disp.plot(cmap="Blues", values_format="d", ax=ax)
    plt.title("Matriz de Confusión - Clasificación KNN")
    plt.tight_layout()
    plt.savefig("outputs/matriz_confusion.png")
    plt.close()

    print(f"Clasificación terminada. Accuracy: {acc:.4f}")
    print("\nReporte de clasificación:")
    print(report_text)