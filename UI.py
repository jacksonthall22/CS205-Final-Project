import pygame, sys
from pygame.locals import *
from Button import Button
from GameGUI import GameGUI
from Layout import Layout
from Board import Board
from Game import  Game
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


def create_button(text, xy_wh, if_pressed=None):
    """ Create a button with: text, x position, y position, width, height, and the function called when pressed """

    pygame.draw.rect(SCREEN, BUTTON_COLOR, (xy_wh[0], xy_wh[1], xy_wh[2], xy_wh[3]))
    font = pygame.font.Font('freesansbold.ttf', 48)
    t = font.render(text, True, BLACK, BUTTON_COLOR)
    r = t.get_rect()
    r.center = ((xy_wh[0] + (xy_wh[2] / 2)), (xy_wh[1] + (xy_wh[3] / 2)))
    SCREEN.blit(t, r)


def game_menu():
    """ Wait for event on game menu screen: either start a game or exit """
    gui = GameGUI()
    game = Game()

    start = Button(text="START")
    start.x_loc = (X // 4) - 125
    start.y_loc = (4 * Y // 5) - 50
    start.width = 300
    start.height = 100
    e_menu = Button(text="EXIT")
    e_menu.x_loc = (3 * X // 4) - 125
    e_menu.y_loc = (4 * Y // 5) - 50
    e_menu.width = 300
    e_menu.height = 100
    menu_layout = Layout([start, e_menu])



    e_in_game = Button(text="EXIT")
    e_in_game.x_loc = X // 12
    e_in_game.y_loc = (3 * Y // 4)
    e_in_game.width = 300
    e_in_game.height = 100
    board = Board(state=Board.get_starting_state())

    in_game_layout = Layout([game, e_in_game])
    gui.update_active_screen(menu_layout)

    title_location = ((X // 2) - (452 // 2), 50)

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                action = gui.handle_click(mouse_position[0], mouse_position[1])
                if action == "EXIT":
                    quit_game()
                elif action == "START":
                    gui.update_active_screen(in_game_layout)
                    title_location = (20, 20)
                elif action == 'NEW GAME':
                    # TODO create new game object
                    gui.update_active_screen(in_game_layout)
                    title_location = ((X // 2) - (452 // 2), 50)
                #GameGUI.get_active_screen().handle_click(mouse_position[0], mouse_position[1])
        #         if start_xy_wh[0] < mouse_position[0] < start_xy_wh[0] + start_xy_wh[2] and \
        #                 start_xy_wh[1] < mouse_position[1] < start_xy_wh[1] + start_xy_wh[3]:
        #             play_game()
        #         if exit_xy_wh[0] < mouse_position[0] < exit_xy_wh[0] + exit_xy_wh[2] and \
        #                 exit_xy_wh[1] < mouse_position[1] < exit_xy_wh[1] + exit_xy_wh[3]:
        #             quit_game()
        #         if win_xy_wh[0] < mouse_position[0] < win_xy_wh[0] + win_xy_wh[2] and \
        #                 win_xy_wh[1] < mouse_position[1] < win_xy_wh[1] + win_xy_wh[3]:
        #             win_screen()
        #
        # # Add title image
        SCREEN.fill(BACKGROUND)
        SCREEN.blit(TITLE, title_location)
        gui.draw(SCREEN)

        # # Add buttons
        # start_xy_wh = [(X // 4) - 125, (4 * Y // 5) - 50, 300, 100]
        # create_button('START', start_xy_wh, play_game)
        # exit_xy_wh = [(3 * X // 4) - 125, (4 * Y // 5) - 50, 300, 100]
        # create_button('EXIT', exit_xy_wh, quit_game)
        # # TODO remove after full implementation
        # # REMOVE COMMENT TO TEST BUTTON (Causes issues with other buttons)
        # win_xy_wh = [X // 2 - 250, Y//2 - 50, 500, 100]
        # create_button('TEST WIN SCREEN', win_xy_wh, win_screen)


        pygame.display.update()
        clock.tick(15)


def play_game():
    """ Main event loop for the game: either exit or choose a tile to play on """
    close = False

    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                if exit_xy_wh[0] < mouse_position[0] < exit_xy_wh[0] + exit_xy_wh[2] and \
                        exit_xy_wh[1] < mouse_position[1] < exit_xy_wh[1] + exit_xy_wh[3]:
                    quit_game()

        SCREEN.fill(BACKGROUND)
        SCREEN.blit(TITLE, (20, 20))

        # TODO change this to be each tile in the board
        draw_board()
        exit_xy_wh = [X // 12, (3 * Y // 4), 300, 100]
        create_button('EXIT', exit_xy_wh, quit_game)

        # TODO Having issues with this getting stuck in recursive loop and crashing, implement later if time permits
        # We will also need to determine how to create a fresh new game object to do this
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
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                if new_game_xy_wh[0] < mouse_position[0] < new_game_xy_wh[0] + new_game_xy_wh[2] and \
                        new_game_xy_wh[1] < mouse_position[1] < new_game_xy_wh[1] + new_game_xy_wh[3]:
                    play_game()
                if exit_xy_wh[0] < mouse_position[0] < exit_xy_wh[0] + exit_xy_wh[2] and \
                        exit_xy_wh[1] < mouse_position[1] < exit_xy_wh[1] + exit_xy_wh[3]:
                    quit_game()

        SCREEN.blit(TITLE, ((X // 2) - (452 // 2), 50))
        new_game_xy_wh = [(X // 4) - 125, (3 * Y // 4) - 50, 300, 100]
        create_button('NEW GAME', new_game_xy_wh, play_game)
        exit_xy_wh = [(3 * X // 4) - 125, (3 * Y // 4) - 50, 300, 100]
        create_button('EXIT', exit_xy_wh, quit_game)

        pygame.display.update()
        clock.tick(15)


def quit_game():
    pygame.quit()
    quit()


game_menu()
quit_game()
