from Game import Game


def welcome():
    """ Print a welcome message when program is run. """

    print('''
 ██████╗ ████████╗██╗  ██╗███████╗██╗     ██╗      ██████╗ 
██╔═══██╗╚══██╔══╝██║  ██║██╔════╝██║     ██║     ██╔═══██╗
██║   ██║   ██║   ███████║█████╗  ██║     ██║     ██║   ██║
██║   ██║   ██║   ██╔══██║██╔══╝  ██║     ██║     ██║   ██║
╚██████╔╝   ██║   ██║  ██║███████╗███████╗███████╗╚██████╔╝
 ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ 
Created by Ben Sylvester, Jackson Hall, Jordan Marchese, and Parker Sawbridge
''')


def main():
    welcome()

    # game = Game(Board.get_state_from_strings([
    #     'ww--b--b',
    #     'www-b-bb',
    #     'wwwwb-bb',
    #     'wwwbwwbb',
    #     'wwbwwwbb',
    #     'bwwwwbwb',
    #     'wbbwwwbb',
    #     'bbbwwb-b'
    # ]), GamePiece.B_CHAR)

    game = Game()

    game.game_loop()


if __name__ == '__main__':
    main()
