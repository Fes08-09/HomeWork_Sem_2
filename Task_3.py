# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

# Пример:

# Для n = 6 -> 14.072


n = int(input('Введите число n: ')) 


def get_squerence(n):
    return [round((1 + 1 / i) ** i, 4) for i in range (1, n + 1)]


nums = get_squerence(n)
print(round(sum(nums), 3))
