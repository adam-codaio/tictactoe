#!/usr/bin/python

import copy
import operator
import random

EMPTY = 0
DRAW = 0.5


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
        # Hard codes first move to speed up minimax
        # Definitely works for boards of size 2 and 3, unsure about larger
        if board.turns_taken == 0:
            i = random.randint(0, board.SIZE - 1)
            if i == board.SIZE / 2:  # Requires size = 3
                board.markMove(i, i, self.marker)
            else:
                if random.randint(0, 1):
                    board.markMove(i, i, self.marker)
                else:
                    board.markMove(i, board.SIZE - i - 1, self.marker)
            return

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
