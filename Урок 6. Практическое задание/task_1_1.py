"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для первого скрипта



Урок 2 по алгоритмам, задание 4.
Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""
from memory_profiler import profile


def get_el(n: int):
    if n <= 1:
        return 1
    return get_el(n - 1) / 2


@profile
def recu(num: int):
    def row_sum(n: int):
        if n == 0:
            return 0
        if n % 2 == 1:
            return get_el(n) + row_sum(n - 1)
        else:
            return row_sum(n - 1) - get_el(n)
    return row_sum(num)


@profile
def cycle(num: int):
    summ = 0.0
    prev = 1.0
    for i in range(num):
        if i % 2 == 0:
            summ += prev
        else:
            summ -= prev
        prev /= 2
    return summ


if __name__ == "__main__":
    tst = 800
    print(recu(tst))
    print(cycle(tst))


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    58     19.2 MiB     19.2 MiB           1   @profile
    59                                         def recu(num: int):
    60     21.0 MiB      1.8 MiB         802       def row_sum(n: int):
    61     21.0 MiB      0.0 MiB         801           if n == 0:
    62     21.0 MiB      0.0 MiB           1               return 0
    63     21.0 MiB      0.0 MiB         800           if n % 2 == 1:
    64     21.0 MiB      0.0 MiB         400               return get_el(n) + row_sum(n - 1)
    65                                                 else:
    66     21.0 MiB      0.0 MiB         400               return row_sum(n - 1) - get_el(n)
    67     21.0 MiB      0.0 MiB           1       return row_sum(num)


0.6666666666666667


Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    70     21.0 MiB     21.0 MiB           1   @profile
    71                                         def cycle(num: int):
    72     21.0 MiB      0.0 MiB           1       summ = 0.0
    73     21.0 MiB      0.0 MiB           1       prev = 1.0
    74     21.0 MiB      0.0 MiB         801       for i in range(num):
    75     21.0 MiB      0.0 MiB         800           if i % 2 == 0:
    76     21.0 MiB      0.0 MiB         400               summ += prev
    77                                                 else:
    78     21.0 MiB      0.0 MiB         400               summ -= prev
    79     21.0 MiB      0.0 MiB         800           prev /= 2
    80     21.0 MiB      0.0 MiB           1       return summ


0.6666666666666667

Заменил рекрсию на цикл, сэкономил память
"""
