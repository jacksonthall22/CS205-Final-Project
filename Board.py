class Board:
    ''' ========== Constant Class Variables ========== '''
    B_CHAR = '○'
    W_CHAR = '●'
    EMPTY_CHAR = ' '
    BLANK_STATE = [[None for file in range(8)] for rank in range(8)]
    STARTING_STATE = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'w', 'b', None, None, None],
        [None, None, None, 'b', 'w', None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
    ]

    ''' ========== Regular Class Variables ========== '''


    ''' ========== Constructor ========== '''
    def __init__(self, state=BLANK_STATE):
        self.state = state


    ''' ========== Magic Methods ========== '''
    def __str__(self):
        # Quick check to make sure board is correct dimensions and
        # only contains 'b', 'w', or None in every square
        # (assert statements throw an AssertionError if given expression is False)
        assert Board.isValidState(self.state)

        # Build board string
        outputString = '┌───┬───┬───┬───┬───┬───┬───┬───┐\n'

        for index, row in enumerate(self.state):
            for col in row:
                if col is None:
                    charToFill = Board.EMPTY_CHAR
                elif col.lower() == 'b':
                    charToFill = Board.B_CHAR
                elif col.lower() == 'w':
                    charToFill = Board.W_CHAR
                else:
                    # Should never reach here - will be helpful for debugging later -JH
                    raise Exception('custom error: Bad formatting of Board.state')

                outputString += f'│ {charToFill} '

            if index != len(self.state) - 1:
                # Not the last row, use ├───┼...
                outputString += '│\n├───┼───┼───┼───┼───┼───┼───┼───┤\n'
            else:
                # Last row, use └───┴...
                outputString += '│\n└───┴───┴───┴───┴───┴───┴───┴───┘\n'

        return outputString


    ''' ========== Static Methods ========== '''
    @staticmethod
    def isValidState(state):
        """
            Return true iff given state is an 8x8 2d list with sublists containing 
            only 'b', 'w', or None.
        """
        return all([
            type(state) == list,
            len(state) == 8,
            all([type(row) == list for row in state]),
            all([len(row) == 8 for row in state]),
            all([all([col in ['b', 'w', None] for col in row]) for row in state]),
        ])


    ''' ========== Instance Methods ========== '''
    def setState(self, newState):
        """ If newState is valid, set state to newState. """
        if Board.isValidState(newState):
            self.state = newState
        else:
            # Should never reach here - will be helpful for debugging later -JH
            raise ValueError('custom error: Invalid newState given to Board.setState()')