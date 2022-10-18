# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

N = int(input('Введите число N '))
numbers = []

for i in range(N*2 + 1):
    numbers.append(-N + i)
print(numbers)

a = int(input('Введите позицию первого элемента: '))
b = int(input('Введите позицию второго элемента: '))
mult = 1

for i in range(len(numbers)):
    mult = numbers[a - 1] * numbers[b - 1]
print(f'Произведение элементов: {numbers[a - 1]} * {numbers[b - 1]} = {mult}')