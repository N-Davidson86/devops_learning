#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Скрипт для проверки размера директории.
Использование: ./check_disk.py /path/to/dir --limit 1.0
"""


import os
import sys
import subprocess
import argparse
import logging

def setup_logging():
    """
    Настраивает логирование.
    Возвращает logger.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('disk_check.log'),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger('DiskChecker')
    return logger
    
def parse_args():
    """
    Парсит аргументы командной строки.
    Возвращает args.
    """    
    parser = argparse.ArgumentParser(description='Проверка размера директории')
    parser.add_argument('path', type=str, help='Путь к директории')
    parser.add_argument('--limit', type=float, default=1.0, help='limit at GB')
    args = parser.parse_args()
    return args

def parse_size(size_str):
    if 'G' in size_str:
        return float(size_str.replace('G', ''))
    elif 'M' in size_str:
        return float(size_str.replace('M', '')) / 1024
    elif 'K' in size_str:
        return float(size_str.replace('K', '')) / (1024 * 1024)
    else:
        return 0.0

def check_disk_size(path, limit_gb, logger):
#1. Проверяем, существует ли путь
    if not os.path.exists(path):
        logger.error(f"Ошибка: такой путь не существует: {path}")
        sys.exit(1)

# 2. Запусти du -sh с try/exept
    try:
        result = subprocess.run(['du', '-sh', path], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка выполнения du: {e.stderr}")
        sys.exit(1)

# 3. Извлеки размер из вывода
    size_str = result.stdout.strip().split()[0] #"1.5G"

# 4. Преобразование в ГБ
    size_gb = parse_size(size_str)

# 5. Сравнение с лимитом
    if size_gb > limit_gb:
        logger.warning(f"ВНИМАНИЕ! Размер {size_gb:.2f} ГБ превышает лимит {limit_gb} ГБ")
    else:
        logger.info(f"Размер {size_gb:.2f} ГБ в пределах нормы")

if __name__ == '__main__':
    logger = setup_logging()
    args = parse_args()
    check_disk_size(args.path, args.limit, logger)

