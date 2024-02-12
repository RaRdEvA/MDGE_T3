'''
Este módulo provee las funciones que
son usadas en los scripts de ejecución de:
- Preprocesamiento de datos
- Entrenamiento de modelos
- Inferencia
Consta de 3 funciones que cubren las tareas mencionadas
'''

import os
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def preprocess_data(input_file, output_file):

    '''
    Esta función toma archivos de la carpeta y los preprocesa
    Toma solamente las variables que se usan para entrenamiento
    También identifica si contiene la variable objetivo
    Rellena los na y los valores en blanco con la media de cada columna
    Guarda el resultado en un nuevo archivo CSV

    Args:
    input_file: str, path del archivo de entrada
    output_file: str, path del archivo de salida

    Returns:
    None

    '''

    # Leer el archivo CSV de entrada
    data = pd.read_csv(input_file)

    # Determinar si el archivo tiene la columna 'SalePrice'
    has_sale_price_column = 'SalePrice' in data.columns

    # Seleccionar las columnas requeridas
    selected_columns = ['OverallQual',
                        'GrLivArea',
                        'GarageCars',
                        'GarageArea',
                        'TotalBsmtSF',
                        '1stFlrSF']

    if has_sale_price_column:
        selected_columns.append('SalePrice')

    # Completar valores faltantes (NaN y blank) con la media de la columna
    for column in selected_columns:
        data[column].fillna(data[column].mean(), inplace=True)

    preprocessed_data = data[selected_columns]

    # Guardar el resultado en un nuevo archivo CSV
    preprocessed_data.to_csv(output_file, index=False)

    print(f"Datos preprocesados guardados en {output_file}")


def train_model(input_file, output_dir):

    '''
    Esta función entrena un modelo de regresión lineal
    para predecir el precio de venta de casas en Ames,
    Iowa, utilizando datos de entrada en formato CSV.
    El modelo entrenado se guarda en un archivo .joblib
    en la carpeta de salida.

    Args:
    input_file: str, path del archivo de entrada
    output_dir: str, path de la carpeta de salida

    Returns:
    None

    '''

    # Leer el archivo CSV de entrada
    data = pd.read_csv(input_file)

    # Separar features (x) y variable objetivo (y)
    x = data[['OverallQual',
              'GrLivArea',
              'GarageCars',
              'GarageArea',
               'TotalBsmtSF',
               '1stFlrSF']]
    y = data['SalePrice']

    # Dividir en sets train y test
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=42)

    # Entrenar modelo de regresión lineal
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Predecir en el test set y calcular error
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Error cuadrático medio en conjunto de prueba: {mse}")

    # Guardar el modelo entrenado
    filename = os.path.splitext(os.path.basename(input_file))[0]
    model_path = os.path.join(output_dir, f"{filename}_model.joblib")
    joblib.dump(model, model_path)
    print(f"Modelo entrenado guardado en {model_path}")


def perform_inference(input_dir, model_path, output_dir):

    '''
    Esta función realiza inferencia con un modelo
    entrenado y datos de entrada en formato CSV.
    Guarda las predicciones en un archivo CSV
    en la carpeta de salida.

    Args:
    input_dir: str, path de la carpeta de entrada
    model_path: str, path del modelo entrenado
    output_dir: str, path de la carpeta de salida

    Returns:
    None

    '''

    # Cargar el modelo entrenado
    model = joblib.load(model_path)

    # Listar archivos en la carpeta de entrada
    input_files = os.listdir(input_dir)

    # Realizar predicciones para cada archivo en la carpeta
    for file in input_files:
        if file.endswith(".csv"):  # Solo procesar archivos CSV
            input_file_path = os.path.join(input_dir, file)
            output_file_path = os.path.join(
                output_dir,
                f"{os.path.splitext(file)[0]}_predictions.csv")

            # Leer datos de entrada
            data = pd.read_csv(input_file_path)

            # Realizar predicciones
            predictions = model.predict(data)

            # Guardar predicciones en archivo CSV
            pd.DataFrame(predictions).to_csv(output_file_path,
                                             index=False,
                                             header=["Predicted_SalePrice"])
            print(f"Predicciones guardadas en {output_file_path}")
