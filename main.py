import Game
import UI


def welcome():
    """ Print a welcome message when program is run. """

    print('''
 ██████╗ ████████╗██╗  ██╗███████╗██╗     ██╗      ██████╗ 
██╔═══██╗╚══██╔══╝██║  ██║██╔════╝██║     ██║     ██╔═══██╗
██║   ██║   ██║   ███████║█████╗  ██║     ██║     ██║   ██║
██║   ██║   ██║   ██╔══██║██╔══╝  ██║     ██║     ██║   ██║
╚██████╔╝   ██║   ██║  ██║███████╗███████╗███████╗╚██████╔╝
 ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ 
Created by: Ben Sylvester, Jackson Hall, Jordan Marchese, and Parker Strawbridge
''')


def main():
    """ Runs GUI or command line game based on gui Bool """
    gui = True
    if gui:
        UI.gui_game()
        UI.quit_game()
    else:
        welcome()
        game = Game.Game()
        game.game_loop()


if __name__ == '__main__':
    main()
