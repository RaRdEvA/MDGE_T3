import os
import joblib
import pandas as pd

def perform_inference(input_dir, model_path, output_dir):
    # Cargar el modelo entrenado
    model = joblib.load(model_path)

    # Listar archivos en la carpeta de entrada
    input_files = os.listdir(input_dir)

    # Realizar predicciones para cada archivo en la carpeta de entrada
    for file in input_files:
        if file.endswith(".csv"):  # Solo procesar archivos CSV
            input_file_path = os.path.join(input_dir, file)
            output_file_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}_predictions.csv")

            # Leer datos de entrada
            data = pd.read_csv(input_file_path)

            # Realizar predicciones
            predictions = model.predict(data)

            # Guardar predicciones en archivo CSV
            pd.DataFrame(predictions).to_csv(output_file_path, index=False, header=["Predicted_SalePrice"])
            print(f"Predicciones guardadas en {output_file_path}")

if __name__ == "__main__":
    # Directorios de entrada y salida
    input_dir = "../data/inference"
    model_path = "../models/train_model.joblib"
    output_dir = "../data/predictions"

    # Asegurarse de que la carpeta de salida exista, si no, crearla
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Realizar inferencia para los archivos de la carpeta de entrada
    perform_inference(input_dir, model_path, output_dir)
