"""
Напишите функцию которая принимает на вход список.
Функция создает из этого списка новый список из квадратных корней чисел (если число положительное)
и самих чисел (если число отрицательное) и возвращает результат
(желательно применить генератор и тернарный оператор при необходимости).
В результате работы функции исходный список не должен измениться.
Например:
old_list = [1, -3, 4]
result = [1, -3, 2]

Примечание: Список с целыми числами создайте вручную в начале файла.
Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.
"""

"""
def new_sqrt_list(list_input):
    list_input = copy.deepcopy(list_input)
    for i in range(len(list_input)):
        number = list_input[i]
        if number > 0:
            list_input[i] = math.sqrt(number)

    return list_input
"""

import math

numbers = [1, 2, 10, 25, 3, 54, 100, -40, -20, 24, 65, -10, -1, 0, 74, -58, 64, 35, -36]


def new_sqrt_list(list_input):
    result = [math.sqrt(number)if number > 0 else number for number in list_input]
    return result


result = new_sqrt_list(numbers)
print(result)
print(numbers)

