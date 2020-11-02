from Board import Board
from Game import Game
import pygame


def main():
    print()

    game = Game(Board.get_starting_state())
    Game.game_loop(game)


if __name__ == '__main__':
    main()
