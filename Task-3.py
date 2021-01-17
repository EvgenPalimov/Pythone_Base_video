name=input("Введите ваше имя: ")
family=input("Введите вашу Фамилию: ")
age=int(input("Введите ваш возраст: "))
ves=int(input("Введите ваше имя: "))
if age <= 30 and ves >= 50 and ves <= 120:
    print(name, family, ",", age, "лет,", "вес:", ves, "кг.", "- в хорошем состоянии.")
elif age > 30 and age <= 40 and (ves < 50 or ves > 120):
    print(name, family, ",", age, "год,", "вес:", ves, "кг.", "- требуется заняться сабой")
elif age > 40 and (ves < 50 or ves > 120):
    print(name, family, ",", age, "год,", "вес:", ves, "кг.", "- требуется врачебный осмотр")

