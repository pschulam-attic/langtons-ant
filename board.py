import numpy as np
import matplotlib.pyplot as plt

class Board(object):
    def __init__(self, n):
        self.n = n
        self.squares = {}
        for i in xrange(n):
            for j in xrange(n):
                self.squares[i, j] = 0

    def move_up(self, i, j):
        i = (i - 1) % self.n
        return i, j

    def move_right(self, i, j):
        j = (j + 1) % self.n
        return i, j

    def move_down(self, i, j):
        i = (i + 1) % self.n
        return i, j

    def move_left(self, i, j):
        j = (j - 1) % self.n
        return i, j

    def flip(self, i, j):
        self[i, j] = (self[i, j] + 1) % 2

    def to_ndarray(self):
        board = np.zeros((self.n, self.n), np.int8)
        for i in xrange(self.n):
            for j in xrange(self.n):
                board[i, j] = self.squares[i, j]

        return board

    def save_image(self, filename):
        board = self.to_ndarray()
        plt.imshow(board)
        plt.savefig(filename)

    def __getitem__(self, key):
        i, j = key
        i = int(i)
        j = int(j)
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        return self.squares[i, j]

    def __setitem__(self, key, value):
        i, j = key
        i = int(i)
        j = int(j)
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        self.squares[i, j] = value

    def __repr__(self):
        s = []
        for i in xrange(self.n):
            row = [ self.squares[i, j] for j in xrange(self.n) ]
            row = ' '.join(map(str, row))
            s.append(row)
        s = '\n'.join(s)
        return s
