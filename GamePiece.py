"""
`GamePiece` represents a two-colored Othello piece that can be placed in `Tile`s within a `Board`.

==========================
|||     Class Info     |||
==========================

Fields
======
    Constant Class Vars
    -------------------
        TODO

    Regular Class Vars
    ------------------
        TODO

Methods
=======
    Constructor
    -----------
        TODO

    Magic Methods
    -------------
        TODO

    Static Methods
    --------------
        TODO

    Instance Methods
    ----------------
        TODO

"""

from GUIElement import GUIElement


class GamePiece(GUIElement):
    """ """

    ''' ========== Constant Class Variables ========== '''
    # Printed to console when printing boards
    B_DISPLAY_CHAR = '○'
    W_DISPLAY_CHAR = '●'
    EMPTY_DISPLAY_CHAR = ' '

    # Used in backend
    B_CHAR = 'b'
    W_CHAR = 'w'
    EMPTY_CHAR = '-'

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''
    def __init__(self, side_up=EMPTY_CHAR):
        # Call parent constructor
        super().__init__()

        assert side_up in (GamePiece.B_CHAR, GamePiece.W_CHAR, GamePiece.EMPTY_CHAR)

        self.side_up = side_up

    ''' ========== Magic Methods ========== '''

    def __str__(self):
        if self.side_up == GamePiece.EMPTY_CHAR or self.side_up is None:
            return GamePiece.EMPTY_DISPLAY_CHAR

        if self.side_up == GamePiece.B_CHAR:
            return GamePiece.B_DISPLAY_CHAR
        elif self.side_up == GamePiece.W_CHAR:
            return GamePiece.W_DISPLAY_CHAR

        return GamePiece.EMPTY_DISPLAY_CHAR

    def __repr__(self):
        """ Docstring for __repr__() - TODO """

        if self.side_up is None:
            return GamePiece.EMPTY_CHAR

        return self.side_up

    ''' ========== Static Methods ========== '''

    @staticmethod
    def get_side_up(self):
        """ Return self.side_up. """
        return self.side_up

    ''' ========== Instance Methods ========== '''

    def flip(self):
        """ Change the side_up to the opposite color. """
        if self.side_up == GamePiece.B_CHAR:
            self.side_up = GamePiece.W_CHAR
        elif self.side_up == GamePiece.W_CHAR:
            self.side_up = GamePiece.B_CHAR
        else:
            print('warning: GamePiece.flip() called on GamePiece set to EMPTY_CHAR')
    
    def set_side_up(self, side_up):
        """ Set self.side_up to given value. """
        assert side_up in ('b', 'w')

        self.side_up = side_up

    def draw(self):
        pass

    def handle_click(self, x_click_loc, y_click_loc):
        """ Docstring for handle_click() - TODO """

        pass
