'''
Este script entrena un modelo de regresión lineal
para predecir el precio de venta de casas en Ames, Iowa,
utilizando datos de entrada en formato CSV.

El modelo entrenado se guarda en un archivo .joblib
en la carpeta de salida.
'''

import os
import sys
sys.path.append('../src')  # Agrega '../src' al PYTHONPATH

from scripts import train_model

if __name__ == "__main__":
    # Directorios de entrada y salida
    INPUT_DIR = "../data/prep"
    OUTPUT_DIR = "../models"

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Listar archivos en la carpeta de entrada
    input_files = os.listdir(INPUT_DIR)

    # Entrenar el modelo para cada archivo .csv en la carpeta de entrada
    for file in input_files:
        if file.endswith(".csv"):  # Solo procesar archivos CSV
            input_file_path = os.path.join(INPUT_DIR, file)
            train_model(input_file_path, OUTPUT_DIR)
