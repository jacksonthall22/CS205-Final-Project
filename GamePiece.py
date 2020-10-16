class GamePiece:
    ''' ========== Constant Class Variables ========== '''
    B_CHAR = '○'
    W_CHAR = '●'

    ''' ========== Regular Class Variables ========== '''
    
    ''' ========== Constructor ========== '''
    def __init__(self, side_up='b'):
        self.side_up = side_up

    ''' ========== Magic Methods ========== '''
    def __str__(self):
        return (B_CHAR, W_CHAR)[self.side_up == 'w']

    ''' ========== Static Methods ========== '''
    

    ''' ========== Instance Methods ========== '''
    def flip(self):
        """ Change the side_up to the opposite color. """
        self.side_up = (B_CHAR, W_CHAR)[self.side_up == 'b']
    
    def get_side_up(self):
        """ Return self.side_up. """
        return self.side_up
    
    def set_side_up(self, side_up):
        """ Set self.side_up to given value. """
        assert side_up in ('b', 'w')

        self.side_up = side_up