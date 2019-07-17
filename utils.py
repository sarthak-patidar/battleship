from globals import __BOARD__


def get_coordinate(input_msg):

    min_val = __BOARD__["min_rows"]
    max_val = __BOARD__["max_rows"]

    running = True

    while running:
        coordinate = input(input_msg)
        try:
            coordinate = int(coordinate)
        except ValueError:
            print("Invalid input.\nPlease enter a number between {} and {} including both:".format(min_val, max_val))
            continue

        if coordinate < min_val or coordinate > max_val:
            print("Invalid input.\nPlease enter a number between {} and {} including both:".format(min_val, max_val))
            continue
        else:
            running = False

    return coordinate


def player_input(msg):
    return input(msg)
