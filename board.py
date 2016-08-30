#!/usr/bin/python

import numpy
import random
import players

EMPTY = 0
EX = 1
NUM_PLAYERS = 2  # Does not support changing number of players


class TicTacToeBoard:

    def __init__(self):
        self.SIZE = 3  # Does not support changing the size
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
            elif ((i + j) % 2) == 0:  # Hard coded for odd sized boards
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
