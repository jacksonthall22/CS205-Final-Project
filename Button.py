from GUIElement import GUIElement
import pygame


class Button(GUIElement):
    """ Button extends GUIElement to represent a button on the screen. """

    ''' ========== Constant Class Variables ========== '''
    BUTTON_COLOR = [239, 239, 239]
    TEXT_COLOR = [0, 0, 0]

    ''' ========== Regular Class Variables ========== '''

    ''' ========== Constructor ========== '''

    def __init__(self, text=None, color=None):
        # Call parent constructor
        super().__init__()

        if color is None:
            color = Button.BUTTON_COLOR
        assert all((
            type(text) in (str, type(None)),
            type(color) in (list, tuple, type(None))
        ))

        self.text = text
        self.color = color

    ''' ========== Magic Methods ========== '''

    ''' ========== Static Methods ========== '''

    ''' ========== Instance Methods ========== '''

    def draw(self, screen):
        x = self.x_loc
        y = self.y_loc
        w = self.width
        h = self.height

        pygame.draw.rect(screen, self.color, (x, y, w, h))
        font = pygame.font.Font('freesansbold.ttf', 48)
        t = font.render(self.text, True, Button.TEXT_COLOR, self.color)
        r = t.get_rect()
        r.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(t, r)

    def handle_click(self, x_click_loc, y_click_loc):
        """ Docstring for handle_click(self, x_click_loc, y_click_loc):() - return text for next step """
        return self.text
