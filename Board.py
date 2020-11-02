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
        TODO update this
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

from GamePiece import GamePiece
from GUIElement import GUIElement
from Tile import Tile


class Board(GUIElement):
    """ Board extends GUIElement, represents an Othello board and stores  """

    ''' ========== Constant Class Variables ========== '''
    
    DEFAULT_BOARD_SIZE = 8

    # (delta_r, delta_f) tuples in this list correspond to the cells neighboring a state[r][f]
    # (ie. state[r + delta_r][f + delta_f])
    # When checking for neighbors using this list, must use try/except to catch index errors for any cells on the
    # perimeter of board
    NEIGHBOR_INDICES_RELATIVE = [
        (-1, -1), (-1,  0), (-1,  1),  # 0   1   2
        ( 0, -1),           ( 0,  1),  # 3       4
        ( 1, -1), ( 1,  0), ( 1,  1)   # 5   6   7
    ]

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, state=None):
        # Call parent constructor
        super().__init__()


        self.state = None
        self.num_black_neighbors = None
        self.num_white_neighbors = None
        self.indices_with_black_neighbors = None
        self.indices_with_white_neighbors = None
        self.set_state(state)

    ''' ========== Magic Methods ========== '''

    def __str__(self, show_coords=True):
        # Quick check to make sure board is correct dimensions and
        # only contains 'b', 'w', or None in every square
        # (assert statements throw an AssertionError if given expression is False)
        assert Board.is_valid_state(self.state)

        # Build board string
        output_string = '┌───┬───┬───┬───┬───┬───┬───┬───┐\n'

        for rank_index, rank in enumerate(self.state):
            for file_index, tile in enumerate(rank):
                if tile.game_piece.get_side_up() == GamePiece.EMPTY_CHAR:
                    char_to_fill = GamePiece.EMPTY_DISPLAY_CHAR
                elif tile.game_piece.get_side_up() == GamePiece.B_CHAR:
                    char_to_fill = GamePiece.B_DISPLAY_CHAR
                elif tile.game_piece.get_side_up() == GamePiece.W_CHAR:
                    char_to_fill = GamePiece.W_DISPLAY_CHAR
                else:
                    # Should never reach here - will be helpful for debugging later -JH
                    raise Exception(f'custom error: Bad formatting of Board.state (tile {tile} at '
                                    f'state[{rank_index}][{file_index}])')

                output_string += f'│ {char_to_fill} '

            if rank_index != len(self.state) - 1:
                # Not the last row, use ├───┼...
                output_string += '│\n├───┼───┼───┼───┼───┼───┼───┼───┤\n'
            else:
                # Last row, use └───┴...
                output_string += '│\n└───┴───┴───┴───┴───┴───┴───┴───┘\n'

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
        """ Docstring for is_valid_algebraic_move() - TODO """

        return algebraic_move in (f + r for f in 'abcdefgh' for r in '12345678')

    @staticmethod
    def algebraic_to_indices(algebraic_move):
        """ Docstring for algebraic_to_indices() - TODO """

        # TODO remove later
        assert Board.is_valid_algebraic_move(algebraic_move)

        return '87654321'.find(algebraic_move[1]), 'abcdefgh'.find(algebraic_move[0])

    @staticmethod
    def indices_to_algebraic(rank, file):
        """ Docstring for indices_to_algebraic() - TODO """

        assert rank in '12345678' and file in 'abcdefgh'

        return 'abcdefgh'[file] + '12345678'[rank]

    @staticmethod
    def get_blank_state():
        """ Return fully initialized Board where all Tiles' GamePieces are set to GamePiece.EMPTY_CHAR. """
        
        return [[Tile(GamePiece()) for _ in range(Board.DEFAULT_BOARD_SIZE)] for _ in range(Board.DEFAULT_BOARD_SIZE)]

    @staticmethod
    def get_starting_state():
        """ Return fully initialized Board where Tiles' GamePieces are set to starting Othello configuration. """

        return [
            [Tile(GamePiece()) for _ in range(Board.DEFAULT_BOARD_SIZE)],
            [Tile(GamePiece()) for _ in range(Board.DEFAULT_BOARD_SIZE)],
            [Tile(GamePiece()) for _ in range(Board.DEFAULT_BOARD_SIZE)],
            [Tile(GamePiece()) for _ in range(3)]
                + [Tile(GamePiece(GamePiece.W_CHAR)), Tile(GamePiece(GamePiece.B_CHAR))]
                + [Tile(GamePiece()) for _ in range((Board.DEFAULT_BOARD_SIZE-2) // 2)],
            [Tile(GamePiece()) for _ in range((Board.DEFAULT_BOARD_SIZE-2) // 2)]
                + [Tile(GamePiece(GamePiece.B_CHAR)), Tile(GamePiece(GamePiece.W_CHAR))]
                + [Tile(GamePiece()) for _ in range((Board.DEFAULT_BOARD_SIZE-2) // 2)],
            [Tile(GamePiece()) for _ in range(Board.DEFAULT_BOARD_SIZE)],
            [Tile(GamePiece()) for _ in range(Board.DEFAULT_BOARD_SIZE)],
            [Tile(GamePiece()) for _ in range(Board.DEFAULT_BOARD_SIZE)]
        ]

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
                all((tile.game_piece.get_side_up() in (GamePiece.B_CHAR, GamePiece.W_CHAR, GamePiece.EMPTY_CHAR)
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

        assert neighbor_color in (GamePiece.B_CHAR, GamePiece.W_CHAR)

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
                        if state[rank_index + d_rank_index][file_index + d_file_index].game_piece.get_side_up() == \
                                neighbor_color:
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

    ''' ========== Instance Methods ========== '''

    def set_state(self, new_state):
        """ If new_state is valid, set state to new_state. """
        if Board.is_valid_state(new_state):
            self.state = new_state

            # Two 2d lists: see docs at the top
            self.num_black_neighbors = Board.get_num_neighbors(self.state, GamePiece.B_CHAR)
            self.num_white_neighbors = Board.get_num_neighbors(self.state, GamePiece.W_CHAR)

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

        if self.state[rank][file].game_piece.get_side_up() == GamePiece.EMPTY_CHAR:
            self.state[rank][file].game_piece.set_side_up(color)

        else:
            raise ValueError('custom error: invalid [rank][file] location given to Board.place_piece()')

    def draw(self):
        # TODO
        pass
