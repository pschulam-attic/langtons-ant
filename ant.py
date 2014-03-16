import numpy as np

from board import Board
from direction import Direction
from random import random, sample
from time import sleep

class Ant(object):
    def __init__(self, n):
        self.board = Board(n)
        self.i = int(n) / 2
        self.j = int(n) / 2
        self.d = Direction()

    def step(self):
        if self.board[self.i, self.j]:  # Square is black
            self.d.turn_right()
        else:                           # Square is white
            self.d.turn_left()

        self.board.flip(self.i, self.j)
        self._move_forward()

    def _move_forward(self):
        i, j = self.i, self.j
        board = self.board

        if self.d == 'up':
            self.i, self.j = board.move_up(i, j)
        elif self.d == 'right':
            self.i, self.j = board.move_right(i, j)
        elif self.d == 'down':
            self.i, self.j = board.move_down(i, j)
        else:
            self.i, self.j = board.move_left(i, j)

    def __repr__(self):
        s = 'Ant(i={}, j={})'.format(self.i, self.j)
        return s + '\n' + str(self.board)

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    niter = int(sys.argv[2])
    boardfile = sys.argv[3]

    ant = Ant(n)
    for itx in xrange(niter):
        ant.step()

    ant.board.save_image(boardfile)
