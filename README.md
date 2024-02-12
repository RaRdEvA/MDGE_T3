# MDGE_T3

## Descripción

Este repositorio contiene la tarea 3 de la materia de Métodos de Gran Escala. 2024-1.

## Árbol del repositorio

El repositorio está organizado de la siguiente forma:

```bash
.
├── README.md
├── data
│   ├── inference
│   │   └── test.csv
│   ├── predictions
│   │   └── test_predictions.csv
│   ├── prep
│   │   ├── test.csv
│   │   └── train.csv
│   ├── raw
│   │   ├── test.csv
│   │   └── train.csv
│   ├── test.csv
│   └── train.csv
├── inference.py
├── inference_rf.py
├── models
│   └── train_model.joblib
├── notebooks
│   └── Tarea_01_MDGE_169589_Javier_Castillo_Millan.ipynb
├── prep.py
├── prep_rf.py
├── src
│   ├── __pycache__
│   │   └── scripts.cpython-38.pyc
│   └── scripts.py
├── train.py
└── train_rf.py

9 directories, 19 files
```

## Contenido

### root

- [README.md](README.md)
  - Este archivo.
- [inference.py](inference.py)
  - Script que realiza la inferencia con el modelo entrenado y los datos de prueba.
  - La salida se guarda en la carpeta predictions.
- [inference_rf.py](inference_rf.py)
  - Versión refactorizada del script [inference.py](inference.py).
- [prep.py](prep.py)
  - Script que realiza el preprocesamiento de los datos de entrenamiento y prueba.
  - La salida se guarda en la carpeta prep.
- [prep_rf.py](prep_rf.py)
  - Versión refactorizada del script [prep.py](prep.py).
- [train.py](train.py)
  - Script que realiza el entrenamiento del modelo.
  - La salida se guarda en la carpeta models.
  - Este script es el que se usó para entrenar el modelo que se encuentra en la carpeta models.
- [train_rf.py](train_rf.py)
  - Versión refactorizada del script [train.py](train.py).

### data

- Inference
  - Contiene los archivos que se usan para ejecutar la inferencia con el script del mismo nombre [inference.py](inference.py).
- predictions
  - Contiene el resultado de la inferemcia después de ejecutar el script de inferencia. Guarda un resultado por cada archivo que haya sido enviado a inferencia usando [inference.py](inference.py)
- prep
  - Aquí se almacenan los datos resultados del preprocesamiento con el script de preprocesamiento [prep.py](prep.py).
- raw
  - Estos son los datos que toma el script de preprocesamiento [prep.py](prep.py) para generar los datos en la carpeta prep.
- [test.csv](data/test.csv)
  - Este archivo es el original provisto por la competencia de kaggle y se usa para realizar la inferencia. También se usa como insumo para los scripts de la tarea.
- [train.csv](data/train.csv)
  - Este archivo es el original provisto por la competencia de kaggle y se usa para realizar el entrenamiento. Tambien se usa como insumo para los scripts de la tarea.

### models

Aquí se almacenan los modelos entrenados.

### notebooks

- Se encuentra el archivo [Tarea_01_MDGE_169589_Javier_Castillo_Millan.ipynb](Tarea_01_MDGE_169589_Javier_Castillo_Millan.ipynb) que contiene el desarrollo de la tarea 1, contiene un análisis exploratorio y el entrenamiento; lo cual, sirvió como fundamento para crear este repositorio y sus funcionalidades.

### src

- [scripts.py](src/scripts.py)
  - Contiene las funciones que se usan en los scripts de la carpeta notebooks.
  - Esto se hizo con la intención de ejecutar refactorización de código y modularizar el código. Tal cual se pidió en las instrucciones de la tarea.

## Refactorización

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![linting: flake8](https://img.shields.io/badge/linting-flake8-yellowgreen)](https://flake8.pycqa.org/en/latest/)

Uno de los requisitos de la tarea fue la ejecución de linting con pylint y flake8.

El resultado de la ejecución de ambos sobre los scripts de Python mostró todos los códigos refactorizados con 10 de 10 de calificación en Pylint y sin mensajes en Flake8.

El resultado fue el siguiente:

```bash
xxx@xxx.xxx@vmMDGE:~/MDGE/MDGE_T3$ pylint prep_rf.py; pylint train_rf.py; pylint inference_rf.py; pylint ./src/scripts.py 

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

xxx@xxx.xxx@vmMDGE:~/MDGE/MDGE_T3$ flake8 prep_rf.py; flake8 train_rf.py; flake8 inference_rf.py; flake8 ./src/scripts.py 
xxx@xxx.xxx@vmMDGE:~/MDGE/MDGE_T3$ 
```

En la siguiente imagen podemos apreciar la evidencia:

![linting](lint_proof.png)

## Tarea solicitada

Las instrucciones de la tarea que llevó a la construcción de este repositorio son las siguientes:

### Tarea 03

En el capítulo 4 aprendiste sobre la importancia de escribir código limpio cuando tengas que crear un producto de datos. Cuando estas construyendo un proyecto de data science, la idea es comenzar con un notebook para prototipar rápido, experimentar cosas, cuando estes listo puedes extraer el código y ponerlo en un script. Recuerda que es importante documentar el código siguiendo las prácticas que vimos.

#### Objetivo

Toma el código de tu tarea anterior y conviertelo en un repositorio, utilizando las mejores prácticas que revisamos para escribir código limpio.

#### Entregables

Un repositorio público en Github.

#### Puntos que deberás cubrir

- Crea la estructura del repositorio (revisa la estructura propuesta en clase).
- Tu notebook o notebooks, los puedes guardar en un directorio que se llame notebooks.
- Tus datos guardalos una carpeta que se llama data. Sigue las recomendaciones de la clase. Recuerda modificar el path de la data en tus notebooks para que puedan correr.
- Vas a convertir tu notebook en un conjunto de scriptps que vas a guardar en el root del repo.
- prep.py: La entrada del script son datos data/raw. La salida del script son datos prep.
- train.py: La entrada del script son datos data/prep. La salida del script es un modelo entrenado. Puedes checar el código de este blog Save and Load Machine Learning Models in Python with scikit-learn
- inference.py: La entrada de este script son datos data/inference y el modelo entrenado model.joblib. La salida de este modelo son predicciones en batch que se guardan en data/predictions.
- Haz un refactor de tu código.
- crea un directorio src y ahi crea módulos (scripts.py) con funciones que luego puedas importar a tu código principal (prep.py, train.py, inference.py) que se encuentra en el root.
- utiliza Docstrings en los módulos y las funciones. Revisa esta sección del blog que mostré en clase.
- utiliza Docstrings e Inline comments en las funciones (sigue la propuesta de la clase).
- Optimiza el código redundante en loops y funciones.
- puedes revisar este blog para llevar tus funciones a un siguiente nivel Defining Your Own Python Function
- Documenta tu repositorio con un README.
- Agrega un arbol con la estructura de tu repositorio. Checa esta documentación Tree command in Linux with examples.
- Aplica unos linters a tu código.
- Aplica el pylint a tu script y trata de obetener una calificación de 10/10.
- Aplica flake8 a tu script y busca no tener ningún error.
- Hay que estirarse para llegar a la meta =).

#### Deadline

Miércoles 14 de febrero via Canvas.
