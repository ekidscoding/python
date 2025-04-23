import sys
from random import choice
from collections import namedtuple

def start_game():
    print("\nЛаскаво Прошу до гри 'Камінь🪨, Ножиці ✂️, Папір📜'\n")
    print("Гра відбувається до 3 очків.\n")
    print("Кінець гри — введіть 0\n")
    
    Total = namedtuple("Рахунок", ["Людина", "Комп"])
    total = Total(0, 0)
    
    while total[0] <3 and total[1] <3:
        you = vvid_hodu()
        it = computer_hodyt()
        winner = ocinka_hodu(you[0], it[0])
        
        if winner[0] == "Людина":
            total = Total(total[0] + 1, total[1])
        elif winner[0] == "Комп'ютер":
             total = Total(total[0], total[1] + 1)
        elif winner[0] == "Дружба":
            total = Total(total[0] + 0.5, total[1] + 0.5)
        else:
            it = (-1, "не важливо")
        
        message = f"""\
        Ваш хід — {you[1]}
        Його хід — {it[1]}
        
        {winner[0]} перемагає

        {winner[1]}

        {total}

        """
        print(message)
    if total[0] >= 3 and  total[1] >= 3:
        print("WIN + WIN")
    elif total[0] >= 3:
        print("\nЛюдина ПЕРЕМОГЛА Комп!!!")
    elif total[1] >= 3:
        print("\nБуває, наступного разу пощастить більше")

def vvid_hodu()-> tuple[int, str]:
    hid = input("Ваш хід: ").lower()
    match hid:
        case '0':
            print("На все добре!")
            sys.exit()
        case 'камінь' | 'к':
            return 0, "Камінь🪨"
        case 'ножиці' | 'н':
            return 1, "Ножиці ✂"
        case 'папір' | 'п':
            return 2, "Папір📜"
        case _:
            return -1, "не розпізнано"

def computer_hodyt() -> tuple[int, str]:
    return choice([(0, "Камінь🪨"),
                            (1, "Ножиці ✂"),
                            (2, "Папір📜")])

def ocinka_hodu(n1: int, n2: int) -> tuple[str, str]:
    match n1, n2:
        case (0, 1) | (1, 2) | (2, 0):
            return "Людина", "Пощастило!"
        case (0, 0) | (1, 1) | (2, 2):
            return "Дружба", "Нічия"
        case (1, 0) | (2, 1) | (0, 2):
            return "Комп'ютер", "Спробуй ще"
        case _:
            return "Ніхто не", "Помилка"


if __name__ == '__main__':
    start_game()
