from globals import __BOARD__, __TILE__


class Tile:
    def __init__(self, row, col):
        self.row = row
        self.column = col
        self.bombed = False
        self.coordinate = str(self.row) + "," + str(self.column)
        self.value = __TILE__["values"]["default"]
        self.ship = None
        self.corners = {
            "rows": [__BOARD__["min_rows"], __BOARD__["max_rows"]],
            "cols": [__BOARD__["min_cols"], __BOARD__["max_cols"]]
        }

    def has_ship(self):
        if self.ship is not None:
            return True

        return False

    def add_ship(self, ship):
        self.ship = ship

    def bomb_ship(self):
        self.is_bombed()
        if self.has_ship():
            self.value = self.ship.short_name
            self.ship = None
        else:
            self.value = __TILE__["values"]["empty"]

    def is_bombed(self):
        if not self.bombed:
            self.bombed = True

    def sink_ship(self):
        if self.has_ship():
            count = 0
            tiles = self.ship.loc
            for tile in tiles:
                count += 1
                tile.bomb_ship()
            return count
        else:
            self.bomb_ship()
            return False

    def __str__(self):
        return "R" + str(self.row) + " C" + str(self.column)
