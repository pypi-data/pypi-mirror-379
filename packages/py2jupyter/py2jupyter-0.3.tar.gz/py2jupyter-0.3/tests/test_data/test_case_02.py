""" # Тест функций и классов # """

"""Этот файл тестирует конвертацию функций и классов в отдельные ячейки."""

import math

def calculate_area(radius):
    """Вычисляет площадь круга"""
    return math.pi * radius ** 2

class Circle:
    """Класс для работы с кругами"""

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return calculate_area(self.radius)

# Тестовый код
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Area: {circle.get_area()}")
