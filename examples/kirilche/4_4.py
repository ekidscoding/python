# використання ключового слова 'in'
slovo = "абабагаламага"
print("а" in slovo)

spysok = ["ручка", "олівець", "лінійка", "гумка"]
thing = input("Що тобі позичити? ")
thing = thing.lower()
if thing in spysok:
    print(f"в мене є в запасі {thing}. Ось тримай, але повернеш після уроків")
else:
    print(f"в мене є {thing}, але тільки для себе. Вибач, спитай ще когось.")

sport_kids = ["Ганна", "Ірина", "Павло", "Євген"]
smart_kids = ["Ірина", "Дмитро", "Василь", "Євгенія"]
boys = ["Павло", "Євген", "Дмитро", "Василь"]
girls = ["Ганна", "Ірина", "Євгенія"]

klas = ["Павло", "Євген", "Дмитро", "Василь", "Ганна", "Ірина", "Євгенія", "Нікодим"]

for student in klas:
    if student in sport_kids and student in smart_kids:
        if student in boys:
            print(student, "– Спортсмен-розумник")
        elif student in girls:
            print(student, "– Спортсменка-розумниця")
    elif student not in sport_kids and student in smart_kids:
        if student in boys:
            print(student, "– Розумник")
        elif student in girls:
            print(student, "– Розумниця")
    elif student in sport_kids and student not in smart_kids:
        if student in boys:
            print(student, "– Спортсмен")
        elif student in girls:
            print(student, "– Спортсменка")
    else:
        print(student, "поки нічого не робить")