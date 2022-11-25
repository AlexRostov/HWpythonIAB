# Задайте список из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
#     *Пример:*
#
#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 36.9}

n = int(input('Введите количество чисел в списке '))

def numbers(n):
    summ = 0
    for i in range(n):
        a = float(input(f'Введи число {i + 1} '))
        a = (1+1/a)**a
        summ = a + summ
        i += 1
    return summ

print('Сумма чисел равна', round((numbers(n)), 2))