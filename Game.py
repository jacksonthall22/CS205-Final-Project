"""
Game objects extend GUIElement and store any relevant data about an Othello game. It contains all methods related to
Othello game logic (making and validating moves, getting AI's move, etc.).

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
import ComputerAI
import GamePiece
import GUIElement

from copy import deepcopy
import pygame
import random
import time


# noinspection DuplicatedCode
class Game(GUIElement.GUIElement):
    """ Game extends GUIElement, stores relevant metadata about an Othello game. """

    ''' ========== Constant Class Variables ========== '''

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, state=Board.Board.get_starting_state(), side_to_move=GamePiece.GamePiece.B_CHAR, moves_played=0,
                 ai_difficulty=1):
        super().__init__()

        # Make sure params are of correct types
        assert all((
            type(state) in (list, None),
            state,  # Checks that state isn't empty
            all((len(sublist) == len(state) for sublist in state)),
            side_to_move in (GamePiece.GamePiece.B_CHAR, GamePiece.GamePiece.W_CHAR),
            type(moves_played) == int,
            moves_played >= 0,
            ai_difficulty in ComputerAI.ComputerAI.DIFFICULTY_LEVELS
        ))
        self.board = Board.Board(Board.Board.get_starting_state())
        self.side_to_move = side_to_move
        self.moves_played = moves_played
        self.white_score = 0
        self.black_score = 0
        self.set_scores()
        self.x_loc = self.board.x_loc
        self.y_loc = self.board.y_loc
        self.width = self.board.width
        self.height = self.board.height
        self.computer_ai = ComputerAI.ComputerAI(ai_difficulty)

    ''' ========== Magic Methods ========== '''

    def __str__(self, show_valid_moves=False):
        """ Print Game metadata and state of self.board to the console. """

        # Construct string to be printed
        output_string = ''

        # Show move number
        if self.moves_played == 0:
            output_string += 'Welcome to Othello. It\'s the first move. '
        else:
            output_string += f'It\'s move {self.moves_played + 1}. '

        # Show who's turn it is
        if self.side_to_move == GamePiece.GamePiece.B_CHAR:
            output_string += 'Black to move.\n'
        elif self.side_to_move == GamePiece.GamePiece.W_CHAR:
            output_string += 'White to move.\n'
        else:
            # Should never reach here - will be helpful for debugging later -JH
            raise ValueError('custom error: self.turn isn\'t "b" or "w"')

        # Show state of the board
        output_string += self.board.__str__()

        return output_string

    ''' ========== Static Methods ========== '''

    @staticmethod
    def get_flip_ranges(board, rank, file, color):
        """
            If making move of given color at given location, return list of tuple-generators that generate pairs of
            indices in self.board.state to flip when making this move. Returns empty list if this move is not valid
            (cannot flip in any direction).
        """

        # Add every direction in NEIGHBOR_INDICES_RELATIVE (if any) that is a direction this move should flip
        ranges_to_flip = []

        # Immediately invalid if the square is occupied
        if GamePiece.GamePiece.get_side_up(board.state[rank][file].game_piece) != GamePiece.GamePiece.EMPTY_CHAR:
            return ranges_to_flip

        # Immediately invalid if there's no immediate neighboring GamePieces of opposite color
        # if color == GamePiece.GamePiece.B_CHAR and board.num_white_neighbors[rank][file] == 0:
        #     return ranges_to_flip
        # elif color == GamePiece.GamePiece.W_CHAR and board.num_black_neighbors[rank][file] == 0:
        #     return ranges_to_flip

        # Valid iff, on any line starting from state[rank][file] and moving in the direction of an element in
        # NEIGHBOR_INDICES_RELATIVE (treating the tuples like direction vectors), there is 1 or more GamePiece of the
        # opposite color followed by a GamePiece of the same color.
        other_color = GamePiece.GamePiece.get_opposite_color(color)

        # Check for line of >= 1 other_color followed by 1 this_color
        # Check in all 8 directions
        for d_rank, d_file in Board.Board.NEIGHBOR_INDICES_RELATIVE:
            current_rank = rank + d_rank
            current_file = file + d_file

            # Prevent indexing a negative index
            # ie. '12345'[-1] = '5'
            if current_rank < 0 or current_file < 0:
                continue

            try:
                while GamePiece.GamePiece.get_side_up(
                        board.state[current_rank][current_file].game_piece) == other_color:
                    # Increment even before first check
                    current_rank += d_rank
                    current_file += d_file

                    # Prevent indexing a negative index
                    if current_rank < 0 or current_file < 0:
                        continue

                    # Check if flip has been "closed"
                    if GamePiece.GamePiece.get_side_up(board.state[current_rank][current_file].game_piece) == color:
                        # If so, add a generator to the list that generates tuples containing the indices to flip for
                        # this direction

                        if d_rank == 0:
                            # Can't do a range(start, stop, step) if step is 0
                            # rank_range below is a generator (rank, rank, rank, rank, ...) with number of "rank"s equal
                            # to how many tiles are flipping in this direction
                            rank_range = (rank for _ in range(file + d_file, current_file, d_file))
                        else:
                            rank_range = range(rank + d_rank, current_rank, d_rank)

                        if d_file == 0:
                            # See comment above
                            file_range = (file for _ in range(rank + d_rank, current_rank, d_rank))
                        else:
                            file_range = range(file + d_file, current_file, d_file)

                        ranges_to_flip.append(e for e in zip(rank_range, file_range))
                        break
            except IndexError:
                # Invalid if loop tries to access element at an invalid index before `break`ing
                continue

        return ranges_to_flip

    @staticmethod
    def has_valid_moves(game, opponent_to_move: bool = False, color=None):
        """
            Return True iff there is one or more moves in game's current board state. If `color` is given,
            check for moves by that color, else check for moves by game.side_to_move. If opponent_to_move is True,
            check for moves of the opposite color.
        """
        for _ in Game.generate_all_valid_moves(game, opponent_to_move, color):
            return True
        return False

    @staticmethod
    def has_no_valid_moves(game, opponent_to_move: bool = False, color=None):
        """
            Return True iff there are no moves in game's current board state. If `color` is given,
            check for moves by that color, else check for moves by game.side_to_move. If opponent_to_move is True,
            check for moves of the opposite color.
        """
        return not Game.has_valid_moves(game, opponent_to_move, color)

    @staticmethod
    def get_all_valid_moves(game, opponent_to_move: bool = False):
        """
            Return list of all valid moves for the given game. If opponent_to_move
            is True, return list of legal moves as if it were opponent's turn.
        """
        return list(Game.generate_all_valid_moves(game, opponent_to_move))

    @staticmethod
    def generate_all_valid_moves(game, opponent_to_move: bool = False, color=None):
        """
            Yield all valid moves for the given game. If `color` is given, check for moves by that color, else check
            for moves by game.side_to_move. If opponent_to_move is True, check for moves of the opposite color.
        """

        if opponent_to_move:
            # Opposite of `color`, if it's set
            if color is not None:
                color = GamePiece.GamePiece.get_opposite_color(color)
            else:
                # Opposite of game.side_to_move
                color = GamePiece.GamePiece.get_opposite_color(game.side_to_move)
        else:
            if color is None:
                color = game.side_to_move

        for rank in range(len(game.board.state)):
            for file in range(len(game.board.state[0])):
                if Game.is_valid_move(game.board, rank, file, color):
                    yield rank, file

        # This ends up being slower overall
        # if game.side_to_move == GamePiece.GamePiece.B_CHAR:
        #     for rank, file in game.board.indices_with_white_neighbors:
        #         if Game.is_valid_move(game.board, rank, file, side_to_move):
        #             yield rank, file
        # else:
        #     for rank, file in game.board.indices_with_black_neighbors:
        #         if Game.is_valid_move(game.board, rank, file, side_to_move):
        #             yield rank, file

    @staticmethod
    def get_random_valid_move(game):
        """ Return a random valid move as a (rank, file, is_only_move) tuple for the current game.side_to_move. """

        if Game.has_no_valid_moves(game):
            return None, None, None
        else:
            all_valid_moves = Game.get_all_valid_moves(game)
            choice = random.choice(all_valid_moves)
            return choice[0], choice[1], len(all_valid_moves) == 1
            #                            ^ indicates whether move was only move

    @staticmethod
    def get_winner(game):
        black_score = 0
        white_score = 0
        for rank in game.board.state:
            for tile in rank:
                if GamePiece.GamePiece.get_side_up(tile.game_piece) == GamePiece.GamePiece.B_CHAR:
                    black_score += 1
                elif GamePiece.GamePiece.get_side_up(tile.game_piece) == GamePiece.GamePiece.W_CHAR:
                    white_score += 1
        return black_score, white_score

    @staticmethod
    def is_over(game: 'Game'):
        """ Return True iff the board has no empty Tiles or neither player has valid moves. """

        return game.moves_played == 60 or Game.has_no_valid_moves(game) and Game.has_no_valid_moves(game, True)

    @staticmethod
    def is_valid_move(board, rank, file, color):
        """ Return True iff placing piece of given color at given location in given board is valid. """

        # Validate that get_flip_ranges() does not return empty list
        # In Python not [] == True
        return not not Game.get_flip_ranges(board, rank, file, color)

    @staticmethod
    def get_position_after_move(game, rank, file, color=None):
        if color is None:
            color = game.side_to_move

        new_game = deepcopy(game)

        new_game.make_move(rank, file, color)

        return new_game

    ''' ========== Instance Methods ========== '''

    def game_loop(self):
        """ Allow user to play this game until completion. """

        if self.side_to_move:
            player_moves_first = self.side_to_move == 'b'
        else:
            # Get side to move
            player_color_prompt = input('Would you like to play black or white? Black always moves first. (b/w)\n>>> ')

            while player_color_prompt not in ('b', 'w'):
                player_color_prompt = input('Please enter "b" or "w":\n>>> ')

            player_moves_first = player_color_prompt == 'b'

        # Loop until game ends
        while not Game.is_over(self):
            print(self)

            move_was_made = False

            # Loop until user enters valid move
            while not move_was_made:
                # Get move in algebraic notation
                # Check if there is only one possible move (only used when it's Computer's move)
                is_only_move = False

                if self.side_to_move == GamePiece.GamePiece.B_CHAR and player_moves_first \
                        or self.side_to_move == GamePiece.GamePiece.W_CHAR and not player_moves_first:
                    if Game.has_valid_moves(self):
                        algebraic_move = input('Enter black\'s move:\n>>> ')
                    else:
                        input('You have no legal moves. Press enter to continue.\n>>> ')
                        self.skip_move()
                        continue
                elif self.side_to_move == GamePiece.GamePiece.W_CHAR and player_moves_first \
                        or self.side_to_move == GamePiece.GamePiece.B_CHAR and not player_moves_first:
                    r, f, is_only_move = Game.get_random_valid_move(self)
                    algebraic_move = Board.Board.indices_to_algebraic(r, f)
                else:
                    raise ValueError('custom error: game.side_to_move not equal to GamePiece.B_CHAR or GamePiece.W_CHAR'
                                     'in Game.game_loop()')

                # Loop until user enters valid move in AN
                # Note: will never break into this loop for iteration where it's computer's move - no need to validate
                while not Board.Board.is_valid_algebraic_move(algebraic_move):
                    algebraic_move = input('Please enter a move in Algebraic Notation (like "a1", "e6", '
                                           'etc.):\n>>> ')

                # Show that computer is thinking if it's their turn
                if self.side_to_move == GamePiece.GamePiece.W_CHAR and player_moves_first \
                        or self.side_to_move == GamePiece.GamePiece.B_CHAR and not player_moves_first:
                    if algebraic_move is None:
                        print('Computer has no moves. It\'s your move again.')
                        self.skip_move()
                        continue
                    elif is_only_move:
                        print('Computer is thinking...', end='')
                        time.sleep(1)
                        print(f' Computer was forced to play {algebraic_move}.')
                    else:
                        print('Computer is thinking.', end='')
                        time.sleep(1)
                        print('.', end='')
                        time.sleep(1)
                        print('.', end='')
                        time.sleep(1)
                        print(f' Computer played {algebraic_move}.')

                # Make the move
                move_rank, move_file = Board.Board.algebraic_to_indices(algebraic_move)
                move_was_made = self.make_move(move_rank, move_file, self.side_to_move)

                # If no move made, it was invalid - continue
                if not move_was_made:
                    print('That wasn\'t a valid move. ', end='')

            # Update scores after a move was made
            self.set_scores()

        # Show board position after final move and display winner
        print(self.board)

        # Set the final scores
        if self.black_score > self.white_score:
            print(f'Game over. Black wins {self.black_score} - {self.white_score}')
        elif self.white_score > self.black_score:
            print(f'Game over. White wins {self.black_score} - {self.white_score}')
        else:
            print(f'Game over. It\'s a tie. {self.black_score} - {self.white_score}')

    def set_scores(self):
        """
            Set black_score and white_score for the current Board state. Only use on initialization - otherwise values
            are updated when moves are made.
        """

        for rank in self.board.state:
            for tile in rank:
                if GamePiece.GamePiece.get_side_up(tile.game_piece) == GamePiece.GamePiece.B_CHAR:
                    self.black_score += 1
                elif GamePiece.GamePiece.get_side_up(tile.game_piece) == GamePiece.GamePiece.W_CHAR:
                    self.white_score += 1

    def skip_move(self):
        """ Skip the side_to_move's move. """
        self.side_to_move = GamePiece.GamePiece.get_opposite_color(self.side_to_move)

    def make_move(self, rank, file, color):
        """
            If move is valid, update state, and side_to_move, then return True. If move is not valid, return False.
        """
        # Return if there are no valid directions to flip
        flip_ranges = Game.get_flip_ranges(self.board, rank, file, color)

        if len(flip_ranges) == 0:
            return False

        self.board.place_piece(rank, file, color)

        # Flip all the necessary lines of GamePieces & return True
        for flip_range in flip_ranges:
            self.flip_all_in_range(flip_range)

        self.moves_played += 1
        self.side_to_move = GamePiece.GamePiece.get_opposite_color(self.side_to_move)
        return True

    def try_next_moves(self, color):
        """
            For all valid moves by the given color in the current position, make the move
            and yield, then un-make the move.
        """
        for rank, file in Game.generate_all_valid_moves(self, color=color):
            flip_ranges = [list(gen) for gen in Game.get_flip_ranges(self.board, rank, file, color)]

            # Note: This try block should not error - in ComputerAI.minimax(), pruning a branch causes for loop to
            #       break, which would stop this generator from un-making the move if there were no finally clause
            try:
                # Do piece placement and flippage
                self.moves_played += 1
                self.board.place_piece(rank, file, color)
                for flip_range in flip_ranges:
                    self.flip_all_in_range(flip_range)

                yield rank, file
            finally:
                # Undo piece placement and flippage
                self.moves_played -= 1
                self.board.remove_piece(rank, file)
                for flip_range in flip_ranges:
                    self.flip_all_in_range(flip_range)

    # def update_board_meta_lists(self, rank, file, color, is_new_piece):
    #     """ Docstring for update_num_neighbors_lists() - TODO """
    #
    #     if color == GamePiece.GamePiece.W_CHAR:
    #         # Flipping black -> white
    #         for d_rank, d_file in Board.Board.NEIGHBOR_INDICES_RELATIVE:
    #             try:
    #                 self.board.num_white_neighbors[rank + d_rank][file + d_file] += 1
    #
    #                 # Only decrement opposite color if a GamePiece was already at this index
    #                 if not is_new_piece:
    #                     self.board.num_black_neighbors[rank + d_rank][file + d_file] -= 1
    #
    #                     # Remove these indices from indices_with_black_neighbors if it falls to 0 in num_black_neighbors
    #                     if self.board.num_black_neighbors[rank + d_rank][file + d_file] == 0 \
    #                             and (rank + d_rank, file + d_file) in self.board.indices_with_black_neighbors:
    #                         self.board.indices_with_black_neighbors.remove((rank + d_rank, file + d_file))
    #
    #                 # Remove these indices from indices_with_white_neighbors if it falls to 0 in num_white_neighbors
    #                 if self.board.num_white_neighbors[rank + d_rank][file + d_file] > 0:
    #                     self.board.indices_with_white_neighbors.add((rank + d_rank, file + d_file))
    #             except IndexError:
    #                 continue
    #
    #     elif color == GamePiece.GamePiece.B_CHAR:
    #         # Flipping white -> black
    #         for d_rank, d_file in Board.Board.NEIGHBOR_INDICES_RELATIVE:
    #             try:
    #                 self.board.num_black_neighbors[rank + d_rank][file + d_file] += 1
    #
    #                 # Only decrement opposite color if a GamePiece was already at this index
    #                 if not is_new_piece:
    #                     self.board.num_white_neighbors[rank + d_rank][file + d_file] -= 1
    #
    #                     # Remove these indices from indices_with_black_neighbors if it falls to 0 in num_black_neighbors
    #                     if self.board.num_white_neighbors[rank + d_rank][file + d_file] == 0 \
    #                             and (rank + d_rank, file + d_file) in self.board.indices_with_white_neighbors:
    #                         self.board.indices_with_white_neighbors.remove((rank + d_rank, file + d_file))
    #
    #                 # Remove these indices from indices_with_white_neighbors if it falls to 0 in num_white_neighbors
    #                 if self.board.num_black_neighbors[rank + d_rank][file + d_file] > 0:
    #                     self.board.indices_with_black_neighbors.add((rank + d_rank, file + d_file))
    #             except IndexError:
    #                 continue
    #     else:
    #         raise ValueError('custom error: Game.flip() called with range containing different colored GamePieces')

    def flip(self, rank, file):
        """
            Take indices rank, file and update board.num_<black/white>_neighbors and
            board.indices_with_<black/white>_neighbors.
        """

        self.board.state[rank][file].game_piece.flip()
        # self.update_board_meta_lists(rank, file,
        #                              GamePiece.GamePiece.get_side_up(self.board.state[rank][file].game_piece),
        #                              False)

    def flip_all_in_range(self, indices_to_flip):
        """
            Take an iterable of tuples of (rank, file) indices to flip and update board.num_<black/white>_neighbors and
            board.indices_with_<black/white>_neighbors.
        """

        for rank, file in indices_to_flip:
            self.flip(rank, file)

    def indices_in_direction(self, rank, file, direction):
        """
            Yield pairs of indies starting (exclusive) from given location [rank][file] and ending (inclusive) at the
            last pair of indices that will not throw an IndexError when indexing into self.board.state.
        """

        # Unpack direction tuple (will be something from Board.NEIGHBOR_INDICES_RELATIVE)
        d_rank, d_file = direction

        current_rank = rank + d_rank
        current_file = file + d_file

        while current_rank in range(Board.Board.DEFAULT_BOARD_SIZE) and current_file in range(
                Board.Board.DEFAULT_BOARD_SIZE):
            try:
                # See if indexing this location throws ValueError
                # noinspection PyStatementEffect
                self.board.state[current_rank][current_file]

                # If not, yield the pair of indices
                yield current_rank, current_file

                current_rank += 1
                current_file += 1
            except ValueError:
                # Else stop generation
                return

    def computer_move(self):
        """ :return True iff computer makes a move, makes move for computer """

        if self.side_to_move == GamePiece.GamePiece.W_CHAR and not Game.is_over(self):
            return ComputerAI.ComputerAI.make_move(self.computer_ai, self)

        return False

    def draw(self, pygame_screen):
        for row in self.board.state:
            for tile in row:
                tile.remove_highlight()

        if self.side_to_move == GamePiece.GamePiece.B_CHAR:
            for r, f in Game.generate_all_valid_moves(self):
                self.board.state[r][f].highlight_tile()

        self.board.draw(pygame_screen)
        position = (150, 300)
        if self.side_to_move == GamePiece.GamePiece.B_CHAR:
            pygame.draw.circle(pygame_screen, GamePiece.GamePiece.BLACK, position, 25)
        elif self.side_to_move == GamePiece.GamePiece.W_CHAR:
            pygame.draw.circle(pygame_screen, GamePiece.GamePiece.WHITE, position, 25)

    def handle_click(self, x_click_loc, y_click_loc):
        """ If the click location was on a Tile in self.board, make a move at that Tile if it is valid. """
        # Check every Tile in the board to see if click occurred inside its bounding box (might have occurred in a gap
        # between them - in this case loop ends and nothing more is handled, as expected)
        if self.side_to_move == GamePiece.GamePiece.B_CHAR:
            for rank_index, rank in enumerate(self.board.state):
                for file_index, tile in enumerate(rank):
                    # If the click is inside this Tile and making a move there is a valid move, make move there
                    if GUIElement.GUIElement.click_is_inside(tile, x_click_loc, y_click_loc):
                        if Game.is_valid_move(self.board, rank_index, file_index, self.side_to_move):
                            self.make_move(rank_index, file_index, self.side_to_move)
                            tile.handle_click(x_click_loc, y_click_loc)

        return None
