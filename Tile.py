"""
`Tile` extends `GUIElement` to represent a single square in the board (contains a `GamePiece` and may be highlighted -
see below).

Fields
------
    Instance Vars
    -------------
        game_piece : Represents the piece at this location - either a `GamePiece` object or `None`
        highlight_circle : If True, show small transparent circle or similar visual cue to indicate this Tile in the
                board is currently a valid move
"""

from GamePiece import GamePiece
from GUIElement import GUIElement
import pygame


class Tile(GUIElement):
    """ Tile extends GUIElement to represent a single square in the board. """

    ''' ========== Constant Class Variables ========== '''

    # Factor to scale the GamePiece contained in this Tile by when draw()ing in the GUI
    # Ex. if
    #     tile.width = 100 and
    #     tile.height = 100
    # then game_piece.width, game_piece.height will be calculated and set:
    #     game_piece.width = 75
    #     game_piece.height = 75
    # and the coords of the top-left corner will be calculated such that its bounding box is centered in the bounding
    # box of tile, ex:
    #     game_piece.x_loc = tile.x_loc + tile.width * (1 - 0.75) / 2
    #     game_piece.y_loc = tile.y_loc + tile.width * (1 - 0.75) / 2
    GAME_PIECE_SCALE_FACTOR = 0.75

    GREEN = [15, 85, 15]

    SPACING = 1

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, game_piece=None, highlight_circle=None):
        # Call parent constructor
        super().__init__()

        # Make a new empty GamePiece if appropriate
        if game_piece is None:
            game_piece = GamePiece()

        # Make sure params are of correct type
        assert all((
            type(game_piece) in (GamePiece, type(None)),
            type(highlight_circle) in (bool, type(None)),
            # TODO Might want to add more later
        ))

        self.game_piece = game_piece
        self.highlight_valid_move = highlight_circle
        self.set_game_piece_locations_and_sizes()

    ''' ========== Magic Methods ========== '''

    ''' ========== Static Methods ========== '''

    ''' ========== Instance Methods ========== '''

    def set_game_piece(self, game_piece):
        """ Docstring for set_game_piece() - TODO """

        self.game_piece = game_piece

    def set_game_piece_locations_and_sizes(self):
        """
            Set the bounding box of self.game_piece such that it is centered in the bounding box of self.

            Example
            -------
            If:
                  tile.width = 1000  # (Tile dimensions of 1000x1000px probably unrealistic but just for the example)
                  tile.height = 1000
                  tile.x_loc = 0
                  tile.y_loc = 0
                  GAME_PIECE_SCALE_FACTOR = 0.75
            then these are set automatically for self.game_piece when __init__() is first called:
                  tile.game_piece.width = 750
                  tile.game_piece.height = 750
                  tile.game_piece.x_loc = 125
                  tile.game_piece.y_loc = 125

            Notice that the bounding box of tile.game_piece would then be defined by these coords:

                    (125, 125)      (875, 125)

                    (875, 125)      (875, 875)

            which is exactly centered in the bounding box tile itself:
                (0, 0)                  (0, 1000)


                (1000, 0)               (1000, 1000)
        """

        # Set the width/height
        self.game_piece.width = self.width * Tile.GAME_PIECE_SCALE_FACTOR
        self.game_piece.height = self.height * Tile.GAME_PIECE_SCALE_FACTOR

        # Set the top-left coords (right and down from top left by half of (1 - [scale factor]) / 2)
        self.game_piece.x_loc = self.x_loc + self.width * (1 - Tile.GAME_PIECE_SCALE_FACTOR) / 2
        self.game_piece.y_loc = self.y_loc + self.height * (1 - Tile.GAME_PIECE_SCALE_FACTOR) / 2

    def is_empty(self):
        """ Return True iff the self.game_piece.side_up is None. """
        return self.game_piece.side_up is None

    def draw(self, pygame_screen, row, column):
        """ Docstring for draw(self, pygame_screen, color, x, y, w, h) """
        pygame.draw.rect(pygame_screen, Tile.GREEN, (self.x_loc,
                                                     self.y_loc,
                                                     self.width,
                                                     self.height))
        if not self.is_empty():
            self.game_piece.draw(pygame_screen, row, column)

    def handle_click(self, x_click_loc, y_click_loc):
        """ Docstring for handle_click(self, x_click_loc, y_click_loc):() - TODO """

        # Note: This method doesn't need to actually be implemented.
        #       The only time the `handle_click()` method would need to be called here (on a Tile) is after the
        #       `handle_click()` of the containing Board has been called - all piece placement logic is
        #       located in Board.handle_click(). It cannot be implemented here because from this scope, we don't have
        #       access to the Board's Game object and therefore can't know what color piece to place.
        print("tile")
        return None
