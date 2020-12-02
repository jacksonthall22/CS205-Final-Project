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

import GamePiece
import GUIElement
import pygame


class Tile(GUIElement.GUIElement):
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
    HIGHLIGHT = [255, 255, 0]

    SPACING = 1

    ''' ========== Constructor ========== '''

    def __init__(self, game_piece=None, highlight_circle=None):
        # Call parent constructor
        super().__init__()

        # Make a new empty GamePiece if appropriate
        if game_piece is None:
            game_piece = GamePiece.GamePiece()

        self.game_piece = game_piece
        self.highlight_valid_move = highlight_circle
        self.set_game_piece_locations_and_sizes()

    ''' ========== Magic Methods ========== '''

    def __repr__(self):
        """ Return a string "[x]" where x is the formal representation of the contained GamePiece. """
        return f'[{repr(self.game_piece)}]'

    ''' ========== Instance Methods ========== '''

    def set_game_piece(self, game_piece):
        """ :param game_piece to make game_piece of the tile """

        self.game_piece = game_piece

    def highlight_tile(self):
        """ Set highlight_valid_move to True """

        self.highlight_valid_move = True

    def remove_highlight(self):
        """ Set highlight_valid_move to False """

        self.highlight_valid_move = False

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
        """ :return True iff there is no game piece in the tile """
        return self.game_piece.side_up is None

    def draw(self, pygame_screen):
        self.set_game_piece_locations_and_sizes()
        if self.highlight_valid_move:
            pygame.draw.rect(pygame_screen, Tile.HIGHLIGHT, (self.x_loc,
                                                             self.y_loc,
                                                             self.width,
                                                             self.height))
            pygame.draw.rect(pygame_screen, Tile.GREEN, (self.x_loc + 6,
                                                         self.y_loc + 6,
                                                         self.width - 12,
                                                         self.height - 12))
        else:
            pygame.draw.rect(pygame_screen, Tile.GREEN, (self.x_loc,
                                                         self.y_loc,
                                                         self.width,
                                                         self.height))
        if not self.is_empty():
            self.game_piece.draw(pygame_screen)

    def handle_click(self, x_click_loc, y_click_loc):
        """
            Although Tile is a GUIElement, there is no need to ever handle a click because its containing Board's
            handle_click() will always be called instead if click occurs inside GamePiece.

            A handle_click() could not be implemented here to place a piece anyway because from this scope, there is
            no access to the Tile's containing (Board's containing) Game object and therefore there is no way to know
            what color GamePiece would need to be placed, nevermind validate the move using functions in Game.
        """
        pass
