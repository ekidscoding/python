import random

def drawBoard(board):
    # Ця функція друкує дошку, яку їй передали

    # "board" (дошка) - це список 10 рядків, що представляють ігрову дошку (індекс 0 ігноруємо)
    # print('   |   |' + ' ' * 16 + '|   |' )
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' '* 11 + ' 7 | 8 | 9')
    print('---+---+---' + ' '* 10 + '---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' '* 11 + ' 4 | 5 | 6')
    print('---+---+---' + ' '* 10 + '---+---+---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' '* 11 + ' 1 | 2 | 3')

def inputPlayerLetter():
    # Дозволяє гравцеві обрати ким бути - Х або O
    # Повертає список зі знаком гравця першим, та знаком компа другим.
    valid_X = ['x', 'X', 'х', 'Х']
    valid_0 = ['0', 'o', 'O', 'о', 'О']
    letter = ''
    while not (letter in valid_X or letter in valid_0):
        print('Ви хочете грати за X чи за O?')
        letter = input().upper().strip()
        if letter in valid_0:
            letter = 'O'
        elif letter in valid_X:
            letter = 'X'

    # Першим в списку буде гравець, комп'ютер буде другим
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Випадковим чином обираємо того, хто першим ходить.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Отримавши дошку та букву гравця, ця функція поверне True якщо Гравець виграв.
    # Ми використовуємо bo замість board та le замість letter щоб не друкувати багато.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # верхня горизонталь
    (bo[4] == le and bo[5] == le and bo[6] == le) or # середня горизонталь
    (bo[1] == le and bo[2] == le and bo[3] == le) or # нижня горизонталь
    (bo[7] == le and bo[4] == le and bo[1] == le) or # ліва вертикаль
    (bo[8] == le and bo[5] == le and bo[2] == le) or # середня вертикаль
    (bo[9] == le and bo[6] == le and bo[3] == le) or # права вертикаль
    (bo[7] == le and bo[5] == le and bo[3] == le) or # діагональ
    (bo[9] == le and bo[5] == le and bo[1] == le)) # діагональ

def _getBoardCopy(board):
    # робимо та повертаємо копію Ігровогї Дошки
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def _isSpaceFree(board, move):
    # Поверне True якщо вказане поле вільне на даній дошці.
    return board[move] == ' '

def getPlayerMove(board):
    # Дозволяє Гравцеві ввести хід.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not _isSpaceFree(board, int(move)):
        print('Який ваш наступний хід? (1-9)')
        move = input()
    return int(move)

def _chooseRandomMoveFromList(board, movesList):
    # Повертає правильний хід із вказаних ходів.
    # Поверне None якщо правильних ходів немає.
    possibleMoves = []
    for i in movesList:
        if _isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Отримує дошку та знак компа, визначає куди йти та повертає хід.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Ось алгоритм нашого Tic Tac Toe AI:
    # Перше, визначаємо чи ми можемо виграти за 1 хід
    for i in range(1, 10):
        boardCopy = _getBoardCopy(board)
        if _isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Перевіряємо чи гравець може виграти наступним ходом, блокуємо виграшний хід.
    for i in range(1, 10):
        boardCopy = _getBoardCopy(board)
        if _isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Займаємокутові клітинки, якщо доступні.
    move = _chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Займаємо центр, якщо це можливо.
    if _isSpaceFree(board, 5):
        return 5

    # Йдемо в одну із сторін випадковим чином.
    return _chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Повертає True якщо всі поля на дошці зайняті. Інакше поверне False.
    for i in range(1, 10):
        if _isSpaceFree(board, i):
            return False
    return True
