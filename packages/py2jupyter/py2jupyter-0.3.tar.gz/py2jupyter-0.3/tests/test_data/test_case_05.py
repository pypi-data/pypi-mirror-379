""" # Тест разделения кода # """

"""Этот тест проверяет разделение кода на ячейки по пустым строкам."""

# Группа импортов
import os
import sys
import json

# Настройка
DEBUG = True
MAX_RETRIES = 3


def first_function():
    """Первая функция"""
    return "first"


def second_function():
    """Вторая функция"""
    return "second"


# Тестовый код
if __name__ == "__main__":
    print(first_function())
    print(second_function())
