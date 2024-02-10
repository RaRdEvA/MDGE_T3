# scripts.py

import pandas as pd
import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def preprocess_data(input_file, output_file):
    # Leer el archivo CSV de entrada
    data = pd.read_csv(input_file)

    # Determinar si el archivo tiene la columna 'SalePrice'
    has_sale_price_column = 'SalePrice' in data.columns

    # Seleccionar las columnas requeridas
    selected_columns = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF']
    if has_sale_price_column:
        selected_columns.append('SalePrice')

    # Completar valores faltantes (NaN) y en blanco con la media de cada columna
    for column in selected_columns:
        data[column].fillna(data[column].mean(), inplace=True)

    preprocessed_data = data[selected_columns]

    # Guardar el resultado en un nuevo archivo CSV
    preprocessed_data.to_csv(output_file, index=False)

    print(f"Datos preprocesados guardados en {output_file}")

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

def perform_inference(input_dir, model_path, output_dir):
    # Cargar el modelo entrenado
    model = joblib.load(model_path)

    # Listar archivos en la carpeta de entrada
    input_files = os.listdir(input_dir)

    # Realizar predicciones para cada archivo en la carpeta de entrada
    for file in input_files:
        if file.endswith(".csv"):  # Solo procesar archivos CSV
            input_file_path = os.path.join(input_dir, file)
            output_file_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}_predictions.csv")

            # Leer datos de entrada
            data = pd.read_csv(input_file_path)

            # Realizar predicciones
            predictions = model.predict(data)

            # Guardar predicciones en archivo CSV
            pd.DataFrame(predictions).to_csv(output_file_path, index=False, header=["Predicted_SalePrice"])
            print(f"Predicciones guardadas en {output_file_path}")
