"""
A Screen represents the a whole screen layout / view shown to the user. A GameGUI can have multiple Screens, so
whenever a new view is needed within a `GameGUI g` (main playing screen, win screen, menu screen, etc.), add a new
Screen to the `g.screens` list.
"""

from GUIElement import GUIElement


class Screen:
    """ A Screen represents a particular screen layout / view shown to the user. See more docs at top of file. """

    ''' ========== Constant Class Variables ========== '''

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, elements=None):

        if elements is None:
            elements = []

        # list of all the GUIElements (could be a Board, Tile, etc. - any type that extends GUIElement) that need to
        # be drawn on this Screen
        self.elements = elements

    ''' ========== Magic Methods ========== '''

    ''' ========== Static Methods ========== '''

    ''' ========== Instance Methods ========== '''

    def handle_click(self, x_click_loc, y_click_loc):
        """ Docstring for handle_window_click() - TODO """

        for element in self.elements:
            if GUIElement.click_is_inside(element, x_click_loc, y_click_loc):
                element.handle_click(x_click_loc, y_click_loc)

    def draw(self, x_loc, y_loc):
        """ Call draw() on every GUIElement in this screen. """

        for element in self.elements:
            element.draw()
