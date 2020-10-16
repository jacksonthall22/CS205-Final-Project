from Board import Board

class Game:
    ''' ========== Constant Class Variables ========== '''


    ''' ========== Regular Class Variables ========== '''
    

    ''' ========== Constructor ========== '''
    def __init__(self, state=None, turn='b', movesPlayed=0):
        # In param list here ^, the "='b'" and similar are default arguments, so they
        # can be left out when instantiating Game objects and the args will get defaulted
        # to whatever value is after the '='.
        # ex. usage: 
        #   >>> def foo(bar1=None, bar2=None):
        #   ...     print(bar1)
        #   ...     print(bar2)
        #   >>> foo()
        #   None
        #   None
        #   >>> foo('test')
        #   test
        #   None
        #   >>> foo('test1', 'test2')
        #   test1
        #   test2
        #   >>> foo(bar2='test1', bar1='test2')
        #   test2
        #   test1

        # Make sure params are of correct types
        assert all([
            type(state) in (list, None),
            not empty(state),
            all([len(state[sublist]) == len(state) for sublist in state]),
            turn in ('b', 'w'),
            type(movesPlayed) == int,
            
        ])
        if state is None:
            state = Board.STARTING_STATE

        self.board = Board(state)
        self.turn = turn
        self.movesPlayed = movesPlayed


    ''' ========== Magic Methods ========== '''
    def __str__(self):
        """ Print Game metadata and state of self.board to the console. """
        
        # Construct string to be printed
        outputString = ''

        # Show move number
        if self.movesPlayed == 0:
            outputString += 'It\'s the first move. '
        else:
            outputString += f'It\'s move {self.movesPlayed + 1}. '

        # Show who's turn it is
        if self.turn == 'b':
            outputString += 'Black to move.\n'
        elif self.turn == 'w':
            outputString += 'White to move.\n'
        else:
            # Should never reach here - will be helpful for debugging later -JH
            raise ValueError('custom error: self.turn isn\'t "b" or "w"')

        # Show state of the board
        outputString += self.board.__str__()

        return outputString


    ''' ========== Static Methods ========== '''

    ''' ========== Instance Methods ========== '''
    def moveIsPossible(self, move):
        """ Return True iff move is possible given self.state. """
        
        if self.turn == 'b':
            locationsToCheck = self.potentialPossibleWhiteMoves
        elif self.turn == 'w':
            locationsToCheck = self.potentialPossibleBlackMoves
        else:
            raise ValueError('custom error: self.turn isn\'t "b" or "w"')
        
        for location in locationsToCheck:
            for gamePiece in 

    def makeMove(self, move):
        """ If move is possible, make the move and flip appropriate GamePieces. """
        

    
    def getLegalMoves(self):
        """ Return a list of available moves. """
        if self.turn == 'b':
            # Get legal black moves in current position
            pass
        elif self.turn == 'w':
            # Get legal white moves in current position
            pass
        else:
            raise Exception('custom error: self.turn was not "b" or "w"')
        

