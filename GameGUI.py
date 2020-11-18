"""
GameGUI is the all-encompassing object to represent the GUI window instance. A GameGUI may have multiple Layouts, so
there is no need to create new instances of GameGUI when a new screen layout is required (menu screen, main playing
screen, win screen, etc.).

"""

from Game import Game
from GUIElement import GUIElement
from Layout import Layout


class GameGUI:
    """ GameGUI is the all-encompassing object to represent the GUI window instance. See docs at top of file. """

    ''' ========== Constant Class Variables ========== '''

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, game=None, screens=None, active_layout=None):

        if game is None:
            game = Game()

        if screens is None:
            screens = set()

        # List of Screen objects representing win screen, play screen, end screen, etc.
        self.layouts = screens

        # Whichever screen should be draw()n in the pygame window
        self.active_layout = active_layout

        # Game object taking care of game logic
        self.game = game

    ''' ========== Magic Methods ========== '''

    ''' ========== Static Methods ========== '''

    @staticmethod
    def get_active_screen(game_gui):
        """ Docstring for get_active_window() - TODO """

        return game_gui.active_screen

    ''' ========== Instance Methods ========== '''

    def update_active_screen(self, new_layout):
        """ Docstring for change_screen() - TODO """

        if new_layout not in self.layouts:
            self.layouts.add(new_layout)

        self.active_layout = new_layout

    def handle_click(self, x_click_loc, y_click_loc):
        """ Docstring for handle_click() - TODO """

        # Handle the click in the context of the currently-active Layout
        return self.active_layout.handle_click(x_click_loc, y_click_loc)

    def draw(self, screen):
        """ Docstring for draw() - TODO """
        self.active_layout.draw(screen)