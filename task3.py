import numpy as np


def scale_columns(matrix):
    # Створюємо копію матриці, щоб не змінювати початкову
    scaled_matrix = matrix.copy().astype(float)

    # Проходимо по кожному стовпцю
    for col in range(scaled_matrix.shape[1]):
        max_value = np.max(scaled_matrix[:, col])

        # Перевіряємо, чи максимальне значення не дорівнює 0
        if max_value != 0:
            scaled_matrix[:, col] /= max_value
        else:
            print(f"Попередження: у стовпці {col} максимальний елемент дорівнює 0.")

    return scaled_matrix


# Приклад використання
X = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 0]])
scaled_X = scale_columns(X)
print(scaled_X)
