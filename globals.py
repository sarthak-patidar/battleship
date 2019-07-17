# Board CONFIG
__BOARD__ = {
    "min_rows": 1,
    "max_rows": 9,
    "min_cols": 1,
    "max_cols": 9,
}

# GAME CONFIG
__GAME__ = {
    "players": 2,
    "turns": 15
}

# SHIP CONFIGS
__SHIP__ = {
    "alignment": ["Horizontal", "Vertical"]
}

# ARMADA CONFIG
__ARMADA__ = {
    "submarine": {
        "name": "submarine",
        "short_name": "S",
        "quantity": 2,
        "length": 1
    },
    "destroyer":  {
        "name": "destroyer",
        "short_name": "D",
        "quantity": 3,
        "length": 2
    },
    "cruiser": {
        "name": "cruiser",
        "short_name": "C",
        "quantity": 2,
        "length": 3
    },
    "battleship": {
        "name": "battleship",
        "short_name": "B",
        "quantity": 3,
        "length": 4
    }
}
