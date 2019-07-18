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


def print_game_instructions(max_turns, max_score):
    print()
    print('Each Player\'s armada contains 3 Battleships, 3 Destroyers, 2 Submarines and 2 Cruisers placed on a 9x9 Board.')
    print('Maximum', max_score, 'points can be scored and whoever scores this points first will win the game.')
    print('Each Player will get', max_turns, 'turns to guess other player\'s armada\'s location.')
    print('Press ctrl+d to exit game at any point.')
    print()

