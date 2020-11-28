"""
`GamePiece` represents a two-colored Othello piece that can be placed in `Tile`s within a `Board`.

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

import GUIElement
import pygame


class GamePiece(GUIElement.GUIElement):
    """ """

    ''' ========== Constant Class Variables ========== '''
    # Printed to console when printing boards
    B_DISPLAY_CHAR = '○'
    W_DISPLAY_CHAR = '●'
    EMPTY_DISPLAY_CHAR = ' '

    # Used in backend
    B_CHAR = 'b'
    W_CHAR = 'w'
    EMPTY_CHAR = '-'

    BLACK = [0, 0, 0]
    WHITE = [255, 255, 255]

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, side_up=EMPTY_CHAR):
        # Call parent constructor
        super().__init__()

        assert side_up in (GamePiece.B_CHAR, GamePiece.W_CHAR, GamePiece.EMPTY_CHAR)

        self.side_up = side_up

    ''' ========== Magic Methods ========== '''

    def __str__(self):
        if self.side_up == GamePiece.EMPTY_CHAR or self.side_up is None:
            return GamePiece.EMPTY_DISPLAY_CHAR

        if self.side_up == GamePiece.B_CHAR:
            return GamePiece.B_DISPLAY_CHAR
        elif self.side_up == GamePiece.W_CHAR:
            return GamePiece.W_DISPLAY_CHAR

        return GamePiece.EMPTY_DISPLAY_CHAR

    def __repr__(self):
        """ Docstring for __repr__() - TODO """

        if self.side_up is None:
            return GamePiece.EMPTY_CHAR

        return self.side_up

    ''' ========== Static Methods ========== '''

    @staticmethod
    def get_side_up(game_piece):
        """ :return side_up of GamePiece """
        return game_piece.side_up

    @staticmethod
    def get_display_char(game_piece):
        """ Return the constant char as defined in GamePiece corresponding to game_piece.get_side_up(). """
        if GamePiece.get_side_up(game_piece) == GamePiece.B_CHAR:
            return GamePiece.B_DISPLAY_CHAR
        elif GamePiece.get_side_up(game_piece) == GamePiece.W_CHAR:
            return GamePiece.W_DISPLAY_CHAR
        else:
            return GamePiece.EMPTY_DISPLAY_CHAR

    ''' ========== Instance Methods ========== '''

    def flip(self):
        """ Change the side_up to the opposite color. """
        if self.side_up == GamePiece.B_CHAR:
            self.side_up = GamePiece.W_CHAR
        elif self.side_up == GamePiece.W_CHAR:
            self.side_up = GamePiece.B_CHAR
        else:
            print('warning: GamePiece.flip() called on GamePiece set to EMPTY_CHAR')

    def set_side_up(self, side_up):
        """ Set self.side_up to given value. """
        assert side_up in ('b', 'w')

        self.side_up = side_up

    def draw(self, pygame_screen):
        x_center = int(self.x_loc + self.width // 2)
        y_center = int(self.y_loc + self.width // 2)
        position = (x_center, y_center)
        if self.side_up == GamePiece.B_CHAR:
            pygame.draw.circle(pygame_screen, GamePiece.BLACK, position, int(self.width / 2))
        elif self.side_up == GamePiece.W_CHAR:
            pygame.draw.circle(pygame_screen, GamePiece.WHITE, position, int(self.width / 2))

    def handle_click(self, x_click_loc, y_click_loc):
        """ Docstring for handle_click() - TODO """
        return None
