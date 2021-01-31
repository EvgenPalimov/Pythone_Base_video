import random

def game():
    number = random.randint(1, 100)
    user_number = None
    count = 0
    levels = {1: 10, 2: 5, 3: 3}

    level = int(input("Выбирите уровень сложности. \nУровень - 1: 10 попыток, \nУровень - 2: 5 попыток,"
                      " \nУровень - 3: 3 попытки. \nВведите желаемый уровень: "))
    max_count = levels[level]

    user_count = int(input("Введите количество пользователей: "))
    users = []
    for i in range(user_count):
        i += 1
        user_name = input(f"Введите имя пользователя - {i}: ")
        users.append(user_name)

    print(f"Список игроков: {users}")

    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print(f"Все пользователи проиграли. Загаданое число {number}")
            break
        print(f"Попытка № {count}.")
        for user in users:
            print(f"Ход пользователя - {user}")
            user_number = int(input("Введите число: "))
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            elif number < user_number:
                print("Ваше число, больше загаданого. Повторите попытку.")
            else:
                print("Ваше число, меньше загаданого. Повторите попытку.")
    else:
        print(f"Поздраляю, выиграл игрок - {winner_name}!")

if __name__ == "__main__":
    game()
