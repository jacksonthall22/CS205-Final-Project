class Tile:
    """ GUI element that represents a single square in the board (contains a GamePiece or None). """
    
    ''' ========== Constant Class Variables ========== '''
    

    ''' ========== Regular Class Variables ========== '''


    ''' ========== Constructor ========== '''
    def __init__(self, piece=None, isHighlighted=None):
        # Make sure params are of correct type
        if piece is not None:
            assert all([
                type(piece) in (GamePiece, None),
                type(isHighlighted) in (bool, None),
                # TODO Might want to add more later
            ])
        
        self.piece = piece
        self.isHighlighted = isHighlighted
    
    ''' ========== Magic Methods ========== '''

    ''' ========== Static Methods ========== '''
    
    ''' ========== Instance Methods ========== '''
    