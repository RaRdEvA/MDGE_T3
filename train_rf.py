'''
Este script entrena un modelo de regresión lineal
para predecir el precio de venta de casas en Ames, Iowa,
utilizando datos de entrada en formato CSV.

El modelo entrenado se guarda en un archivo .joblib
en la carpeta de salida.
'''

import os
import argparse
from src.scripts import train_model, load_config
from datetime import datetime
from src.utils import setup_logger

# Configuración del logger
now = datetime.now()
date_time = now.strftime("%Y%m%d-%H%M%S")
logger = setup_logger('training', f'logs/training_{date_time}.log', log_level=2)

# Definimos y parseamos los argumentos de entrada
parser = argparse.ArgumentParser(description='Entrena un modelo utilizando datos preprocesados y guarda el modelo entrenado.')
parser.add_argument('--input_dir', type=str, default='./data/prep', help='Directorio de los archivos de entrada preprocesados.')
parser.add_argument('--output_dir', type=str, default='./models', help='Directorio para guardar los modelos entrenados.')
parser.add_argument('--config_path', type=str, default='./config.yaml', help='Ruta al archivo de configuración del modelo.')
args = parser.parse_args()

if __name__ == "__main__":
    # Usamos los argumentos para los directorios de entrada y salida, y la ruta del archivo de configuración
    INPUT_DIR = args.input_dir
    OUTPUT_DIR = args.output_dir
    CONFIG_PATH = args.config_path

    logger.info("Iniciando el proceso de entrenamiento del modelo")

    # Cargar la configuración utilizando load_config importada
    config = load_config(CONFIG_PATH)

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Listar archivos en la carpeta de entrada
    INPUT_FILES = os.listdir(INPUT_DIR)

    # Entrenar el modelo para cada archivo .csv en la carpeta de entrada
    for file in INPUT_FILES:
        if file.endswith(".csv"):
            input_file_path = os.path.join(INPUT_DIR, file)
            try:
                train_model(input_file_path, OUTPUT_DIR, config)
                logger.info(f"Modelo entrenado y guardado exitosamente para {file}")
            except Exception as e:
                logger.error(f"Error al entrenar el modelo para {file}", exc_info=True)
