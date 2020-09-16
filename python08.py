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


def game(): 
    print('Move player 1')
    print(moveDoc)
    player1Move = input()
    isInAllowMove = [move for move in moves if move == player1Move]
    # if len(isInAllowMove) > 0:
    # print(isInAllowMove)
    print('Move player 2')
    print(moveDoc)
    player2Move = input()

    print(whoWin(player1Move, player2Move))

    



def askToGameMore():
    print('Do u want to start new game?\n')
    print('Yes | No\n')
    isPlayNextOne = input()

    if isPlayNextOne:
        game()


# askToGameMore()
game()
