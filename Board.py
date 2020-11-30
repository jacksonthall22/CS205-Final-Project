"""
The `Board` class represents an Othello board. Since `Board` objects need to contain more metadata 
than just the state of the board, like the methods needed to validate and make moves, the actual 
state of the game board is an instance variable called `state`.

The `state` variable is a square 2d list of length DEFAULT_BOARD_SIZE where sublists represent ranks (rows) and
elements in sublists are Tiles that optionally contain a `GamePiece` (if no `GamePiece` is in the Tile, the type of
`tile.gamePiece` will be None.

In the board state below, every rank (row) and file (column) is labeled with two characters - the first is the
letter or number that would conventionally be used to refer to that line of squares. Most games using a chess-like
board of squares use Algebraic Notation (AN) to transcribe games. You can get the gist here:
https://en.wikipedia.org/wiki/Algebraic_notation_(chess)#/media/File:SCD_algebraic_notation.svg.

The second numbers represent the index locations in the `Board`'s `state` that would be used to access the `GamePiece`
object stored there. Recall how double indexing works: ((1, 2), (3, 4))[0][1] = (1, 2)[1] = 2.

Also notice that the two values for ranks increase in opposite directions—this is because a1 is conventionally on the
bottom-left corner of the board from the perspective of the first player to make a move (black for Othello), whereas
when the board is printed rank-by-rank, the 0th rank in `state` will print on the top. Therefore using both naming
schemes and providing functions to convert moves AN and rank-file forms is convenient for the GUI and backend.

Here's a blank board state for reference (with empty Tiles):

        ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
  8/[0] │      │      │      │      │      │      │      │      │
        │      │      │      │      │      │      │      │      │
        ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
  7/[1] │      │      │      │      │      │      │      │      │
        │      │      │      │      │      │      │      │      │
        ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
  6/[2] │      │      │      │      │      │      │      │      │
        │      │      │      │      │      │      │      │      │
        ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
  5/[3] │      │      │      │      │      │      │      │ "h5" │  <—— "h5" when speaking and playing over-the-board
        │      │      │      │      │      │      │      │[3][7]│  <—— `b.state[3][7]` for a `Board b`
        ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
  4/[4] │      │      │      │      │      │      │      │      │
        │      │      │      │      │      │      │      │      │
        ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
  3/[5] │      │      │      │      │      │      │      │      │
        │      │      │      │      │      │      │      │      │
        ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
  2/[6] │      │      │      │      │      │      │      │      │
        │      │      │      │      │      │      │      │      │
        ├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
  1/[7] │      │      │      │      │      │      │      │      │
        │      │      │      │      │      │      │      │      │
        └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
          a/[0]  b/[1]  c/[2]  d/[3]  e/[4]  f/[5]  g/[6]  h/[7]

Fields
------
    Constant Class Vars
    -------------------
        B_CHAR : Character to print to terminal in board spaces containing black `GamePieces`
        W_CHAR : Character to print to terminal in board spaces containing white `GamePieces`
        EMPTY_CHAR : Character to print to terminal in board spaces containing no `GamePiece`
    Instance Vars
    -------------
        state : Current state of the board as a 2d list of `Tile` objects, each of which
                optionally contains a `GamePiece` object (see `Tile` class documentation)
        num_black_neighbors: 2d list where each element contains an int equal to the number of black GamePieces
                neighboring the corresponding element in state
        num_white_neighbors: 2d list where each element contains an int equal to the number of white GamePieces
                neighboring the corresponding element in state

Methods
-------
    TODO

"""
import copy

import GamePiece
import GUIElement
import Tile


