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

import Game
import GamePiece


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
    def make_move_random(game: Game):
        """ Make a random valid move from given Board, or None if no valid moves exist. """
        r, f, was_only_move = Game.Game.get_random_valid_move(game)
        if None in (r, f):
            return

        game.make_move(r, f, game.side_to_move)

    @staticmethod
    def make_move_beginner(game: Game):
        """ Docstring for make_move_() - TODO """
        # TODO Comment out when implemented
        ComputerAI.make_move_random(game)

        pass

    @staticmethod
    def make_move_amateur(game: Game):
        """ Docstring for make_move_() - TODO """
        # TODO Comment out when implemented
        ComputerAI.make_move_random(game)

        pass

    @staticmethod
    def make_move_club(game: Game):
        """ Docstring for make_move_() - TODO """
        # TODO Comment out when implemented
        ComputerAI.make_move_random(game)

        pass

    @staticmethod
    def make_move_expert(game: Game):
        """ Return best move using alpha-beta search DEFAULT_DEPTH moves deep. """
        # TODO Comment out when implemented
        ComputerAI.make_move_random(game)

        pass

    @staticmethod
    def static_eval(game: Game):
        """
            Return a float value representing the positional evaluation of the current Board state
            (without look-ahead). Positive numbers mean black is better, positive numbers mean
            white is better.

            # TODO Figure out how to do this
            # Othello strategy series
            # https://www.youtube.com/watch?v=5uwQPpfwSKs
        """

        pass

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

        if depth == 0 or game.is_over():
            return ComputerAI.static_eval(game)

        # Without the following check this function would return +/- infinity in positions
        # where no moves are yielded from generate_all_valid_moves() - no future static eval would
        # beat infinity so computer would always preference first line it finds that forces opponent
        # to skip a move regardless of future outcomes
        children = ((r, f, Game.Game.get_position_after_move(game, r, f))
                    for r, f in Game.Game.generate_all_valid_moves(game))
        for _ in children:
            # For/else behavior: execute else iff loop terminates without hitting a break
            break
        else:
            # TODO Make sure skipping moves here produces expected results
            #  Credit to: https://stackoverflow.com/a/51323433/7304977
            # No children (this side has no moves). If opponent also has no moves
            # in this position, game is over - return static_eval(). Else, return
            # the best minimax move from perspective of opponent (at same depth)
            children = ((r, f, Game.Game.get_position_after_move(game, r, f))
                        for r, f in Game.Game.generate_all_valid_moves(game, True))
            for _ in children:
                break
            else:
                return ComputerAI.static_eval(game)

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
        """ Docstring for make_move() - TODO """

        if self.difficulty == 1:
            self.make_move_random(game)
        elif self.difficulty == 2:
            self.make_move_beginner(game)
        elif self.difficulty == 3:
            self.make_move_amateur(game)
        elif self.difficulty == 4:
            self.make_move_club(game)
        elif self.difficulty == 5:
            self.make_move_expert(game)
        else:
            raise ValueError('custom error: Invalid difficulty in ComputerAI.make_move()')
