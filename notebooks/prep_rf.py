'''

Este script lee todos los achivos en la carpeta "raw" y selecciona las columnas requeridas.

El script guarda los datos preprocesados en la carpeta "prep" que se encuentra dentro de "data"

'''

import os
import sys
from scripts import preprocess_data

sys.path.append('../src')

if __name__ == "__main__":
    # Directorios de entrada y salida
    INPUT_DIR = "../data/raw"
    OUTPUT_DIR = "../data/prep"

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Listar archivos en la carpeta de entrada
    INPUT_FILES = os.listdir(INPUT_DIR)

    # Preprocesar cada archivo de entrada
    for file in INPUT_FILES:
        if file.endswith(".csv"):  # Solo procesar archivos CSV
            input_file_path = os.path.join(INPUT_DIR, file)
            output_file_path = os.path.join(OUTPUT_DIR, file)
            preprocess_data(input_file_path, output_file_path)
