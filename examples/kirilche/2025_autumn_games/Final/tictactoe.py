# ГРА Хрестики 0-ки

from utils import inputPlayerLetter, whoGoesFirst, drawBoard, getPlayerMove, getComputerMove, makeMove, isWinner, isBoardFull


print('Вітаємо у Грі "Хрестики Нулики" (Tic Tac Toe)!')

while True:
    # Ініціалізація гри
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    first = "Гравець" if turn == 'player' else "Комп'ютер"
    print(first + ' ходитиме першим.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Черга Гравця.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ура, Ви виграли гру!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Гра скінчилась нічиєю!')
                    break
                else:
                    turn = 'computer'

        else:
            # Хід комп'ютера.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Комп\'ютер переміг, ви програли.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Гра в нічию!')
                    break
                else:
                    turn = 'player'

    print('Зіграємо ще? (yes або no)')
    if not input().lower().startswith('y'):
        break
