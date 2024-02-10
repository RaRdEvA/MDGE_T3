'''
Este código se encarga de realizar la inferencia de un modelo entrenado en un conjunto de datos de entrada.

Consta de la definición de una función que toma como argumentos los directorios de entrada y salida, así como el path del modelo entrenado.

Posteriormente ejecuta la inferencia para cada archivo en la carpeta de entrada, guardando las predicciones en la carpeta de salida.
'''

import os
import joblib
import pandas as pd

import sys
sys.path.append('../src')  # Agrega '../src' al PYTHONPATH

from scripts import perform_inference

# Ejecución de la inferencia
if __name__ == "__main__":
    # Directorios de entrada y salida
    input_dir = "../data/inference"
    model_path = "../models/train_model.joblib"  # Cambiar a train_model.joblib
    output_dir = "../data/predictions"

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Realizar inferencia para los archivos de la carpeta de entrada
    perform_inference(input_dir, model_path, output_dir)
