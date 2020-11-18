import pygame
from Button import Button
from GameGUI import GameGUI
from Layout import Layout
from Game import Game
from GamePiece import GamePiece
import time

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

    in_game_layout = Layout([game, e_in_game])
    gui.update_active_screen(menu_layout)

    title_location = ((X // 2) - (452 // 2), 50)

    in_game = True

    while in_game:
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

        # # Add title image
        SCREEN.fill(BACKGROUND)
        SCREEN.blit(TITLE, title_location)
        gui.draw(SCREEN)

        pygame.display.update()

        if GameGUI.get_active_screen(gui) == in_game_layout:
            current_game = Layout.get_game(GameGUI.get_active_screen(gui))
            if current_game.computer_move():
                time.sleep(1)
                gui.draw(SCREEN)
                pygame.display.update()

        clock.tick(15)


def quit_game():
    pygame.quit()
    quit()


game_menu()
quit_game()
