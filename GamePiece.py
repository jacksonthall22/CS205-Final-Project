from GUIElement import GUIElement


class GamePiece(GUIElement):
    """ """

    ''' ========== Constant Class Variables ========== '''
    # Printed to console when printing boards
    B_DISPLAY_CHAR = '○'
    W_DISPLAY_CHAR = '●'

    # Used in backend (for easy typing)
    B_CHAR = 'b'
    W_CHAR = 'w'
    EMPTY_CHAR = ' '

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''
    def __init__(self, side_up='b'):
        # Call parent constructor
        super().__init__()

        self.side_up = side_up

    ''' ========== Magic Methods ========== '''

    def __str__(self):
        return (GamePiece.B_CHAR, GamePiece.W_CHAR)[self.side_up == 'w']

    ''' ========== Static Methods ========== '''

    ''' ========== Instance Methods ========== '''

    def flip(self):
        """ Change the side_up to the opposite color. """
        self.side_up = (GamePiece.B_CHAR, GamePiece.W_CHAR)[self.side_up == 'b']
    
    def get_side_up(self):
        """ Return self.side_up. """
        return self.side_up
    
    def set_side_up(self, side_up):
        """ Set self.side_up to given value. """
        assert side_up in ('b', 'w')

        self.side_up = side_up

    def draw(self):
        pass
