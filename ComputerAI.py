"""
Container for all methods used to choose good Othello moves.

==========================
|||     Class Info     |||
==========================

Fields
======
    Constant Class Vars
    -------------------
        TODO

    Regular Class Vars
    ------------------
        TODO

Methods
=======
    Constructor
    -----------
        TODO

    Magic Methods
    -------------
        TODO

    Static Methods
    --------------
        TODO

    Instance Methods
    ----------------
        TODO

"""

import Board


class ComputerAI:
    """ Container for all methods used to choose good Othello moves. """

    ''' ========== Constant Class Variables ========== '''

    DIFFICULTY_LEVELS = {
        1: 'Random',
        2: 'Beginner',
        3: 'Amateur',
        4: 'Club',
        5: 'Expert'
    }
    DEFAULT_DEPTH = 15

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, difficulty=None):
        self.difficulty = None
        self.set_difficulty(difficulty)

    ''' ========== Magic Methods ========== '''

    def __repr__(self):
        """ Return a formal string representation of self.  """

        s = f'<ComputerAI with difficulty = {self.difficulty}>'

    ''' ========== Static Methods ========== '''
    @staticmethod
    def make_move_random(board: Board.Board, side_to_move):
        """ Return a random valid move from given Board, or None if no valid moves exist. """

        pass

    @staticmethod
    def make_move_beginner(board: Board.Board, side_to_move):
        """ Docstring for make_move_() - TODO """

        pass

    @staticmethod
    def make_move_amateur(board: Board.Board, side_to_move):
        """ Docstring for make_move_() - TODO """

        pass

    @staticmethod
    def make_move_club(board: Board.Board, side_to_move):
        """ Docstring for make_move_() - TODO """

        pass

    @staticmethod
    def make_move_expert(board: Board.Board, side_to_move):
        """ Return best move using alpha-beta search DEFAULT_DEPTH moves deep. """

        pass

    @staticmethod
    def static_eval(board: Board.Board, side_to_move):
        """
            Return a float value representing the positional evaluation of the current Board state
            (without look-ahead). Positive numbers mean black is better, positive numbers mean
            white is better.

            # TODO Figure out how to do this
            # Othello strategy series
            # https://www.youtube.com/watch?v=5uwQPpfwSKs
        """

        pass

    ''' ========== Instance Methods ========== '''
    def set_difficulty(self, difficulty):
        if difficulty not in ComputerAI.DIFFICULTY_LEVELS:
            raise ValueError('custom error: Invalid difficulty in ComputerAI.__init__()')

        self.difficulty = difficulty

    def make_move(self, board: Board.Board, side_to_move):
        """ Docstring for make_move() - TODO """

        if self.difficulty == 1:
            self.make_move_random(board, side_to_move)
        elif self.difficulty == 2:
            self.make_move_beginner(board, side_to_move)
        elif self.difficulty == 3:
            self.make_move_amateur(board, side_to_move)
        elif self.difficulty == 4:
            self.make_move_club(board, side_to_move)
        elif self.difficulty == 5:
            self.make_move_expert(board, side_to_move)
        else:
            raise ValueError('custom error: Invalid difficulty in ComputerAI.make_move()')