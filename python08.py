import os


def clear(): return os.system('cls')


moves = ["Rock", "Scissors", "Paper"]
[Rock, Scissors, Paper] = moves

moveDoc = "Rock | Scissors | Paper\n"


def whoWin(player1Move, player2Move):
    if player1Move == Rock:
        if player2Move == Scissors:
            return "Player1"
        elif player2Move == Paper:
            return "Player2"
        elif player2Move == Rock:
            return "Draw"
    elif player1Move == Scissors:
        if player2Move == Paper:
            return "Player1"
        elif player2Move == Rock:
            return "Player2"
        elif player2Move == Scissors:
            return "Draw"
    elif player1Move == Paper:
        if player2Move == Rock:
            return "Player1"
        elif player2Move == Scissors:
            return "Player2"
        elif player2Move == Paper:
            return "Draw"


def MovePlayer1():
    while True:
        clear()
        print('Move player 1')
        print(moveDoc)
        inputMove = input()
        isInAllowMove = [move for move in moves if move == inputMove]
        if(len(isInAllowMove) != 0):
            return inputMove


def MovePlayer2():
    while True:
        clear()
        print('Move player 2')
        print(moveDoc)
        inputMove = input()
        isInAllowMove = [move for move in moves if move == inputMove]
        if(len(isInAllowMove) != 0):
            return inputMove


def game():
    move1 = MovePlayer1()
    move2 = MovePlayer2()

    clear()

    print(whoWin(move1, move2) + " WIN")
    askToGameMore()


def askToGameMore():
    print('Do u want to start new game?\n')
    print('Yes | No\n')
    isPlayNextOne = input()

    if isPlayNextOne == "Yes":
        game()


# start game
game()
