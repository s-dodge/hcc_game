# HCC Text-Based Adventure game by Soren M. Dodge | 2026
from game import Game
from player import Player
from rooms import all_rooms, locked_exits

if __name__ == "__main__":
    player = Player(location=all_rooms["help desk office"])
    game = Game(player=player, rooms=all_rooms, locked_exits=locked_exits)
    game.run()
