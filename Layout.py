"""
A Layout represents the a whole screen layout / view shown to the user. A GameGUI can have multiple Screens, so
whenever a new view is needed within a `GameGUI g` (main playing screen, win screen, menu screen, etc.), add a new
Screen to the `g.layouts` list.

A Layout consists of

"""

from GUIElement import GUIElement


class Layout:
    """ A Layout represents a particular screen layout / view shown to the user. See more docs at top of file. """

    ''' ========== Constant Class Variables ========== '''

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, gui_elements=None):

        if gui_elements is None:
            gui_elements = []

        # List of all the GUIElements (could be a Board, Tile, etc. - any type that extends GUIElement) that need to
        # be drawn on this Screen
        self.elements = gui_elements

    ''' ========== Magic Methods ========== '''

    ''' ========== Static Methods ========== '''

    ''' ========== Instance Methods ========== '''

    def handle_click(self, x_click_loc, y_click_loc):
        """ Docstring for handle_window_click() - TODO """

        for element in self.elements:
            # print("ELEMENT: ", type(element), "LOCATION: ", element.x_loc, element.y_loc)
            # print("MOUSE CLICK LOCATION: ", x_click_loc, y_click_loc)
            if GUIElement.click_is_inside(element, x_click_loc, y_click_loc):

                return element.handle_click(x_click_loc, y_click_loc)

    def draw(self, pygame_screen):
        """ Call draw(pygame_screen) on every GUIElement in this screen. """

        for element in self.elements:
            element.draw(pygame_screen)
