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
import random

import Game
import GamePiece
import utility


class ComputerAI:
    """ Container for all methods used to choose good Othello moves. """

    ''' ========== Constant Class Variables ========== '''

    DIFFICULTY_LEVELS = {
        1:
            {
                'name': 'Random',
                'search_depth': None,
                'probability_returning_random': 1
            },
        2:
            {
                'name': 'Beginner',
                'search_depth': 4,
                'probability_returning_random': 0.75
            },
        3:
            {
                'name': 'Amateur',
                'search_depth': 4,
                'probability_returning_random': 0.5
            },
        4:
            {
                'name': 'Club',
                'search_depth': 6,
                'probability_returning_random': 0.25
            },
        5:
            {
                'name': 'Expert',
                'search_depth': 6,
                'probability_returning_random': 0
            }
    }

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
    def make_move_random(game: Game, ai: 'ComputerAI'):
        """ Make a random valid move from given Board, or None if no valid moves exist. """
        r, f, was_only_move = Game.Game.get_random_valid_move(game)
        if None in (r, f):
            return

        game.make_move(r, f, game.side_to_move)

    @staticmethod
    def make_move_beginner(game: Game, ai: 'ComputerAI'):
        """ Docstring for make_move_() - TODO """
        # TODO Comment out when implemented
        ComputerAI.make_move_random(game, ai)

        pass

    @staticmethod
    def make_move_amateur(game: Game, ai: 'ComputerAI'):
        """ Docstring for make_move_() - TODO """
        # TODO Comment out when implemented
        ComputerAI.make_move_random(game, ai)

        pass

    @staticmethod
    def make_move_club(game: Game, ai: 'ComputerAI'):
        """ Docstring for make_move_() - TODO """
        # TODO Comment out when implemented
        ComputerAI.make_move_random(game, ai)

        pass

    @staticmethod
    def make_move_expert(game: Game, ai: 'ComputerAI'):
        """ Make the best move using alpha-beta search. Return True iff move was made successfully. """
        # TODO Comment out when implemented
        # ComputerAI.make_move_random(game, ai)

        r, f, _ = ComputerAI.minimax(game, ComputerAI.DIFFICULTY_LEVELS[ai.difficulty]['search_depth'],
                                     float('-inf'), float('+inf'), False)

        if None not in (r, f):
            move_made = game.make_move(r, f, game.side_to_move)
            if not move_made:
                raise RuntimeError('custom error: CompuerAI.minimax() did not generate a valid move')
            return True
        else:
            print('test: no moves found in ComputerAI.minimax()')

        return False

    @staticmethod
    def static_eval():
        """
            Return a float value representing the positional evaluation of the current Board state
            (without look-ahead). Positive numbers mean black is better, positive numbers mean
            white is better.

            # Othello strategy series
            # https://www.youtube.com/watch?v=5uwQPpfwSKs
        """

        # Generate float from normal distribution (mean = 0, sd = 1)
        return random.normalvariate(0, 1)

    @staticmethod
    def minimax(game, depth, alpha, beta, maximizing_player):
        """
            Preform minimax search on the given Game (return
            move with highest static evaluation `depth` moves
            in the future. Maximizing player must be True or False.

            Credit to:
            https://www.youtube.com/watch?v=l-hh51ncgDI&list=TLPQMjkxMTIwMjBN_bodUBpAxQ&index=1
            (@ 10:26)
        """
        if depth == 0 or Game.Game.is_over(game):
            return None, None, ComputerAI.static_eval()

        # Without the following check this function would return +/- infinity in positions
        # where no moves are yielded from generate_all_valid_moves() - no future static eval would
        # beat infinity so computer would always preference first line it finds that forces opponent
        # to skip a move regardless of future outcomes
        children = ((r, f, Game.Game.get_position_after_move(game, r, f))
                    for r, f in Game.Game.generate_all_valid_moves(game))

        if Game.Game.has_no_valid_moves(game):
            # TODO Make sure skipping moves here produces expected results
            #  Credit to: https://stackoverflow.com/a/51323433/7304977
            # No children (this side has no moves). If opponent also has no moves
            # in this position, game is over - return static_eval(). Else, return
            # the best minimax move from perspective of opponent (at same depth)
            if Game.Game.has_no_valid_moves(game, True):
                # No moves for opponent in this position either
                return None, None, ComputerAI.static_eval()

            return ComputerAI.minimax(game, depth, alpha, beta, not maximizing_player)

        best_move_r = None
        best_move_f = None
        if maximizing_player:
            # -infinity = worst score for maximizing player
            max_eval = float('-inf')
            for r, f, child in children:
                # Best move at next depth irrelevant at this depth (only eval matters)
                _, _, current_eval = ComputerAI.minimax(child, depth-1, alpha, beta, False)
                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move_r = r
                    best_move_f = f
                alpha = max(alpha, current_eval)
                if beta <= alpha:
                    break
            return best_move_r, best_move_f, max_eval
        else:
            # +infinity = worst score for minimizing player
            min_eval = float('+inf')
            children = ((r, f, Game.Game.get_position_after_move(game, r, f))
                        for r, f in Game.Game.generate_all_valid_moves(game))
            for r, f, child in children:
                # Best move at next depth irrelevant at this depth (only eval matters)
                _, _, current_eval = ComputerAI.minimax(child, depth-1, alpha, beta, True)
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move_r = r
                    best_move_f = f
                beta = min(beta, current_eval)
                if beta <= alpha:
                    break
            return best_move_r, best_move_f, min_eval

    ''' ========== Instance Methods ========== '''

    def set_difficulty(self, difficulty):
        if difficulty not in ComputerAI.DIFFICULTY_LEVELS:
            raise ValueError('custom error: Invalid difficulty in ComputerAI.__init__()')

        self.difficulty = difficulty

    def make_move(self, game: Game):
        """ Call appropriate make_move_...() function based on self.difficulty. """

        if self.difficulty == 1:
            return self.make_move_random(game, game.computer_ai)
        elif self.difficulty == 2:
            return self.make_move_beginner(game, game.computer_ai)
        elif self.difficulty == 3:
            return self.make_move_amateur(game, game.computer_ai)
        elif self.difficulty == 4:
            return self.make_move_club(game, game.computer_ai)
        elif self.difficulty == 5:
            return self.make_move_expert(game, game.computer_ai)
        else:
            raise ValueError('custom error: Invalid difficulty in ComputerAI.make_move()')
