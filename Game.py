"""
Game objects extend GUIElement and store any relevant data about an Othello game.
"""

from Board import Board
from GamePiece import GamePiece
from GUIElement import GUIElement
import random
import time


class Game(GUIElement):
    """ Game extends GUIElement, stores relevant metadata about an Othello game. """

    ''' ========== Constant Class Variables ========== '''

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, state=Board.get_starting_state(), side_to_move=GamePiece.B_CHAR, moves_played=0):
        # Explanation of default parameters as used above      ^here                          ^and here
        # https://www.programiz.com/python-programming/function-argument

        # Call parent constructor
        super().__init__()

        # Make sure params are of correct types
        assert all((
            type(state) in (list, None),
            state,  # Checks that state isn't empty
            all((len(sublist) == len(state) for sublist in state)),
            side_to_move in (GamePiece.B_CHAR, GamePiece.W_CHAR),
            type(moves_played) == int,
            moves_played >= 0,
        ))

        self.board = Board(state)
        self.side_to_move = side_to_move
        self.moves_played = moves_played

    ''' ========== Magic Methods ========== '''

    def __str__(self, show_valid_moves=False):
        """ Print Game metadata and state of self.board to the console. """

        # Construct string to be printed
        output_string = ''

        # Show move number
        if self.moves_played == 0:
            output_string += 'It\'s the first move. '
        else:
            output_string += f'It\'s move {self.moves_played + 1}. '

        # Show who's turn it is
        if self.side_to_move == GamePiece.B_CHAR:
            output_string += 'Black to move.\n'
        elif self.side_to_move == GamePiece.W_CHAR:
            output_string += 'White to move.\n'
        else:
            # Should never reach here - will be helpful for debugging later -JH
            raise ValueError('custom error: self.turn isn\'t "b" or "w"')

        # Show state of the board
        output_string += self.board.__str__()

        return output_string

    ''' ========== Static Methods ========== '''

    @staticmethod
    def game_loop(game):
        """ Docstring for game_loop() - TODO """

        player_color_prompt = input('Would you like to play black or white? Black always moves first. (b/w)\n>>> ')

        while player_color_prompt not in ('b', 'w'):
            player_color_prompt = input('Please enter "b" or "w":\n>>> ')

        player_moves_first = player_color_prompt == 'b'

        # Loop until game ends
        while not game.is_over():
            print(game)

            move_was_made = False

            # Loop until user enters valid move
            while not move_was_made:
                # Get move in algebraic notation
                if game.side_to_move == GamePiece.B_CHAR:
                    if player_moves_first:
                        algebraic_move = input('Enter black\'s move:\n>>> ')
                    else:
                        r, f = game.get_random_valid_move()
                        algebraic_move = Board.indices_to_algebraic(r, f)
                elif game.side_to_move == GamePiece.W_CHAR:
                    if not player_moves_first:
                        algebraic_move = input('Enter white\'s move:\n>>> ')
                    else:
                        r, f = game.get_random_valid_move()
                        algebraic_move = Board.indices_to_algebraic(r, f)
                else:
                    raise ValueError('custom error: game.side_to_move not equal to GamePiece.B_CHAR or GamePiece.W_CHAR'
                                     'in Game.game_loop()')

                # Loop until user enters valid move in AN
                # Note: will never break into this loop for iteration where it's computer's move - no need to validate
                while not Board.is_valid_algebraic_move(algebraic_move):
                    algebraic_move = input('Please enter a move in Algebraic Notation (like "a1", "e6", '
                                           'etc.):\n>>> ')

                # Show that computer is thinking if it's their turn
                if game.side_to_move == GamePiece.W_CHAR and player_moves_first \
                        or game.side_to_move == GamePiece.B_CHAR and not player_moves_first:
                    print('Computer is thinking.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print(f' the computer played {algebraic_move}.')

                # Make the move
                move_rank, move_file = Board.algebraic_to_indices(algebraic_move)
                move_was_made = game.make_move(move_rank, move_file, game.side_to_move)

                # If no move made, it was invalid - continue
                if not move_was_made:
                    print('That wasn\'t a valid move. ', end='')

        # Show board position after final move and display winner
        print(game.board)
        black_score, white_score = game.get_winner()
        if black_score > white_score:
            print(f'Game over. Black wins {black_score} - {white_score}')
        elif white_score > black_score:
            print(f'Game over. White wins {black_score} - {white_score}')
        else:
            print(f'It\'s a tie. {black_score} - {white_score}')

    ''' ========== Instance Methods ========== '''

    def get_random_valid_move(self):
        """ Docstring for get_random_valid_move() - TODO """

        return random.choice(self.get_all_valid_moves())

    def get_all_valid_moves(self):
        """ Docstring for get_all_valid_moves() - TODO """

        valid_moves = []

        for rank in range(8):
            for file in range(8):
                if self.is_valid_move(rank, file, self.side_to_move):
                    valid_moves.append((rank, file))

        return valid_moves

    def is_over(self):
        """ Docstring for play_game() - TODO """

        # TODO Make this smarter
        return self.moves_played == 60

    def get_winner(self):
        """ Docstring for get_winner() - TODO """

        black_count = 0
        white_count = 0

        for rank in range(8):
            for file in range(8):
                if self.board.state[rank][file].game_piece.get_side_up() == GamePiece.B_CHAR:
                    black_count += 1
                elif self.board.state[rank][file].game_piece.get_side_up() == GamePiece.W_CHAR:
                    white_count += 1

        return black_count, white_count

    def make_move(self, rank, file, color):
        """
            If move is valid, update state, num_<black/white>_neighbors, indices_with_<black/white>_neighbors,
            and side_to_move, then return True. If move does not flip any tiles, don't make the move and return False.
        """

        # Return if there are no valid directions to flip
        flip_ranges = self.get_flip_ranges(rank, file, color)
        if not flip_ranges:
            # This move does not flip any other pieces = not valid
            return False

        self.board.place_piece(rank, file, color)
        self.update_num_board_meta_lists(rank, file, color, True)

        # Flip all the necessary lines of GamePieces & return True
        for flip_range in flip_ranges:
            self.flip_all_in_range(flip_range)

        self.moves_played += 1
        self.side_to_move = (GamePiece.B_CHAR, GamePiece.W_CHAR)[self.side_to_move == GamePiece.B_CHAR]

        return True

    def update_num_board_meta_lists(self, rank, file, color, is_new_piece):
        """ Docstring for update_num_neighbors_lists() - TODO """

        if color == GamePiece.W_CHAR:
            # Flipping black -> white
            for d_rank, d_file in Board.NEIGHBOR_INDICES_RELATIVE:
                try:
                    self.board.num_white_neighbors[rank + d_rank][file + d_file] += 1

                    # Only decrement opposite color if a GamePiece was already at this index
                    if not is_new_piece:
                        self.board.num_black_neighbors[rank + d_rank][file + d_file] -= 1

                        # TODO Can probably make more efficient - may add and remove same element from indices_... list
                        # Remove these indices from indices_with_black_neighbors if it falls to 0 in num_black_neighbors
                        if self.board.num_black_neighbors[rank + d_rank][file + d_file] == 0\
                                and (rank + d_rank, file + d_file) in self.board.indices_with_black_neighbors:
                            self.board.indices_with_black_neighbors.remove((rank + d_rank, file + d_file))

                    # Remove these indices from indices_with_white_neighbors if it falls to 0 in num_white_neighbors
                    if self.board.num_white_neighbors[rank + d_rank][file + d_file] > 0:
                        self.board.indices_with_white_neighbors.add((rank + d_rank, file + d_file))
                except IndexError:
                    continue

        elif color == GamePiece.B_CHAR:
            # Flipping white -> black
            for d_rank, d_file in Board.NEIGHBOR_INDICES_RELATIVE:
                try:
                    self.board.num_black_neighbors[rank + d_rank][file + d_file] += 1

                    # Only decrement opposite color if a GamePiece was already at this index
                    if not is_new_piece:
                        self.board.num_white_neighbors[rank + d_rank][file + d_file] -= 1

                        # Remove these indices from indices_with_black_neighbors if it falls to 0 in num_black_neighbors
                        if self.board.num_white_neighbors[rank + d_rank][file + d_file] == 0 \
                                and (rank + d_rank, file + d_file) in self.board.indices_with_white_neighbors:
                            self.board.indices_with_white_neighbors.remove((rank + d_rank, file + d_file))


                    # Remove these indices from indices_with_white_neighbors if it falls to 0 in num_white_neighbors
                    if self.board.num_black_neighbors[rank + d_rank][file + d_file] > 0:
                        self.board.indices_with_black_neighbors.add((rank + d_rank, file + d_file))
                except IndexError:
                    continue
        else:
            raise ValueError('custom error: Game.flip() called with range containing different colored GamePieces')

    def flip(self, rank, file):
        """
            Take indices rank, file and update board.num_<black/white>_neighbors and
            board.indices_with_<black/white>_neighbors.
        """

        self.board.state[rank][file].game_piece.flip()
        self.update_num_board_meta_lists(rank, file, self.board.state[rank][file].game_piece.get_side_up(), False)

    def get_flip_ranges(self, rank, file, color):
        """
            If making move of given color at given location, return list of tuple-generators that generate pairs of
            indices in self.board.state to flip when making this move. Returns empty list if this move is not valid
            (cannot flip in any direction).
        """

        # Add every direction in NEIGHBOR_INDICES_RELATIVE (if any) that is a direction this move should flip
        ranges_to_flip = []

        # Immediately invalid if it's not `color`'s turn
        if self.side_to_move != color:
            return ranges_to_flip

        # Immediately invalid if the square is occupied
        if self.board.state[rank][file].game_piece.get_side_up() != GamePiece.EMPTY_CHAR:
            return ranges_to_flip

        # Immediately invalid if there's no immediate neighboring GamePieces of opposite color
        if color == GamePiece.B_CHAR and self.board.num_white_neighbors[rank][file] == 0:
            return ranges_to_flip
        elif color == GamePiece.W_CHAR and self.board.num_black_neighbors[rank][file] == 0:
            return ranges_to_flip

        # Valid iff, on any line starting from state[rank][file] and moving in the direction of an element in
        # NEIGHBOR_INDICES_RELATIVE (treating the tuples like direction vectors), there is 1 or more GamePiece of the
        # opposite color followed by a GamePiece of the same color.
        if self.side_to_move == GamePiece.B_CHAR:
            other_color = GamePiece.W_CHAR
        elif self.side_to_move == GamePiece.W_CHAR:
            other_color = GamePiece.B_CHAR
        else:
            raise ValueError(f'custom error: self.side_to_move not GamePiece.B_CHAR ("{GamePiece.B_CHAR}") or '
                             f'GamePiece.W_CHAR ("{GamePiece.W_CHAR}") in Game.is_valid_move()')

        # Check for line of >= 1 other_color followed by 1 this_color
        # Check in all 8 directions
        for d_rank, d_file in Board.NEIGHBOR_INDICES_RELATIVE:
            current_rank = rank + d_rank
            current_file = file + d_file

            try:
                while self.board.state[current_rank][current_file].game_piece.get_side_up() == other_color:
                    # Increment even before first check
                    current_rank += d_rank
                    current_file += d_file

                    # Check if flip has been "closed"
                    if self.board.state[current_rank][current_file].game_piece.get_side_up() == self.side_to_move:
                        # If so, add a generator that generates tuples containing the indices to flip for this direction

                        # TODO Can probably make more efficient (fewer if/else checks)
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

        if not ranges_to_flip:
            return False

        return ranges_to_flip

    def is_valid_move(self, rank, file, color):
        """ Return True iff placing piece of given color at given location in self.board.state is valid. """

        # Validate that get_flip_ranges() does not return empty list
        # In Python empty list = False
        return not not self.get_flip_ranges(rank, file, color)

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

        while current_rank in range(Board.DEFAULT_BOARD_SIZE) and current_file in range(Board.DEFAULT_BOARD_SIZE):
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

    def draw(self):
        # TODO
        pass
