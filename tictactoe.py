#!/usr/bin/python

import copy
import numpy
import operator
import random

DRAW = 0.5
EMPTY = 0
EX = 1
OH = -1
NUM_PLAYERS = 2


class TicTacToeBoard:

    def __init__(self):
        self.SIZE = 3
        self.turn = EX
        self.turns_taken = 0
        self.board = numpy.zeros((self.SIZE, self.SIZE))
        self.winner = EMPTY
        self.over = False

    def markMove(self, i, j, value):
        self.board[i, j] = value
        self.turn *= -1
        self.turns_taken += 1

        if self.turns_taken >= self.SIZE * NUM_PLAYERS - 1:
            row_sum = numpy.sum(self.board[i, :])
            col_sum = numpy.sum(self.board[:, j])
            if abs(row_sum) == self.SIZE:
                self.winner = row_sum / self.SIZE
            elif abs(col_sum) == self.SIZE:
                self.winner = col_sum / self.SIZE
            elif ((i + j) % 2) == 0:
                diag_sum = 0
                antidiag_sum = 0
                for i in xrange(self.SIZE):
                    diag_sum += self.board[i, i]
                    antidiag_sum += self.board[i, self.SIZE - i - 1]
                if abs(diag_sum) == self.SIZE:
                    self.winner = diag_sum / self.SIZE
                elif abs(antidiag_sum) == self.SIZE:
                    self.winner = antidiag_sum / self.SIZE

        if self.turns_taken == self.SIZE * self.SIZE:
            self.over = True

    def __repr__(self):
        return self.board.__repr__()


class Player:

    def __init__(self, marker):
        self.marker = marker

    def getCandidateMoves(self, board):
        candidate_moves = []
        for i in xrange(board.SIZE):
            for j in xrange(board.SIZE):
                if board.board[i, j] == EMPTY:
                    candidate_moves.append((i, j))
        return candidate_moves


class RandomPlayer(Player):

    def makeMove(self, board):
        candidate_moves = self.getCandidateMoves(board)
        i, j = candidate_moves[random.randint(0, len(candidate_moves) - 1)]
        board.markMove(i, j, self.marker)


class MiniMaxPlayer(Player):

    def makeMove(self, board):
        self.recurse(copy.deepcopy(board))
        i, j = self.move
        board.markMove(i, j, self.marker)

    def recurse(self, board):
        if board.winner or board.over:
            if not board.winner:
                return DRAW
            return 1 if board.winner == self.marker else 0

        scores = []
        moves = []
        for i, j in self.getCandidateMoves(board):
            newBoard = copy.deepcopy(board)
            newBoard.markMove(i, j, board.turn)
            scores.append((self.recurse(newBoard)))
            moves.append((i, j))

        if board.turn == self.marker:
            index, value = max(enumerate(scores), key=operator.itemgetter(1))
            self.move = moves[index]
            return value
        else:
            index, value = min(enumerate(scores), key=operator.itemgetter(1))
            self.move = moves[index]
            return value


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
    playerOne = RandomPlayer(EX)
    playerTwo = MiniMaxPlayer(OH)
    playGame(playerOne, playerTwo)


if __name__ == '__main__':
    main()
