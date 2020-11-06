"""
GameGUI is the all-encompassing object to represent the GUI window instance. A GameGUI may have multiple Screens, so
there is no need to create new instances of GameGUI when a new screen layout is required.

"""

from Game import Game
from GUIElement import GUIElement
from Screen import Screen


class GameGUI:
    """ GameGUI is the all-encompassing object to represent the GUI window instance. See docs at top of file. """

    ''' ========== Constant Class Variables ========== '''

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, game=None, screens=None, active_screen=None):

        if game is None:
            game = Game()

        if screens is None:
            screens = []

        # List of Screen objects representing win screen, play screen, end screen, etc.
        self.screens = screens

        # Whichever screen should be draw()n in the pygame window
        self.active_screen = active_screen

        # Game object taking care of game logic
        self.game = game

    ''' ========== Magic Methods ========== '''

    ''' ========== Static Methods ========== '''

    @staticmethod
    def get_active_screen(game_gui):
        """ Docstring for get_active_window() - TODO """

        return game_gui.active_screen

    ''' ========== Instance Methods ========== '''

    def handle_click(self, x_click_loc, y_click_loc):
        """ Docstring for handle_click() - TODO """

        '''
        pseudocode:
        
        based on x_loc, y_loc of mouse click:
            
            if click in self.game.board:
                GameGUI.handle_board_click(x_loc, y_loc)
            elif click in 
        '''

        # Assuming (0, 0) pixel is top left of the pygame window, not whole screen
        for e in GameGUI.get_active_screen(self).elements:
            if GUIElement.click_is_inside(e, x_click_loc, y_click_loc):
                e.handle_click(x_click_loc, y_click_loc)
