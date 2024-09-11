import numpy as np


def closest_element(matrix, v):
    # Обчислюємо різницю між кожним елементом матриці та v
    diff = np.abs(matrix - v)

    # Знаходимо індекс мінімальної різниці
    idx = np.argmin(diff)

    # Повертаємо елемент матриці, який найближчий до v
    return matrix.flat[idx]


# Приклад використання
X = np.arange(0, 10).reshape((2, 5))
v = 3.6
result = closest_element(X, v)
print(result)
