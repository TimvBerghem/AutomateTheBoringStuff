import random

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(f" {board['top-L']} | {board['top-M']} | {board['top-R']}")
    print(f" - + - + -")
    print(f" {board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print(f" - + - + -")
    print(f" {board['low-L']} | {board['low-M']} | {board['low-R']}")

def playerTurn():
    playerTurns = ['X', 'Y']
    turn = random.choice(playerTurns)
    for i in range(9):
        printBoard(theBoard)
        print(f"\nPlayer {turn}'s turn to move. Format is Row(top, mid, row)-Colomn(L, M, R):")
        move = input('  > ')
        theBoard[move] = turn
        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'


####### Execute Program #######
playerTurn()