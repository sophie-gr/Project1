import functools
n = input('Введите натуральное число: ')
n = [int(digit) for digit in n]

summa = sum(n)
print('Сумма цифр данного числа: ', summa)

