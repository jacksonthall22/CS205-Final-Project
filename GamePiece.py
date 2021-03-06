"""
`GamePiece` represents a two-colored Othello piece that can be placed in `Tile`s within a `Board`.
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

    ''' ========== Constructor ========== '''

    def __init__(self, side_up=EMPTY_CHAR):
        # Call parent constructor
        super().__init__()

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
        """ Return GamePiece.B_CHAR, GamePiece.W_CHAR, or GamePiece.EMPTY_CHAR depending on self.side_up. """

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

    @staticmethod
    def get_opposite_color(color):
        """ Return the opposite GamePiece color if color is GamePiece.B_CHAR or GamePiece.W_CHAR. """

        if color == GamePiece.B_CHAR:
            return GamePiece.W_CHAR
        else:
            return GamePiece.B_CHAR

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
        """
            Although GamePiece is a GUIElement, there is no need to ever handle a click because its containing
            Board's handle_click() will always be called instead if click occurs inside GamePiece.
        """
        pass
