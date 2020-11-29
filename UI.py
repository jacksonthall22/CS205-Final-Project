import pygame
import Button
import GameGUI
import Layout
import Game
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
    gui = GameGUI.GameGUI()
    game = Game.Game()

    s_menu = Button.Button(text="START")
    s_menu.x_loc = (X // 4) - 125
    s_menu.y_loc = (4 * Y // 5) - 50
    s_menu.width = 300
    s_menu.height = 100

    e_menu = Button.Button(text="EXIT")
    e_menu.x_loc = (3 * X // 4) - 125
    e_menu.y_loc = (4 * Y // 5) - 50
    e_menu.width = 300
    e_menu.height = 100
    menu_layout = Layout.Layout([s_menu, e_menu])

    # random, beginner, amateur, club, expert
    random_button = Button.Button(text="RANDOM")
    random_button.x_loc = (X // 4) - 125
    random_button.y_loc = (3 * Y // 5) - 50
    random_button.width = 150
    random_button.height = 50

    beginner_button = Button.Button(text="BEGINNER")
    beginner_button.x_loc = (3 * X // 4) - 125
    beginner_button.y_loc = (3 * Y // 5) - 50
    beginner_button.width = 150
    beginner_button.height = 50

    amateur_button = Button.Button(text="AMATEUR")
    amateur_button.x_loc = (X // 4) - 125
    amateur_button.y_loc = (4 * Y // 5) - 50
    amateur_button.width = 150
    amateur_button.height = 50

    club_button = Button.Button(text="CLUB")
    club_button.x_loc = (3 * X // 4) - 125
    club_button.y_loc = (4 * Y // 5) - 50
    club_button.width = 150
    club_button.height = 50

    expert_button = Button.Button(text="EXPERT")
    expert_button.x_loc = (X // 4) - 125
    expert_button.y_loc = (4.5 * Y // 5) - 50
    expert_button.width = 150
    expert_button.height = 50

    difficulty_layout = Layout.Layout([random_button, beginner_button, amateur_button, club_button, expert_button])

    e_in_game = Button.Button(text="EXIT")

    e_in_game.x_loc = X // 12
    e_in_game.y_loc = (3 * Y // 4)
    e_in_game.width = 300
    e_in_game.height = 100

    in_game_layout = Layout.Layout([game, e_in_game])

    e_end = Button.Button(text="EXIT")
    e_end.x_loc = (3 * X // 4) - 125
    e_end.y_loc = (4 * Y // 5) - 50
    e_end.width = 300
    e_end.height = 100

    ng_end = Button.Button(text="NEW GAME")
    ng_end.x_loc = (X // 4) - 125
    ng_end.y_loc = (4 * Y // 5) - 50
    ng_end.width = 300
    ng_end.height = 100
    end_layout = Layout.Layout([ng_end, e_end])

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
                    gui.update_active_screen(difficulty_layout)
                elif action == "RANDOM" or action == "BEGINNER" or action == "AMATEUR" or action == "CLUB" or action == "EXPERT":
                    gui.update_active_screen(in_game_layout)
                    current_game = Layout.Layout.get_game(GameGUI.GameGUI.get_active_screen(gui))
                    if action == "RANDOM":
                        current_game.computer_ai.set_difficulty(1)
                    if action == "BEGINNER":
                        current_game.computer_ai.set_difficulty(2)
                    if action == "AMATEUR":
                        current_game.computer_ai.set_difficulty(3)
                    if action == "CLUB":
                        current_game.computer_ai.set_difficulty(4)
                    if action == "EXPERT":
                        current_game.computer_ai.set_difficulty(5)

                    title_location = (20, 20)

                elif action == 'NEW GAME':
                    gui.update_active_screen(in_game_layout)
                    in_game_layout.new_game()
                    title_location = (20, 20)

        # Add title image
        SCREEN.fill(BACKGROUND)
        if GameGUI.GameGUI.get_active_screen(gui) == in_game_layout:
            font = pygame.font.Font('freesansbold.ttf', 65)
            text_surf = font.render("\'s Turn", True, BLACK)
            text_pos = [180, 265]
            SCREEN.blit(text_surf, text_pos)
        SCREEN.blit(TITLE, title_location)
        gui.draw(SCREEN)

        if GameGUI.GameGUI.get_active_screen(gui) == end_layout:
            b_score, w_score = Game.Game.get_winner(current_game)
            if w_score > b_score:
                dif = w_score - b_score
                text = "You lost by: " + str(dif) + " points"
            elif w_score < b_score:
                dif = b_score - w_score
                text = "You won by: " + str(dif) + " points"
            else:
                text = "Tie game"
            font = pygame.font.Font('freesansbold.ttf', 60)
            text_surf = font.render(text, True, Button.Button.TEXT_COLOR)
            text_pos = [(X // 2) - 300, (Y // 2)]
            SCREEN.blit(text_surf, text_pos)

        pygame.display.update()

        if GameGUI.GameGUI.get_active_screen(gui) == in_game_layout:
            current_game = Layout.Layout.get_game(GameGUI.GameGUI.get_active_screen(gui))
            if Game.Game.is_over(current_game):
                gui.update_active_screen(end_layout)
                title_location = ((X // 2) - (452 // 2), 50)
            if Game.Game.has_no_valid_moves(current_game) and not Game.Game.is_over(current_game):
                current_game.skip_move()
                time.sleep(1)
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
