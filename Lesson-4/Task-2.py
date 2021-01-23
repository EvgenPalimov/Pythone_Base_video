"""
Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
"""

def max_number():
  user_answer = input("Введите числа через пробел: ")
  my_list = []
  for el in range(user_answer.count(" ") + 1):
    my_list = user_answer.split()

  result = max(my_list)
  return result

print(max_number())