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
import argparse
from src.scripts import perform_inference

# Definimos y parseamos los argumentos de entrada
parser = argparse.ArgumentParser(description='Realiza la inferencia utilizando un modelo entrenado y guarda las predicciones.')
parser.add_argument('--input_dir', type=str, default='./data/inference', help='Directorio de los archivos de entrada para inferencia.')
parser.add_argument('--model_path', type=str, default='./models/train_model.joblib', help='Ruta al modelo entrenado para usar en la inferencia.')
parser.add_argument('--output_dir', type=str, default='./data/predictions', help='Directorio para guardar las predicciones.')
args = parser.parse_args()

# Ejecución de la inferencia
if __name__ == "__main__":
    # Usamos los argumentos para los directorios de entrada y salida, y la ruta del modelo
    INPUT_DIR = args.input_dir
    MODEL_PATH = args.model_path
    OUTPUT_DIR = args.output_dir

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Ejecución de la inferencia
    perform_inference(INPUT_DIR, MODEL_PATH, OUTPUT_DIR)
