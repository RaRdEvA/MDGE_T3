'''
Este código se encarga de realizar la inferencia de un modelo
entrenado en un conjunto de datos de entrada.

Consta de la definición de una función que toma como argumentos
los directorios de entrada y salida, así como el path del modelo entrenado.

Posteriormente ejecuta la inferencia para cada archivo
que se encuentre presente en la carpeta de entrada,
guardando las predicciones en la carpeta de salida.
'''

import os
import sys
sys.path.append('../src')  # Agrega '../src' al PYTHONPATH
from scripts import perform_inference

# Ejecución de la inferencia
if __name__ == "__main__":
    # Directorios de entrada y salida
    INPUT_DIR = "../data/inference"
    MODEL_PATH = "../models/train_model.joblib"  # Cambiar a train_model.joblib
    OUTPUT_DIR = "../data/predictions"

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Realizar inferencia para los archivos de la carpeta de entrada
    perform_inference(INPUT_DIR, MODEL_PATH, OUTPUT_DIR)
