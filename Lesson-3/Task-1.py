import random

print('Для общения с компьютером используете следующие знаки: \n">" - введите это знак, если число компьютера '
      'больше чем ваше, \n"<" - введите это знак, если число компьютера меньше чем ваше, \n">" - введите это знак, '
      'если компьютер угадал ваше число.')

user_number = int(input('Загадайте число от 1 до 100 и введите его: '))
result = None
min_number = 1
mux_number = 100

while result != "=":
    number = random.randint(min_number, mux_number)
    print(f"Ваше число - {user_number}")
    print(f"Компьютер говорит число - {number}. Это правильный ответ?")
    result = input("Ваш ответ: ")
    print(number)
    if result == "<":
        mux_number = number - 1
    elif result == ">":
        min_number = number + 1

print("Компьютер угадал ваше число.")



