import logging
from datetime import datetime
import os

def setup_logger(name, log_file, log_level=2):
    '''
    Función para configurar y obtener un logger.
    Args:
    name: str, el nombre del logger.
    log_file: str, la ruta al archivo de log.
    log_level: int, el nivel de log deseado:
        - 1 para INFO
        - 2 para DEBUG
        - 3 para ERROR
        Default a DEBUG si no se especifica
    '''
    # Mapeo del nivel de log numérico a logging level
    level_dict = {
        1: logging.INFO,
        2: logging.DEBUG,
        3: logging.ERROR,
    }

    level = level_dict.get(log_level, logging.DEBUG) 

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    handler = logging.FileHandler(log_file, mode='w')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
