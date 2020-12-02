"""
Container for all methods used to choose good Othello moves.
"""
import random

import Game
import GamePiece


class ComputerAI:
    """ Container for all methods used to choose good Othello moves. """

    ''' ========== Constant Class Variables ========== '''

    DIFFICULTY_LEVELS = {
        1:
            {
                'name': 'Random',
                'max_depth': None,
                'probability_returning_random': 1
            },
        2:
            {
                'name': 'Beginner',
                'max_depth': 5,
                'probability_returning_random': 0.75
            },
        3:
            {
                'name': 'Moderate',
                'max_depth': 6,
                'probability_returning_random': 0.5
            },
        4:
            {
                'name': 'Hard',
                'max_depth': 7,
                'probability_returning_random': 0.25
            },
        5:
            {
                'name': 'Expert',
                'max_depth': 8,
                'probability_returning_random': 0
            }
    }

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, difficulty=None):
        self.difficulty = difficulty

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
            return False

        return game.make_move(r, f, game.side_to_move)

    @staticmethod
    def make_move_beginner(game: Game, ai: 'ComputerAI'):
        """
            Either make the minimax-best move or a random move, given the AI's difficulty level (see
            ComputerAI.DIFFICULTY_LEVELS).
        """

        if ComputerAI.DIFFICULTY_LEVELS[ai.difficulty]['probability_returning_random'] > random.random():
            # Make a random move
            return ComputerAI.make_move_random(game, ai)
        else:
            # Make a minimax-best move
            r, f, _ = ComputerAI.minimax(game, ComputerAI.DIFFICULTY_LEVELS[ai.difficulty]['max_depth'],
                                         float('-inf'), float('+inf'), game.side_to_move)

            if None not in (r, f):
                move_made = game.make_move(r, f, game.side_to_move)
                if not move_made:
                    raise RuntimeError('custom error: ComputerAI.minimax() did not generate a valid move')
                return True
            else:
                raise RuntimeError('custom error: no moves found in ComputerAI.minimax()')

    @staticmethod
    def make_move_moderate(game: Game, ai: 'ComputerAI'):
        """
            Either make the minimax-best move or a random move, given the AI's difficulty level (see
            ComputerAI.DIFFICULTY_LEVELS).
        """

        if ComputerAI.DIFFICULTY_LEVELS[ai.difficulty]['probability_returning_random'] > random.random():
            # Make a random move
            return ComputerAI.make_move_random(game, ai)
        else:
            # Make a minimax-best move
            r, f, _ = ComputerAI.minimax(game, ComputerAI.DIFFICULTY_LEVELS[ai.difficulty]['max_depth'],
                                         float('-inf'), float('+inf'), game.side_to_move)

            if None not in (r, f):
                move_made = game.make_move(r, f, game.side_to_move)
                if not move_made:
                    raise RuntimeError('custom error: ComputerAI.minimax() did not generate a valid move')
                return True
            else:
                raise RuntimeError('custom error: no moves found in ComputerAI.minimax()')

    @staticmethod
    def make_move_hard(game: Game, ai: 'ComputerAI'):
        """
            Either make the minimax-best move or a random move, given the AI's difficulty level (see
            ComputerAI.DIFFICULTY_LEVELS).
        """
        if ComputerAI.DIFFICULTY_LEVELS[ai.difficulty]['probability_returning_random'] > random.random():
            # Make a random move
            return ComputerAI.make_move_random(game, ai)
        else:
            # Make a minimax-best move
            r, f, _ = ComputerAI.minimax(game, ComputerAI.DIFFICULTY_LEVELS[ai.difficulty]['max_depth'],
                                         float('-inf'), float('+inf'), game.side_to_move)

            if None not in (r, f):
                move_made = game.make_move(r, f, game.side_to_move)
                if not move_made:
                    raise RuntimeError('custom error: ComputerAI.minimax() did not generate a valid move')
                return True
            else:
                raise RuntimeError('custom error: no moves found in ComputerAI.minimax()')

    @staticmethod
    def make_move_expert(game: Game, ai: 'ComputerAI'):
        """ Make the best move using alpha-beta search. Return True iff move was made successfully. """
        r, f, _ = ComputerAI.minimax(game, ComputerAI.DIFFICULTY_LEVELS[ai.difficulty]['max_depth'],
                                     float('-inf'), float('+inf'), game.side_to_move)

        if None not in (r, f):
            move_made = game.make_move(r, f, game.side_to_move)
            if not move_made:
                raise RuntimeError('custom error: ComputerAI.minimax() did not generate a valid move')
            return True
        else:
            raise RuntimeError('custom error: no moves found in ComputerAI.minimax()')

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
        return random.getrandbits(8)

    @staticmethod
    def minimax(game, depth, alpha, beta, color):
        """
            Preform minimax search on the given Game (return
            move with highest static evaluation `depth` moves
            in the future. Maximizing player must be True or False.

            Credit to:
            https://www.youtube.com/watch?v=l-hh51ncgDI&list=TLPQMjkxMTIwMjBN_bodUBpAxQ&index=1
            (@ 10:26)
        """
        # print(game)
        # time.sleep(0.1)

        if depth == 0:
            # Normally would have to check if game.is_over(), but lines below would make it redundant
            return None, None, ComputerAI.static_eval()

        # Without the following check this function would return +/- infinity in positions
        # where no moves are yielded from generate_all_valid_moves() - no future static eval would
        # beat infinity so computer would always preference first line it finds that forces opponent
        # to skip a move regardless of future outcomes
        if Game.Game.has_no_valid_moves(game, color=color):
            # Credit to: https://stackoverflow.com/a/51323433/7304977
            # No children (this side has no moves). If opponent also has no moves
            # in this position, game is over - return static_eval(). Else, return
            # the best minimax move from perspective of opponent (at same depth)
            if Game.Game.has_no_valid_moves(game, color=color, opponent_to_move=True):
                # No moves for opponent in this position either
                return None, None, ComputerAI.static_eval()

            return ComputerAI.minimax(game, depth, alpha, beta, GamePiece.GamePiece.get_opposite_color(color))

        best_move_r = None
        best_move_f = None
        if color == GamePiece.GamePiece.B_CHAR:
            # -infinity = worst score for maximizing player (black)
            max_eval = float('-inf')
            for r, f in game.try_next_moves(GamePiece.GamePiece.B_CHAR):
                # Best move at next depth irrelevant at this depth (only eval matters)
                _, _, current_eval = ComputerAI.minimax(game, depth-1, alpha, beta, GamePiece.GamePiece.W_CHAR)
                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move_r = r
                    best_move_f = f
                alpha = max(alpha, current_eval)
                if beta <= alpha:
                    break
            return best_move_r, best_move_f, max_eval
        else:
            # +infinity = worst score for minimizing player (white)
            min_eval = float('+inf')
            for r, f in game.try_next_moves(GamePiece.GamePiece.W_CHAR):
                # Best move at next depth irrelevant at this depth (only eval matters)
                _, _, current_eval = ComputerAI.minimax(game, depth-1, alpha, beta, GamePiece.GamePiece.B_CHAR)
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move_r = r
                    best_move_f = f
                beta = min(beta, current_eval)
                if beta <= alpha:
                    break
            return best_move_r, best_move_f, min_eval

    @staticmethod
    def make_move(ai: 'ComputerAI', game: Game):
        """ Call appropriate make_move_...() function based on self.difficulty. """

        if ai.difficulty == 1:
            return ai.make_move_random(game, game.computer_ai)
        elif ai.difficulty == 2:
            return ai.make_move_beginner(game, game.computer_ai)
        elif ai.difficulty == 3:
            return ai.make_move_moderate(game, game.computer_ai)
        elif ai.difficulty == 4:
            return ai.make_move_hard(game, game.computer_ai)
        elif ai.difficulty == 5:
            return ai.make_move_expert(game, game.computer_ai)
        else:
            raise ValueError('custom error: Invalid difficulty in ComputerAI.make_move()')

    ''' ========== Instance Methods ========== '''

    def set_difficulty(self, difficulty):
        if difficulty not in ComputerAI.DIFFICULTY_LEVELS:
            raise ValueError('custom error: Invalid difficulty in ComputerAI.__init__()')

        self.difficulty = difficulty
