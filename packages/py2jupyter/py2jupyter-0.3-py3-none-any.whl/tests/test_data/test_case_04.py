""" # Тест magic и shell команд # """

"""Этот тест проверяет обработку magic и shell команд."""

#> %matplotlib inline
#> %config InlineBackend.figure_format = 'retina'

import matplotlib.pyplot as plt
import numpy as np

def plot_data():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

#> !echo "Hello from shell"

# Выполняем функцию
if __name__ == "__main__":
    plot_data()
