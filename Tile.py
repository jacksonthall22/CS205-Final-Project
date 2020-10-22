"""
GUI element used to represent a single square in the board (contains a `GamePiece` or `None`).

Instance Vars
-------------
    game_piece : Represents the piece at this location - either a `GamePiece` object or `None`
    highlight_valid_move : If True, show some sort of visual cue to user (ie. small transparent 
        or similar) in this Tile to indicate this space in the board is a valid move

"""

from GUIElement import GUIElement


class Tile(GUIElement):
    
    ''' ========== Constant Class Variables ========== '''
    

    ''' ========== Regular Class Variables ========== '''


    ''' ========== Constructor ========== '''

    def __init__(self, game_piece=None, highlight_valid_move=None):
        # Make sure params are of correct type
        assert all([
            type(game_piece) in (GamePiece, None),
            type(highlight_valid_move) in (bool, None),
            # TODO Might want to add more later
        ])
        
        self.game_piece = game_piece
        self.highlight_valid_move =  highlight_valid_move
    
    
    ''' ========== Magic Methods ========== '''


    ''' ========== Static Methods ========== '''

    
    ''' ========== Instance Methods ========== '''

    def draw(self):
        # TODO
        pass