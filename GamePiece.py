class GamePiece:
    ''' ========== Constant Class Variables ========== '''
    B_CHAR = '○'
    W_CHAR = '●'

    ''' ========== Regular Class Variables ========== '''
    
    ''' ========== Constructor ========== '''
    def __init__(self, sideUp='b'):
        self.sideUp = sideUp

    ''' ========== Magic Methods ========== '''
    def __str__(self):
        return (B_CHAR, W_CHAR)[sideUp == 'w']

    ''' ========== Static Methods ========== '''
    

    ''' ========== Instance Methods ========== '''
    def flip(self):
        """ Change the sideUp to the opposite color. """
        sideUp = [B_CHAR, W_CHAR][sideUp == 'b']
    
    def getSideUp(self):
        """ Return sideUp. """
        return sideUp
    
    def setSideUp(self, sideUp):
        """ Set sideUp to given value. """
        assert sideUp in ('b', 'w')

        self.sideUp = sideUp