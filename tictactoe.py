#!/usr/bin/python

import numpy
import random
import copy

DRAW = -1
EMPTY = 0
EX = 1
OH = 2

class TicTacToeBoard:

	def __init__(self):
		self.SIZE = 3
		self.board = numpy.zeros((self.SIZE, self.SIZE))

	def markMove(self, i, j, value):
		self.board[i, j] = value

	def isWon(self):
		global DRAW
		global EMPTY
		global EX
		global OH

		for i in xrange(self.SIZE):
			row_sum = numpy.sum(self.board[i,:])
			col_sum = numpy.sum(self.board[:,i])
			if row_sum == self.SIZE * EX or col_sum == self.SIZE * EX:
				return EX
			elif row_sum == self.SIZE * OH or col_sum == self.SIZE * OH:
				return OH
		diag_sum = 0
		antidiag_sum = 0
		for i in xrange(self.SIZE):
			diag_sum += self.board[i,i]
			antidiag_sum += self.board[i, self.SIZE - i - 1]
		if diag_sum == self.SIZE * EX or antidiag_sum == self.SIZE * EX:
			return EX
		elif diag_sum == self.SIZE * OH or antidiag_sum == self.SIZE * OH:
			return OH
		for i in xrange(self.SIZE):
			for j in xrange(self.SIZE):
				if self.board[i,j] == EMPTY: return EMPTY
		return DRAW

	def __repr__(self):
		return self.board.__repr__()

class Player:

	def __init__(self, marker):
		self.marker = marker

	def findCandidateMoves(self, board):
		candidate_moves = []
		for i in xrange(board.SIZE):
			for j in xrange(board.SIZE):
				if board.board[i,j] == EMPTY:
					candidate_moves.append((i,j))
		return candidate_moves


class RandomPlayer(Player):

	def makeMove(self, board):
		candidate_moves = self.findCandidateMoves(board)
		i, j = candidate_moves[random.randint(0, len(candidate_moves) - 1)]
		board.board[i,j] = self.marker

class MiniMaxPlayer(Player):

	def makeMove(self, board):
		pass


def main():
	tttBoard = TicTacToeBoard()
	playerOne = RandomPlayer(EX)
	playerTwo = MiniMaxPlayer(OH)
	print tttBoard
	print tttBoard.isWon()


if __name__ == '__main__':
	main()