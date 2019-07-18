from globals import __ARMADA__
from ships import Ship
from board import Board
from itertools import count


class Player(object):
    _ids = count(1)

    def __init__(self, name):
        self.id = next(self._ids)
        self.name = name
        self.board = Board(self)
        self.score = 0
        self.ships = self.create_armada()
        self.opponent = None

    def create_armada(self):
        armada = []
        for ship_name, ship in __ARMADA__.items():
            for i in range(ship['quantity']):
                new_ship = Ship(ship['length'], ship_name, self, ship['short_name'])
                armada.append(new_ship)
        return armada

    def set_opponent(self, player):
        self.opponent = player

    def __str__(self):
        return str(self.id) + ". " + self.name

    def add_score(self, count):
        self.score = self.score + count
