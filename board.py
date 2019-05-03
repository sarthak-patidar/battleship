from tile import Tile


class Board:
    def __init__(self, owner):  # Owner must be a player instance
        self.owner = owner
        self.maxRow = 9
        self.maxCol = 9
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

    def print_coordinates(self):
        for arr in self.grid:
            row = ""
            for tile in arr:
                row = row + str(tile.coordinate) + " "
            print(row)

    def __str__(self):
        return self.owner + "'s Board"
