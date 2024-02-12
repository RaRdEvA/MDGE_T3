'''
ESte script entrena un modelo de regresión lineal para predecir el precio de venta de casas en Ames, Iowa, utilizando datos de entrada en formato CSV.

El modelo entrenado se guarda en un archivo .joblib en la carpeta de salida.
'''

import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_model(input_file, output_dir):
    # Leer el archivo CSV de entrada
    data = pd.read_csv(input_file)

    # Separar características (X) y variable objetivo (y)
    X = data[['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF']]
    y = data['SalePrice']

    # Dividir datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predecir en el conjunto de prueba y calcular error
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Error cuadrático medio en conjunto de prueba: {mse}")

    # Guardar el modelo entrenado
    filename = os.path.splitext(os.path.basename(input_file))[0]  # Nombre del archivo sin extensión
    model_path = os.path.join(output_dir, f"{filename}_model.joblib")
    joblib.dump(model, model_path)
    print(f"Modelo entrenado guardado en {model_path}")

if __name__ == "__main__":
    # Directorios de entrada y salida
    input_dir = "./data/prep"
    output_dir = "./models"

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Listar archivos en la carpeta de entrada
    input_files = os.listdir(input_dir)

    # Entrenar el modelo para cada archivo .csv en la carpeta de entrada
    for file in input_files:
        if file.endswith(".csv"):  # Solo procesar archivos CSV
            input_file_path = os.path.join(input_dir, file)
            train_model(input_file_path, output_dir)
