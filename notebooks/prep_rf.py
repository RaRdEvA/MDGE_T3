
'''
Este script lee todos los achivos en la carpeta "raw"  y selecciona las columnas requeridas para el análisis.

Después de seleccionar las columnas requeridas, el script guarda los datos preprocesados en la carpeta "prep" que se encuentra dentro de "data".
'''

import pandas as pd
import os

import sys
sys.path.append('../src')  # Agrega '../src' al PYTHONPATH

from scripts import preprocess_data

if __name__ == "__main__":
    # Directorios de entrada y salida
    input_dir = "../data/raw"
    output_dir = "../data/prep"

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Listar archivos en la carpeta de entrada
    input_files = os.listdir(input_dir)

    # Preprocesar cada archivo de entrada
    for file in input_files:
        if file.endswith(".csv"):  # Solo procesar archivos CSV
            input_file_path = os.path.join(input_dir, file)
            output_file_path = os.path.join(output_dir, file)
            preprocess_data(input_file_path, output_file_path)
