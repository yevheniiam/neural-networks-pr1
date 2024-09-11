import numpy as np


def max_after_zero(x):
    # Отримуємо індекси елементів, що дорівнюють нулю
    zero_indices = np.where(x == 0)[0]

    # Якщо немає нульових елементів, повертаємо None
    if len(zero_indices) == 0:
        return None

    # Створюємо список елементів, що йдуть після нулів
    after_zero_elements = []

    for idx in zero_indices:
        if idx + 1 < len(x):  # Перевіряємо, чи є елемент після нуля
            after_zero_elements.append(x[idx + 1])

    # Якщо немає елементів після нулів, повертаємо None
    if len(after_zero_elements) == 0:
        return None

    # Повертаємо максимальний елемент після нуля
    return max(after_zero_elements)



x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
result = max_after_zero(x)
print(result)
