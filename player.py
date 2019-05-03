from ships import battleship, submarine, cruiser, destroyer, Ship
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
        ships = [battleship, submarine, cruiser, destroyer]
        armada = []
        for ship in ships:
            for i in range(ship['quantity']):
                new_ship = Ship(ship['length'], ship['name'], self, ship['short_name'])
                armada.append(new_ship)
        return armada

    def set_opponent(self, player):
        self.opponent = player

    def __str__(self):
        return str(self.id) + ". " + self.name

    def add_score(self, count):   # Count = ship.length
        self.score = self.score + count
