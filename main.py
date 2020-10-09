from Game import Game
from Board import Board

def main():
    print()

    game = Game(Board.BLANK_STATE)
    print('Game with Blank Board')
    print('=====================')
    print(game)

    game.board.setState([
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'w', 'b', None, None, None],
        [None, None, None, 'b', 'w', None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]])
    print('Game with Starting Othello Position')
    print('===================================')
    print(game)
if __name__ == '__main__':
    main()
