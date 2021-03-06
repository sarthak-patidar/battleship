#!/usr/bin/env python3.6

from globals import __GAME__
from player import Player
from utils import get_coordinate, player_input, print_game_instructions


class Game:
    def __init__(self):
        self.players = __GAME__["players"]
        self.registry = self.get_players()
        self.maxScore = self.get_max_score()
        self.turns = __GAME__["turns"]

    def get_players(self):
        players = []
        for i in range(self.players):
            msg = "Enter Player{}'s Name: ".format(i+1)
            name = player_input(msg)
            player = Player(name)
            players.append(player)
        return players

    def set_opponents(self):
        player = self.registry
        player[0].set_opponent(player[1])
        player[1].set_opponent(player[0])

    def play(self):
        self.set_opponents()
        print_game_instructions(self.turns, self.maxScore)
        players = self.registry

        for i in range(self.turns):
            if players[0].score < self.maxScore and players[1].score < self.maxScore:
                for player in players:
                    opponent = player.opponent
                    opponent.board.print()
                    str_row = "{} guess row>".format(player.name)
                    str_col = "{} guess column>".format(player.name)

                    row = get_coordinate(str_row)
                    col = get_coordinate(str_col)
                    tile = opponent.board.grid[row - 1][col - 1]

                    while tile.bombed:
                        print('You have already bombed this position. Please bomb some other position.')
                        row = get_coordinate(str_row)
                        col = get_coordinate(str_col)
                        tile = opponent.board.grid[row - 1][col - 1]

                    count = tile.sink_ship()
                    if count:
                        player.add_score(count)

                self.display_score(i + 1)
        self.display_result()

    def display_score(self, turn):
        print()
        scr = 'Score at the end of round ' + str(turn) + ' => ' + self.registry[0].name + ": "
        scr = scr + str(self.registry[0].score) + " v/s " + self.registry[1].name + ": " + str(self.registry[1].score)
        print(scr)
        print()

    def display_result(self):
        if self.registry[0].score > self.registry[1].score:
            print("{} Won.".format(self.registry[0].name))
        elif self.registry[1].score > self.registry[0].score:
            print("{} Won.".format(self.registry[1].name))
        else:
            print("It's a Draw.")

    def get_max_score(self):
        score = 0
        player = self.registry[0]
        for ship in player.ships:
            score = ship.length + score
        return score

    def __str__(self):
        return self.registry[0].__str__() + " v/s " + self.registry[1].__str__()


if __name__ == "__main__":
    game = Game()
    try:
        game.play()
    except EOFError:
        print("\nExiting game.")
        game.display_result()


