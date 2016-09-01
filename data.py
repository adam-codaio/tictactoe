import itertools
import random
import players
from board import TicTacToeBoard
from tracker import StatisticsTracker

EX = 1
OH = -1
DRAW = 0.5
EPOCHS = 10000
SIZE = 3


def evaluateResult(board):
    if board.winner == EX:
        print "Player one won."
        return 1
    elif board.winner == OH:
        print "Player two won."
        return 0
    elif board.over:
        print "It was a draw."
        return 0.5
    else:
        print "Someone fucked up."
        return 42

def playGame(playerOne, playerTwo):
    board = TicTacToeBoard()
    states = [[0.0] * (SIZE ** 2)]
    while not board.winner and not board.over:
        if board.turn == EX:
            playerOne.makeMove(board)
        else:
            playerTwo.makeMove(board)
        states.append(board.board.flatten().tolist())
    return states, evaluateResult(board)

def recordData(f, states, win):
    if win == DRAW:
        for state in states:
            f.write(str(state))
            f.write('#')
            f.write(str(win))
            f.write('\n')
    else:
        flag = True if win else False
        for state in states:
            f.write(str(state))
            f.write('#')
            if flag:
                f.write(str(1))
                f.write('\n')
            else:
                f.write(str(0))
                f.write('\n')
            flag = not flag

def main():
    randomOne = players.RandomPlayer()
    randomTwo = players.RandomPlayer()
    minimaxOne = players.MinimaxPlayer()
    minimaxTwo = players.MinimaxPlayer()
    contestantsTwo = [randomOne, minimaxOne]
    contestantsOne = [randomTwo, minimaxTwo]
    with open('seed_data.txt', 'w') as f:
        for playerOne, playerTwo in itertools.product(contestantsOne, contestantsTwo):
            for i in xrange(EPOCHS):
                print "Playing game {} of 10000".format(i)
                if random.randint(0, 1):
                    playerOne.setMarker(EX)
                    playerTwo.setMarker(OH)
                    states, win = playGame(playerOne, playerTwo)
                    recordData(f, states, win)
                else:
                    playerOne.setMarker(OH)
                    playerTwo.setMarker(EX)
                    states, win = playGame(playerTwo, playerOne)
                    recordData(f, states, win)

if __name__ == '__main__':
    main()
