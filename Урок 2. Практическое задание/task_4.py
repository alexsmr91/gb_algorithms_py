"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def get_el(n: int):
    if n <= 1:
        return 1
    return get_el(n - 1) / 2


def row_sum(n: int):
    if n == 0:
        return 0
    if n % 2 == 1:
        return get_el(n) + row_sum(n - 1)
    else:
        return row_sum(n - 1) - get_el(n)


if __name__ == "__main__":
    tst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 51, 52, 53, 54, 55, 56, 57]
    for ts in tst:
        print(row_sum(ts))
