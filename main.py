from Board import Board
from Game import Game
from GamePiece import GamePiece
import pygame


def main():
    print()

    game = Game(Board.get_state_from_strings([
        'ww--b--b',
        'www-b-bb',
        'wwwwb-bb',
        'wwwbwwbb',
        'wwbwwwbb',
        'bwwwwbwb',
        'wbbwwwbb',
        'bbbwwb-b'
    ]), GamePiece.B_CHAR)

    game.game_loop()


if __name__ == '__main__':
    main()
