"""
Tile extends GUIElement to represent a single square in the board (contains a `GamePiece` and may be highlighted -
see below).

Fields
------
    Instance Vars
    -------------
        game_piece : Represents the piece at this location - either a `GamePiece` object or `None`
        highlight_circle : If True, show small transparent circle or similar visual cue to indicate this Tile in the
                board is currently a valid move
"""

from GUIElement import GUIElement
from GamePiece import GamePiece


class Tile(GUIElement):
    """ Tile extends GUIElement to represent a single square in the board. """

    ''' ========== Constant Class Variables ========== '''
    
    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, game_piece=GamePiece(), highlight_circle=None):
        # Call parent constructor
        super().__init__()

        # Make sure params are of correct type
        assert all([
            type(game_piece) in (GamePiece, None),
            type(highlight_circle) in (bool, None),
            # TODO Might want to add more later
        ])

        self.game_piece = game_piece
        self.highlight_valid_move = highlight_circle

    ''' ========== Magic Methods ========== '''

    ''' ========== Static Methods ========== '''

    ''' ========== Instance Methods ========== '''

    def draw(self):
        # TODO
        pass
