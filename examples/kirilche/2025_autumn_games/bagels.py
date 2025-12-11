import random

NUM_DIGITS = 3  # Спробуйте змінити константу
MAX_GUESSES = 10  # Спробуйте встановити трішки менше для ускладнення гри


def getSecretNum():
    """Повертає string що складається з NUM_DIGITS унікальних випадкових цифр."""
    numbers = list('0123456789')  # створюємо список цифр від 0 до 9.
    random.shuffle(numbers)  # перемішуємо у випадковому порядку.

    # Беремо перші NUM_DIGITS цифр у списку цифр:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        # secretNum = secretNum + str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Повертає string з підказками pico, fermi, bagels для пари здогадка + секрет"""
    if guess == secretNum:
        return 'Ви вгадали!'

    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильна цифра на своєму місці.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Правильна цифра, але не на своєму місці.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # Немає вірних цифр взагалі.
    else:
        # сортуємо підказки в алфавітному порядку, щоб не видавати додаткової інформації
        clues.sort()
        # об'єднуємо підказки в один рядок.
        return ' '.join(clues)


def main():
    print(f'''Bagels - це логічна гра
Автор коду Al Sweigart al@inventwithpython.com

Я загадую {NUM_DIGITS}-значне число без повторень.
Спробуй вгадати, ось підказки:
Коли я кажу:    Це значить:
  Pico         Одна цифра вірна, але не на своєму місці.
  Fermi        Одна цифра вірна та на своєму місці.
  Bagels       Немає вірних цифр.

До прикладу якщо загадане 248 а ваша здогадка 843,
підказками будуть Fermi Pico.\n''')

    while True:  # основний цикл гри
        # це число, яке потрібно вгадати:
        secretNum = getSecretNum()
        print('Я загадую число.')
        print(f'Ви маєте {MAX_GUESSES} спроб, щоб вгадати.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # опитуємо поки число не вірне:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Здогадка #{numGuesses}: ')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Здогадка вірна, отже виходимо з циклу
            if numGuesses > MAX_GUESSES:
                print('Спроби закінчились.')
                print(f'Загадане число {secretNum}.')

        # Питаємо гравця чи хоче грати ще.
        print('Зіграємо ще? (yes або no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Приходьте ще!')

# якщо програма запущена (а не імпортована) - запустити гру:
if __name__ == '__main__':
    main()
