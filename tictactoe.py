#!/usr/bin/python

import numpy
import random
import copy
import operator

EMPTY = 0
DRAW = 0.5
EX = 1
OH = -1

class TicTacToeBoard:

	def __init__(self):
		self.SIZE = 3
		self.board = numpy.zeros((self.SIZE, self.SIZE))

	def markMove(self, i, j, value):
		self.board[i, j] = value

	def isWon(self):
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

	def isTurn(self):
		return OH if numpy.sum(self.board) else EX

	def __repr__(self):
		return self.board.__repr__()

class Player:

	def __init__(self, marker):
		self.marker = marker

	def getCandidateMoves(self, board):
		candidate_moves = []
		for i in xrange(board.SIZE):
			for j in xrange(board.SIZE):
				if board.board[i,j] == EMPTY:
					candidate_moves.append((i,j))
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
		result = board.isWon()
		if result != EMPTY:
			if result == DRAW: return DRAW
			return 1 if result == self.marker else 0
		scores = []
		moves = []

		for i, j in self.getCandidateMoves(board):
			newBoard = copy.deepcopy(board)
			newBoard.markMove(i, j, board.isTurn())
			scores.append((self.recurse(newBoard)))
			moves.append((i,j))

		if board.isTurn() == self.marker:
			index, value = max(enumerate(scores), key=operator.itemgetter(1))
			self.move = moves[index]
			return value
		else:
			index, value = min(enumerate(scores), key=operator.itemgetter(1))
			self.move = moves[index]
			return value

def playGame(playerOne, playerTwo):
	board = TicTacToeBoard()
	result = board.isWon()
	while not result:
		if board.isTurn() == EX:
			playerOne.makeMove(board)
		else:
			playerTwo.makeMove(board)
		result = board.isWon()
		print board
	if result == DRAW:
		print "It was a draw."
	elif result == EX:
		print "Player one won."
	elif result == OH:
		print "Player two won."
	else:
		print "Someone fucked up."

def main():
	playerOne = MiniMaxPlayer(EX)
	playerTwo = RandomPlayer(OH)
	playGame(playerOne, playerTwo)


if __name__ == '__main__':
	main()