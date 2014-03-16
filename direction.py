class Direction(object):
    def __init__(self):
        self.directions = ['up', 'right', 'down', 'left']
        self.current = 'up'

    def _rotate(self, amount):
        ix = self.directions.index(self.current)
        ix = (ix + amount) % len(self.directions)
        return self.directions[ix]

    def turn_right(self):
        self.current = self._rotate(1)

    def turn_left(self):
        self.current = self._rotate(-1)

    def turn_around(self):
        self.current = self._rotate(2)

    def __eq__(self, value):
        return self.current == value
