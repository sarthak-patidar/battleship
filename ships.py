from globals import __SHIP__
import random
from itertools import count


class Ship:
    _ids = count(1)

    def __init__(self, length, name, owner, short_name):
        self.id = next(self._ids)
        self.owner = owner
        self.length = length
        self.name = name
        self.short_name = short_name
        self.type = random.randint(0, 1)   # 0 for horizontal, 1 for vertical
        self.loc = []
        self.destroyed = False  # set to true if bombed
        self.update_loc()

    def get_type(self):
        return __SHIP__["alignment"][self.type]

    def update_loc(self):
        if not self.loc:
            start_tile = self.get_start_tile()
            row = start_tile.row
            col = start_tile.column

            if not self.type:  # Horizontal Alignment of ship => Row in constant
                for j in range(self.length):
                    try:
                        tile = self.owner.board.grid[row - 1][col + j - 1]
                        tile.add_ship(self)
                        self.loc.append(tile)
                    except IndexError:
                        print("Horizontal Index Error while placing warships at: ", row, col + j)
                        exit()

            else:   # Vertical Alignment of ship
                for i in range(self.length):
                    try:
                        tile = self.owner.board.grid[row + i - 1][col - 1]
                        tile.add_ship(self)
                        self.loc.append(tile)
                    except IndexError:
                        print("Vertical Index Error while placing warships at: ", row + i, col)
                        exit()
        else:
            print('Location already set.')

    def get_location(self):
        location = ""
        for tile in self.loc:
            location = location + tile.__str__() + "; "
        return location

    def get_start_tile(self):
        # exit condition => Tile at row, col is empty(no ship)
        # exit condition => can_start = True
        can_start = False
        length = self.length
        grid = self.owner.board.grid
        start_tile = None

        min_val = 1
        max_val_var = 9 - length  # var => in direction parallel to ship
        max_val_const = 9  # per => in direction perpendicular to ship

        while not can_start:
            const_coordinate = random.randint(min_val, max_val_const)
            var_coordinate = random.randint(min_val, max_val_var)
            has_ship = []

            if self.type:  # Column const
                row = var_coordinate
                col = const_coordinate

                for i in range(length):
                    tile = grid[row - 1 + i][col - 1]
                    if tile.has_ship():
                        has_ship.append(True)
                    else:
                        has_ship.append(False)

            else:   # Row const
                row = const_coordinate
                col = var_coordinate

                for j in range(length):
                    tile = grid[row - 1][col - 1 + j]
                    if tile.has_ship():
                        has_ship.append(True)
                    else:
                        has_ship.append(False)

            if True in has_ship:   # returns True if all the elements are false
                can_start = False
            else:
                can_start = True
                start_tile = grid[row -1][col - 1]

        return start_tile

    def __str__(self):
        return self.name + '(' + str(self.length) + ')'
