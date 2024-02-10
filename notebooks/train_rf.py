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

import sys
sys.path.append('../src')  # Agrega '../src' al PYTHONPATH

from scripts import train_model

if __name__ == "__main__":
    # Directorios de entrada y salida
    input_dir = "../data/prep"
    output_dir = "../models"

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
