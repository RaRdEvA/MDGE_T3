'''
- Este script lee todos los achivos en la carpeta "raw".
- Para cada uno selecciona las columnas requeridas.
- Para cada uno guarda los datos preprocesados en la carpeta "prep".
'''

import os
import argparse
from src.scripts import preprocess_data
from datetime import datetime
from src.utils import setup_logger

# Configuración del logger
now = datetime.now()
date_time = now.strftime("%Y%m%d-%H%M%S")
logger = setup_logger('preprocessing', f'logs/preprocessing_{date_time}.log', log_level=2)

# Definimos y parseamos los argumentos de entrada
parser = argparse.ArgumentParser(description='Preprocesa archivos CSV desde una carpeta de entrada y los guarda en una carpeta de salida.')
parser.add_argument('--input_dir', type=str, default='./data/raw', help='Directorio de los archivos de entrada.')
parser.add_argument('--output_dir', type=str, default='./data/prep', help='Directorio para guardar los archivos preprocesados.')
args = parser.parse_args()


if __name__ == "__main__":
    # Usamos los argumentos para los directorios de entrada y salida
    INPUT_DIR = args.input_dir
    OUTPUT_DIR = args.output_dir

    logger.info("Iniciando el proceso de preprocesamiento")

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        logger.debug(f"Carpeta de salida {OUTPUT_DIR} creada")

    # Listar archivos en la carpeta de entrada
    INPUT_FILES = os.listdir(INPUT_DIR)

    # Preprocesar cada archivo de entrada
    for file in INPUT_FILES:
        if file.endswith(".csv"):  # Solo procesar archivos CSV
            input_file_path = os.path.join(INPUT_DIR, file)
            output_file_path = os.path.join(OUTPUT_DIR, file)
            logger.debug(f"Preprocesando {input_file_path}")
            try:
                preprocess_data(input_file_path, output_file_path)
                logger.info(f"Archivo preprocesado guardado en {output_file_path}")
            except Exception as e:
                logger.error(f"Error al preprocesar {input_file_path}", exc_info=True)
