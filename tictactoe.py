#!/usr/bin/python

import numpy
import random
import players
from board import TicTacToeBoard

EX = 1
OH = -1


def playGame(playerOne, playerTwo):
    board = TicTacToeBoard()

    while not board.winner and not board.over:
        if board.turn == EX:
            playerOne.makeMove(board)
        else:
            playerTwo.makeMove(board)
        print board
    if board.winner == EX:
        print "Player one won."
    elif board.winner == OH:
        print "Player two won."
    elif board.over:
        print "It was a draw."
    else:
        print "Someone fucked up."


def main():
    playerOne = players.MiniMaxPlayer(EX)
    playerTwo = players.MiniMaxPlayer(OH)
    playGame(playerOne, playerTwo)


if __name__ == '__main__':
    main()
