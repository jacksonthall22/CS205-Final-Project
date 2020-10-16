from Board import Board 

class Game:
    ''' ========== Constant Class Variables ========== '''


    ''' ========== Regular Class Variables ========== '''
    

    ''' ========== Constructor ========== '''

    def __init__(self, state=None, turn='b', moves_played=0):
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
            type(moves_played) == int,
            
        ])
        if state is None:
            state = Board.STARTING_STATE

        self.board = Board(state)
        self.turn = turn
        self.moves_played = moves_played
        self.potential_available_white_moves = get_potential_available_white_moves(self.board)
        self.potential_available_black_moves = get_potential_available_black_moves(self.board)


    ''' ========== Magic Methods ========== '''
    def __str__(self):
        """ Print Game metadata and state of self.board to the console. """
        
        # Construct string to be printed
        output_string = ''

        # Show move number
        if self.moves_played == 0:
            output_string += 'It\'s the first move. '
        else:
            output_string += f'It\'s move {self.moves_played + 1}. '

        # Show who's turn it is
        if self.turn == 'b':
            output_string += 'Black to move.\n'
        elif self.turn == 'w':
            output_string += 'White to move.\n'
        else:
            # Should never reach here - will be helpful for debugging later -JH
            raise ValueError('custom error: self.turn isn\'t "b" or "w"')

        # Show state of the board
        output_string += self.board.__str__()

        return output_string


    ''' ========== Static Methods ========== '''

    ''' ========== Instance Methods ========== '''
    def get_potential_available_black_moves(self, b):
        """ Take a Board b and return a 2d list where the element at every index is an int representing the number of white GamePieces neighboring that index (vertically and horizontally). """
        
        # for row_index, row in enumerate(b):
        #     pass
        pass 

    def get_potential_available_white_moves(self, b):
        """ Take a Board b and return a 2d list where the element at every index is an int representing the number of black GamePieces neighboring that index (vertically and horizontally). """
        pass
