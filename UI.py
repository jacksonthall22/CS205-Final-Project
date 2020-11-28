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

    s_menu = Button(text="START")
    s_menu.x_loc = (X // 4) - 125
    s_menu.y_loc = (4 * Y // 5) - 50
    s_menu.width = 300
    s_menu.height = 100

    e_menu = Button(text="EXIT")
    e_menu.x_loc = (3 * X // 4) - 125
    e_menu.y_loc = (4 * Y // 5) - 50
    e_menu.width = 300
    e_menu.height = 100
    menu_layout = Layout([s_menu, e_menu])

    e_in_game = Button(text="EXIT")
    e_in_game.x_loc = X // 12
    e_in_game.y_loc = (3 * Y // 4)
    e_in_game.width = 300
    e_in_game.height = 100

    in_game_layout = Layout([game, e_in_game])

    e_end = Button(text="EXIT")
    e_end.x_loc = (3 * X // 4) - 125
    e_end.y_loc = (4 * Y // 5) - 50
    e_end.width = 300
    e_end.height = 100

    ng_end = Button(text="NEW GAME")
    ng_end.x_loc = (X // 4) - 125
    ng_end.y_loc = (4 * Y // 5) - 50
    ng_end.width = 300
    ng_end.height = 100
    end_layout = Layout([ng_end, e_end])

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
                    gui.update_active_screen(in_game_layout)
                    in_game_layout.new_game()
                    title_location = (20, 20)

        # Add title image
        SCREEN.fill(BACKGROUND)
        if GameGUI.get_active_screen(gui) == in_game_layout:
            font = pygame.font.Font('freesansbold.ttf', 65)
            text_surf = font.render("\'s Turn", True, BLACK)
            text_pos = [180, 265]
            SCREEN.blit(text_surf, text_pos)
        SCREEN.blit(TITLE, title_location)
        gui.draw(SCREEN)

        if GameGUI.get_active_screen(gui) == end_layout:
            b_score, w_score = Game.get_winner(current_game)
            if w_score > b_score:
                dif = w_score - b_score
                text = "You lost by: " + str(dif) + " points"
            elif w_score < b_score:
                dif = b_score - w_score
                text = "You won by: " + str(dif) + " points"
            else:
                text = "Tie game"
            font = pygame.font.Font('freesansbold.ttf', 60)
            text_surf = font.render(text, True, Button.TEXT_COLOR)
            text_pos = [(X // 2) - 300, (Y // 2)]
            SCREEN.blit(text_surf, text_pos)

        pygame.display.update()

        if GameGUI.get_active_screen(gui) == in_game_layout:
            current_game = Layout.get_game(GameGUI.get_active_screen(gui))
            if len(Game.get_all_valid_moves(current_game)) == 0:
                current_game.skip_move()
            if Game.is_over(current_game):
                gui.update_active_screen(end_layout)
                title_location = ((X // 2) - (452 // 2), 50)
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