class Board(GUIElement.GUIElement):
    """ Board extends GUIElement, represents an Othello board and stores  """

    ''' ========== Constant Class Variables ========== '''

    DEFAULT_BOARD_SIZE = 8

    # (delta_r, delta_f) tuples in this list correspond to the cells neighboring a state[r][f]
    # (ie. state[r + delta_r][f + delta_f])
    # When checking for neighbors using this list, must use try/except to catch index errors for any cells on the
    # perimeter of board
    NEIGHBOR_INDICES_RELATIVE = [
        (-1, -1), (-1, 0), (-1, 1),  # 0   1   2
        (0, -1), (0, 1),  # 3       4
        (1, -1), (1, 0), (1, 1)  # 5   6   7
    ]

    # Number of pixels gap between ranks/files in the GUI's Board
    GUI_TILE_GAP_SIZE = 2.5

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, state=None, x_loc=500, y_loc=15, width=528, height=528):
        # Call parent constructor
        super().__init__(x_loc, y_loc, width, height)

        # All these set to None for now before being set in set_state()
        # If not set to None first PyCharm gives warning for adding instance variables outside __init__()
        self.state = None
        self.num_black_neighbors = None
        self.num_white_neighbors = None
        self.indices_with_black_neighbors = None
        self.indices_with_white_neighbors = None
        self.set_state(state)
        self.set_tile_locations_and_sizes()

    ''' ========== Magic Methods ========== '''

    def __str__(self, show_coords=True):
        # Quick check to make sure board is correct dimensions and
        # only contains 'b', 'w', or None in every square
        # (assert statements throw an AssertionError if given expression is False)
        assert Board.is_valid_state(self.state)

        # Build board string
        output_string = ''

        # Add left margin padding if coords are being displayed
        if show_coords:
            output_string += '   '

        output_string += '┌───┬───┬───┬───┬───┬───┬───┬───┐\n'

        for rank_index, rank in enumerate(self.state):
            if show_coords:
                output_string += f' {"87654321"[rank_index]} '

            output_string += f'| {" | ".join((GamePiece.GamePiece.get_display_char(tile.game_piece) for tile in rank))} |\n'

            if rank_index != len(self.state) - 1:
                # Not the last row, use ├───┼───...

                # Add left margin padding if showing coords
                if show_coords:
                    output_string += '   '

                output_string += '├───┼───┼───┼───┼───┼───┼───┼───┤\n'
            else:
                # Last row, use └───┴───...

                # Add left margin padding if showing coords
                if show_coords:
                    output_string += '   '

                output_string += '└───┴───┴───┴───┴───┴───┴───┴───┘\n'

        if show_coords:
            output_string += '     a   b   c   d   e   f   g   h\n'

        return output_string

    def __repr__(self):
        """ Print all metadata for this object. """

        # Header
        r = 'Board __repr__()\n'
        r += '----------------\n'

        # Super's __repr__()
        r += '  super().__repr__(): ' + super().__repr__() + '\n'

        r += '  state: [\n'
        for rank in self.state:
            r += '    ' + ', '.join(str(tile.game_piece) for tile in rank) + '\n'
        r += '  ]\n'

        r += '  num_black_neighbors: [\n'
        for rank in self.num_black_neighbors:
            r += '    ' + ', '.join(str(i) for i in rank) + '\n'
        r += '  ]\n'

        r += '  indices_with_black_neighbors: {\n'
        r += '    ' + ', '.join(str(coord) for coord in self.indices_with_black_neighbors) + '\n'
        r += '  }\n'

        r += '  num_white_neighbors: [\n'
        for rank in self.num_white_neighbors:
            r += '    ' + ', '.join(str(i) for i in rank) + '\n'
        r += '  ]\n'

        r += '  indices_with_white_neighbors: {\n'
        r += '    ' + ', '.join(str(coord) for coord in self.indices_with_white_neighbors) + '\n'
        r += '  }\n'

        return r

    ''' ========== Static Methods ========== '''

    @staticmethod
    def is_valid_algebraic_move(algebraic_move):
        """ Return True iff given algebraic_move is formatted correctly for an 8x8 board. """

        return algebraic_move in (f + r for f in 'abcdefgh' for r in '12345678')

    @staticmethod
    def algebraic_to_indices(algebraic_move):
        """
            Return the (rank, file) location corresponding to the given algebraic_move. If algebraic_move is None,
            return (None, None).
        """

        if not algebraic_move:
            return None, None

        return '87654321'.find(algebraic_move[1]), 'abcdefgh'.find(algebraic_move[0])

    @staticmethod
    def indices_to_algebraic(rank, file):
        """
            Return the algebraic location corresponding to the given (rank, file) location. If rank and file are None,
            return None.
        """

        if rank is None and file is None:
            return None

        return 'abcdefgh'[file] + '87654321'[rank]

    @staticmethod
    def get_blank_state():
        """ Return fully initialized Board where all Tiles' GamePieces are set to GamePiece.EMPTY_CHAR. """

        return [[Tile.Tile(GamePiece.GamePiece()) for _ in range(Board.DEFAULT_BOARD_SIZE)] for _ in
                range(Board.DEFAULT_BOARD_SIZE)]

    @staticmethod
    def get_starting_state():
        """ Return fully initialized Board where Tiles' GamePieces are set to starting Othello configuration. """

        return Board.get_state_from_strings([
            '--------',
            '--------',
            '--------',
            '---wb---',
            '---bw---',
            '--------',
            '--------',
            '--------'
        ])

    @staticmethod
    def get_state_from_strings(state_str):
        """
            Take a list of strings that contain any of GamePiece.B_CHAR, GamePiece.W_CHAR, GamePiece.EMPTY_CHAR and
            return a 2d list of Tiles with GamePieces corresponding to

            ex. to generate the starting state:
                start_state_str = [
                    '--------',
                    '--------',
                    '--------',
                    '---wb---',
                    '---bw---',
                    '--------',
                    '--------',
                    '--------'
                ]
                start_state = Board.get_state_from_strings(start_state_str)
        """

        assert all((
            len(state_str) == 8,
            len(state_str[0]) == 8,
            all((c in (GamePiece.GamePiece.B_CHAR, GamePiece.GamePiece.W_CHAR, GamePiece.GamePiece.EMPTY_CHAR) for rank
                 in state_str for c in rank))
        ))

        state = []
        for rank_index, rank in enumerate(state_str):
            state.append([])
            for file_index, color in enumerate(rank):
                state[rank_index].append(Tile.Tile(GamePiece.GamePiece(color)))

        return state

    @staticmethod
    def is_valid_state(state):
        """
            Return true iff given state is a square 2d list of size DEFAULT_BOARD_SIZE with sublists
            containing only GamePiece.B_CHAR, GamePiece.W_CHAR, or GamePiece.EMPTY_CHAR.

            Note: Does not check for "islands" of pieces, which could not arise in a normal Othello game, nor whether
            the state could actually have been reached from the standard Othello starting position (too hard)
        """
        return all((
            type(state) == list,
            len(state) == Board.DEFAULT_BOARD_SIZE,
            all((type(rank) == list for rank in state)),
            all((len(rank) == Board.DEFAULT_BOARD_SIZE for rank in state)),
            all((
                all((
                    GamePiece.GamePiece.get_side_up(tile.game_piece) in (
                    GamePiece.GamePiece.B_CHAR, GamePiece.GamePiece.W_CHAR, GamePiece.GamePiece.EMPTY_CHAR)
                    for tile in rank))
                for rank in state
            )),
        ))

    @staticmethod
    def get_num_neighbors(state, neighbor_color):
        """
            Return 2d list L such that every L[r][f] index is an int equal to the number of GamePieces of the given
            color neighboring state[r][f] (ie. Tiles at state[r + delta_r][f + delta_f] for
            (delta_r, delta_f) in NEIGHBOR_INDEXES_RELATIVE). If state is None, return None.
        """

        assert neighbor_color in (GamePiece.GamePiece.B_CHAR, GamePiece.GamePiece.W_CHAR)

        # Return None if there is no `state` to build the list from
        if state is None:
            return None

        num_neighbors = []

        for rank_index, rank in enumerate(state):
            num_neighbors.append([])

            for file_index, tile in enumerate(rank):  # ("tile" not a typo)
                # `Loop 1`: Looping on Tiles in state

                # No neighbors found yet at this index yet
                num_neighbors[rank_index].append(0)

                # Check all the neighboring cells
                for d_rank_index, d_file_index in Board.NEIGHBOR_INDICES_RELATIVE:
                    # `Loop 2`: Check every neighbor of this Tile
                    try:
                        # Try indexing the neighbor at given location relative to the Tile in `Loop 1`
                        # Will throw IndexError for any Tile on the perimeter of state
                        if GamePiece.GamePiece.get_side_up(
                                state[rank_index + d_rank_index][file_index + d_file_index].game_piece) \
                                == neighbor_color:
                            num_neighbors[rank_index][file_index] += 1
                    except IndexError:
                        continue

        return num_neighbors

    @staticmethod
    def get_indices_with_neighbors(num_neighbors_lst):
        """ Return a `set` of tuples (r, f) such that num_neighbors_lst[r][f] > 0. """

        indices_with_neighbors = set()

        for rank_index, rank in enumerate(num_neighbors_lst):
            for file_index, num_neighbors in enumerate(rank):
                if num_neighbors > 0:
                    indices_with_neighbors.add((rank_index, file_index))

        return indices_with_neighbors

    @staticmethod
    def is_full(state):
        """ Return True iff state does not have any Tiles with empty GamePieces. """

        for rank in state:
            for tile in rank:
                if GamePiece.GamePiece.get_side_up(tile.game_piece) == GamePiece.GamePiece.EMPTY_CHAR:
                    return False

        return True

    ''' ========== Instance Methods ========== '''

    def set_tile_locations_and_sizes(self):
        """
            Set the locations and sizes of all Tiles in self.state to align appropriately with the bounding box of self.
        """

        # Set all tile.x_loc, tile.y_loc for tile in rank for rank in self.state
        tile_widths = (self.width - 7 * Board.GUI_TILE_GAP_SIZE) / 8
        tile_heights = (self.height - 7 * Board.GUI_TILE_GAP_SIZE) / 8

        current_y_loc = self.y_loc

        for rank_index, rank in enumerate(self.state):
            # Reset x coord on every new row
            current_x_loc = self.x_loc

            for file_index, tile in enumerate(rank):
                tile.x_loc = current_x_loc
                tile.y_loc = current_y_loc
                tile.width = tile_widths
                tile.height = tile_heights

                current_x_loc += tile_widths + Board.GUI_TILE_GAP_SIZE

            # Increment y after every row
            current_y_loc += tile_heights + Board.GUI_TILE_GAP_SIZE

    def set_state(self, new_state):
        """ If new_state is valid, set state to new_state. """
        if Board.is_valid_state(new_state):
            self.state = new_state

            # Two 2d lists: see docs at the top
            self.num_black_neighbors = Board.get_num_neighbors(self.state, GamePiece.GamePiece.B_CHAR)
            self.num_white_neighbors = Board.get_num_neighbors(self.state, GamePiece.GamePiece.W_CHAR)

            # Two 1d sets: contains tuples of (rank, file) indices where
            # self.num_<white/black>_neighbors[rank][file] > 0
            # Ex. for starting position:
            #     self.indices_with_black_neighbors = {(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (3, 5), ... (5, 5)}
            # Note: Python sets have O(1) insert, delete, and `x in s` operations
            self.indices_with_black_neighbors = Board.get_indices_with_neighbors(self.num_white_neighbors)
            self.indices_with_white_neighbors = Board.get_indices_with_neighbors(self.num_white_neighbors)
        else:
            # Should never reach here - will be helpful for debugging later
            raise ValueError('custom error: Invalid new_state given to Board.set_state()')

    def place_piece(self, rank, file, color):
        """ Set the GamePiece of the Tile at the given location to the given color. Assumes move already validated. """

        if GamePiece.GamePiece.get_side_up(self.state[rank][file].game_piece) == GamePiece.GamePiece.EMPTY_CHAR:
            self.state[rank][file].game_piece.set_side_up(color)

        else:
            raise ValueError('custom error: invalid [rank][file] location given to Board.place_piece()')

    def draw(self, pygame_screen):
        for row in self.state:
            for column in row:
                column.draw(pygame_screen)

    def handle_click(self, x_click_loc, y_click_loc):
        return None
