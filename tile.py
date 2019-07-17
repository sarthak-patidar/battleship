from globals import __BOARD__


class Tile:
    def __init__(self, row, col):
        self.row = row
        self.column = col
        self.hasShip = False
        self.bombed = False
        self.coordinate = str(self.row) + "," + str(self.column)  # For Debugging Purposes
        self.value = '-'
        self.ship = None
        self.corners = {
            "rows": [__BOARD__["min_rows"], __BOARD__["max_rows"]],
            "cols": [__BOARD__["min_cols"], __BOARD__["max_cols"]]
        }

    def is_border(self):
        row = self.row
        col = self.column

        if row in self.corners["rows"] or col in self.corners["cols"]:
            return True
        return False

    def add_ship(self, ship):
        self.ship = ship
        self.hasShip = True    # add ships

    def del_ship(self):  # Always call this method after calling is_bombed() method
        self.is_bombed()
        if self.hasShip:
            self.value = self.ship.short_name
        else:
            self.value = "X"

        self.ship = None
        self.hasShip = False   # delete ship if guessed by player

    def is_bombed(self):
        if not self.bombed:
            self.bombed = True

    def sink_ship(self):
        if self.hasShip:
            count = 0
            tiles = self.ship.loc
            for tile in tiles:
                count = count + 1
                tile.del_ship()
            return count
        else:
            self.del_ship()
            return False

    def __str__(self):
        return "R" + str(self.row) + " C" + str(self.column)
