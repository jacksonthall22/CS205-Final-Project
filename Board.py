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
        assert Board.is_valid_state(self.state)

        # Build board string
        output_string = '┌───┬───┬───┬───┬───┬───┬───┬───┐\n'

        for index, row in enumerate(self.state):
            for col in row:
                if col is None:
                    char_to_fill = Board.EMPTY_CHAR
                elif col.lower() == 'b':
                    char_to_fill = Board.B_CHAR
                elif col.lower() == 'w':
                    char_to_fill = Board.W_CHAR
                else:
                    # Should never reach here - will be helpful for debugging later -JH
                    raise Exception('custom error: Bad formatting of Board.state')

                output_string += f'│ {char_to_fill} '

            if index != len(self.state) - 1:
                # Not the last row, use ├───┼...
                output_string += '│\n├───┼───┼───┼───┼───┼───┼───┼───┤\n'
            else:
                # Last row, use └───┴...
                output_string += '│\n└───┴───┴───┴───┴───┴───┴───┴───┘\n'

        return output_string


    ''' ========== Static Methods ========== '''
    @staticmethod
    def is_valid_state(state):
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
    def set_state(self, new_state):
        """ If new_state is valid, set state to new_state. """
        if Board.is_valid_state(new_state):
            self.state = new_state
        else:
            # Should never reach here - will be helpful for debugging later -JH
            raise ValueError('custom error: Invalid new_state given to Board.set_state()')
