import random
import players
from board import TicTacToeBoard
from tracker import StatisticsTracker

EX = 1
OH = -1
EPOCHS = 50


def playGame(playerOne, playerTwo):
    board = TicTacToeBoard()

    while not board.winner and not board.over:
        if board.turn == EX:
            playerOne.makeMove(board)
        else:
            playerTwo.makeMove(board)
        # print board
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


def main():
    tracker = StatisticsTracker("Random", "Minimax")
    for i in xrange(EPOCHS):
        ex = True
        if random.randint(0, 1):
            playerOne = players.MinimaxPlayer(EX)
            playerTwo = players.MinimaxPlayer(OH)
        else:
            ex = False
            playerOne = players.MinimaxPlayer(EX)
            playerTwo = players.MinimaxPlayer(OH)
        win = playGame(playerOne, playerTwo)
        tracker.recordGame(ex, win)
    tracker.printReport()


if __name__ == '__main__':
    main()
