'''
Este módulo provee las funciones que
son usadas en los scripts de ejecución de:
- Preprocesamiento de datos
- Entrenamiento de modelos
- Inferencia
Consta de 3 funciones que cubren las tareas mencionadas
'''

import yaml
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib
from src.utils import setup_logger
from datetime import datetime

# Configuración de loggers individuales
now = datetime.now()
date_time = now.strftime("%Y%m%d-%H%M%S")
info_logger = setup_logger('info_', f'logs/info_{date_time}.log', log_level=1)
debug_logger = setup_logger('debug_', f'logs/debug_{date_time}.log', log_level=2)
error_logger = setup_logger('error_', f'logs/error_{date_time}.log', log_level=3)

def load_config(config_path):
    '''
    Función para cargar la configuración desde el archivo YAML.

    Args:
    config_path: str, path del archivo de configuración.

    Returns:
    dict, la configuración cargada desde el archivo YAML.

    '''
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        # Usando info_logger para registrar la carga exitosa de la configuración
        info_logger.info(f"Configuración cargada exitosamente desde {config_path}")
        return config
    except Exception as e:
        # Usando error_logger para registrar errores al cargar la configuración
        error_logger.error("Error al cargar la configuración", exc_info=True)
        return None


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
    try:
        # Leer el archivo CSV de entrada
        debug_logger.info(f"Iniciando preprocesamiento de datos desde {input_file}")
        data = pd.read_csv(input_file)
        debug_logger.debug(f"Datos cargados desde {input_file} con {data.shape[0]} filas y {data.shape[1]} columnas")

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

        # Completar valores faltantes (NaN y blank) con la media
        for column in selected_columns:
            data[column].fillna(data[column].mean(), inplace=True)

        preprocessed_data = data[selected_columns]

        # Guardar el resultado en un nuevo archivo CSV
        preprocessed_data.to_csv(output_file, index=False)
        info_logger.info(f"Datos preprocesados guardados en {output_file}")
    except Exception as e:
        error_logger.error(f"Error en el preprocesamiento de datos para {input_file}", exc_info=True)


def train_model(input_file, output_dir, config):
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
    try:
        # Leer el archivo CSV de entrada
        debug_logger.info(f"Iniciando entrenamiento del modelo con datos de {input_file}")
        data = pd.read_csv(input_file)
        debug_logger.debug(f"Datos de entrenamiento cargados desde {input_file} con {data.shape[0]} filas y {data.shape[1]} columnas")

        # Separar features (x) y variable objetivo (y) según la configuración
        features = config['model']['features']
        x = data[features]
        y = data['SalePrice']

        # Dividir en sets train y test usando la configuración
        test_size = config['data_split']['test_size']
        random_state = config['data_split']['random_state']
        x_train, x_test, y_train, y_test = train_test_split(x,
                                                            y,
                                                            test_size=test_size,
                                                            random_state=random_state)

        # Entrenar modelo de regresión lineal
        model = LinearRegression()
        model.fit(x_train, y_train)

        # Predecir en el test set y calcular error
        y_pred = model.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)
        debug_logger.debug(f"Error cuadrático medio en conjunto de prueba: {mse}")

        # Guardar el modelo entrenado
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        model_path = os.path.join(output_dir,
                                  f"model_{datetime.now().strftime('%Y%m%d-%H%M%S')}.joblib")
        joblib.dump(model, model_path)
        info_logger.info(f"Modelo entrenado guardado en {model_path}")
    except Exception as e:
        error_logger.error("Error al entrenar el modelo", exc_info=True)


def perform_inference(input_dir, model_path, output_dir):
    '''
    Esta función realiza inferencia con un modelo
    entrenado y datos de entrada en formato CSV.
    Guarda las predicciones en unarchivo CSV en la carpeta de salida.

    Args:
    input_dir: str, path de la carpeta de entrada
    model_path: str, path del modelo entrenado
    output_dir: str, path de la carpeta de salida

    Returns:
    None

    '''
    try:
        # Cargar el modelo entrenado
        info_logger.info(f"Cargando modelo para inferencia desde {model_path}")
        model = joblib.load(model_path)

        # Crear carpeta de salida si no existe
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Archivos en la carpeta de entrada
        input_files = os.listdir(input_dir)

        # Realizar predicciones para cada archivo en la carpeta
        for file in input_files:
            if file.endswith(".csv"):
                input_file_path = os.path.join(input_dir, file)
                output_file_path = os.path.join(output_dir,
                                                f"{os.path.splitext(file)[0]}_predictions.csv")

                # Leer datos de entrada
                debug_logger.info(f"Realizando inferencia para {input_file_path}")
                data = pd.read_csv(input_file_path)

                # Realizar predicciones
                predictions = model.predict(data)

                # Guardar predicciones en archivo CSV
                pd.DataFrame(predictions).to_csv(output_file_path, index=False, header=["Predicted_SalePrice"])
                info_logger.info(f"Predicciones guardadas en {output_file_path}")
    except Exception as e:
        error_logger.error("Error al realizar inferencia", exc_info=True)
