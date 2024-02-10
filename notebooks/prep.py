
'''
Este script lee todos los achivos en la carpeta "raw" que se encuentra dentro de "data" y selecciona las columnas requeridas para el análisis.

Después de seleccionar las columnas requeridas, el script guarda los datos preprocesados en la carpeta "prep" que se encuentra dentro de "data".
'''

import pandas as pd
import os

def preprocess_data(input_file, output_file):
    # Leer el archivo CSV de entrada
    data = pd.read_csv(input_file)

    # Determinar si el archivo tiene la columna 'SalePrice'
    has_sale_price_column = 'SalePrice' in data.columns

    # Seleccionar las columnas requeridas
    selected_columns = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF']
    if has_sale_price_column:
        selected_columns.append('SalePrice')

    preprocessed_data = data[selected_columns]

    # Guardar el resultado en un nuevo archivo CSV
    preprocessed_data.to_csv(output_file, index=False)

    print(f"Datos preprocesados guardados en {output_file}")

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
