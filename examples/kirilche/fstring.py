name = input("Введіть ваше ім'я: ")

while True:
    age = input("Введіть свій вік: ")
    try:
        age_int = int(age)
    except ValueError:
        print(f"Вік {age} не є коректним цілим числом. Введіть коректний вік")
        continue
    if age_int <= 0:
        print(f"Вік {age} не є додатним цілим числом. Введіть коректний вік")
    break

print(f"Вас звати {name} вам {age_int} років")