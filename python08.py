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
        huj = input()
        isInAllowMove = [move for move in moves if move == huj]
        print(isInAllowMove)
        print(len(isInAllowMove))
        if(len(isInAllowMove) != 0):
            print('here') 
            return huj


def MovePlayer2():
    while True:
        huj = input()
        isInAllowMove = [move for move in moves if move == huj]
        print(isInAllowMove)
        if(len(isInAllowMove) != 0): 
            return huj
    




def game(): 
    print('Move player 1')
    print(moveDoc)
    move1 = MovePlayer1()
    move2 = MovePlayer2()


    # if len(isInAllowMove) > 0:
    # print(isInAllowMove)
    # print('Move player 2')
    # print(moveDoc)
    # player2Move = input()

    print(whoWin(move1, move2))

    



def askToGameMore():
    print('Do u want to start new game?\n')
    print('Yes | No\n')
    isPlayNextOne = input()

    if isPlayNextOne:
        game()


# askToGameMore()
game()
