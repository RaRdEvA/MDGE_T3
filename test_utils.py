import pytest
from src.utils import setup_logger
import os
import logging


def test_setup_logger_creates_file():
    '''
    Prueba que setup_logger crea un archivo de log correctamente.
    '''
    logger = setup_logger("test_logger", 2)
    logger.info(f'./logs/test_logger_*.log')
    assert os.path.exists(f'./logs/test_logger_*.log')


def test_setup_logger_level_debug():
    '''
    Prueba que el logger se configura en nivel DEBUG correctamente.
    '''
    logger = setup_logger("test_debug_logger", 2)
    assert logger.level == logging.DEBUG


def test_setup_logger_level_info():
    '''
    Prueba que el logger se configura en nivel INFO correctamente.
    '''
    logger = setup_logger("test_info_logger", 1)
    assert logger.level == logging.INFO


def test_setup_logger_level_error():
    '''
    Prueba que el logger se configura en nivel ERROR correctamente.
    '''
    logger = setup_logger("test_error_logger", 3)
    assert logger.level == logging.ERROR


def test_log_file_format():
    '''
    Prueba que el archivo de log sigue el formato de nombre esperado.
    '''
    logger = setup_logger("test_format_test", 2)
    files = os.listdir('./logs')
    assert any("format_test_" in file for file in files)
