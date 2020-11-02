import pygame, sys
from pygame.locals import *

''' Initialize pygame and clock'''
pygame.init()
clock = pygame.time.Clock()

''' Define main colors '''
GREEN = [15, 85, 15]
BLACK = [0, 0, 0]
BACKGROUND = [146, 196, 125]
BUTTON_COLOR = [239, 239, 239]

''' Load images '''
programIcon = pygame.image.load('icon.png')
TITLE = pygame.image.load('title.png')

''' Set window icon '''
pygame.display.set_icon(programIcon)

''' Create main game window, change window title '''
X = 1040
Y = 560
SCREEN = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Othello')

''' Main Loop to display each tile '''
''' Parameters needed to draw each tile '''
WIDTH = 64
HEIGHT = 64
START_LEFT = 500
START_TOP = 15
SPACING = 2

# TODO change '8' to the size of the board object
def draw_board():
    for row in range(8):
        for column in range(8):
            pygame.draw.rect(SCREEN, GREEN, (START_LEFT + (SPACING * column) + (WIDTH * column),
                                             START_TOP + (SPACING * row) + (HEIGHT * row),
                                             WIDTH,
                                             HEIGHT))


def create_button(text, x, y, w, h, if_pressed=None):
    """ Create a button with: text, x position, y position, width, height, and the function called when pressed """

    mouse_position = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    pygame.draw.rect(SCREEN, BUTTON_COLOR, (x, y, w, h))
    if x+w > mouse_position[0] > x and y+h > mouse_position[1] > y:
        if mouse_press[0] and if_pressed is not None:
            if_pressed()

    font = pygame.font.Font('freesansbold.ttf', 48)
    t = font.render(text, True, BLACK, BUTTON_COLOR)
    r = t.get_rect()
    r.center = ((x + (w / 2)), (y + (h / 2)))
    SCREEN.blit(t, r)


def game_menu():
    """ Wait for event on game menu screen: either start a game or exit """

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        # Add title image
        SCREEN.fill(BACKGROUND)
        SCREEN.blit(TITLE, ((X // 2) - (452 // 2), 50))

        # Add buttons
        create_button('START', (X // 4) - 125, (4 * Y // 5) - 50, 300, 100, play_game)
        create_button('EXIT', (3 * X // 4) - 125, (4 * Y // 5) - 50, 300, 100, quit_game)
        # TODO remove after full implementation
        # REMOVE COMMENT TO TEST BUTTON (Causes issues with other buttons)
        # create_button('TEST WIN SCREEN', X // 2 - 250, Y//2 - 50, 500, 100, win_screen)

        pygame.display.update()
        clock.tick(15)


def play_game():
    """ Main event loop for the game: either exit or choose a tile to play on """
    close = False

    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        SCREEN.fill(BACKGROUND)
        SCREEN.blit(TITLE, (20, 20))

        # TODO change this to be each tile in the board
        draw_board()
        create_button('EXIT', X // 12, (Y // 2), 300, 100, quit_game)

        # TODO Having issues with this getting stuck in recursive loop and crashing, implement later if time permits
        #create_button('MENU', X//9, (4 * Y // 8), 300, 100, game_menu)

        pygame.display.update()
        clock.tick(60)


def win_screen():
    """ Win screen event loop wait for: new game or exit game """

    SCREEN.fill(BACKGROUND)
    large = pygame.font.Font('freesansbold.ttf', 80)
    win_t = large.render('YOU WON', True, BLACK, BACKGROUND)
    win_r = win_t.get_rect()
    win_r.center = ((X // 2), (Y // 2))
    SCREEN.blit(win_t, win_r)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        SCREEN.blit(TITLE, ((X // 2) - (452 // 2), 50))
        create_button('NEW GAME', (X // 4) - 125, (3 * Y // 4) - 50, 300, 100, play_game)
        create_button('EXIT', (3 * X // 4) - 125, (3 * Y // 4) - 50, 300, 100, quit_game)

        pygame.display.update()
        clock.tick(15)


def quit_game():
    pygame.quit()
    quit()


game_menu()
quit_game()
