from globals import __BOARD__
from tile import Tile


class Board:
    def __init__(self, owner):
        self.owner = owner
        self.maxRow = __BOARD__["max_rows"]
        self.maxCol = __BOARD__["max_cols"]
        self.armada = []
        self.grid = self.create_grid()

    def create_grid(self):
        grid = []
        for i in range(self.maxRow):
            arr = []
            for j in range(self.maxCol):
                arr.append(Tile(i+1, j+1))
            grid.append(arr)
        return grid

    def print(self):
        for arr in self.grid:
            row = ""
            for tile in arr:
                row = row + str(tile.value) + " "
            print(row)

    def __str__(self):
        return self.owner + "'s Board"
