from Game import Game
from Board import Board
# import pygame


def main():
    print()

    game = Game(Board.BLANK_STATE)
    print('Game with Blank Board')
    print('=====================')
    print(game)

    game.board.set_state(Board.STARTING_STATE)
    print('Game with Starting Othello Position')
    print('===================================')
    print(game)


if __name__ == '__main__':
    main()
