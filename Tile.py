class Tile:
    """ GUI element that represents a single square in the board (contains a GamePiece or None). """
    
    ''' ========== Constant Class Variables ========== '''
    

    ''' ========== Regular Class Variables ========== '''


    ''' ========== Constructor ========== '''
    def __init__(self, piece=None, is_highlighted=None):
        # Make sure params are of correct type
        if piece is not None:
            assert all([
                type(piece) in (GamePiece, None),
                type(is_highlighted) in (bool, None),
                # TODO Might want to add more later
            ])
        
        self.piece = piece
        self.is_highlighted = is_highlighted
    
    ''' ========== Magic Methods ========== '''

    ''' ========== Static Methods ========== '''
    
    ''' ========== Instance Methods ========== '''
    