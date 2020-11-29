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


def gui_game():
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
    random_button.x_loc = (X // 4) - 100
    random_button.y_loc = (3 * Y // 5) - 50
    random_button.width = 300
    random_button.height = 65

    beginner_button = Button.Button(text="BEGINNER", color=(63, 255, 0))
    beginner_button.x_loc = (3 * X // 4) - 175
    beginner_button.y_loc = (3 * Y // 5) - 50
    beginner_button.width = 300
    beginner_button.height = 65

    amateur_button = Button.Button(text="AMATEUR", color=(255, 255, 0))
    amateur_button.x_loc = (X // 4) - 100
    amateur_button.y_loc = (4 * Y // 5) - 65
    amateur_button.width = 300
    amateur_button.height = 65

    hard_button = Button.Button(text="HARD", color=(246, 129, 129))
    hard_button.x_loc = (3 * X // 4) - 175
    hard_button.y_loc = (4 * Y // 5) - 65
    hard_button.width = 300
    hard_button.height = 65

    expert_button = Button.Button(text="EXPERT", color=(242, 42, 42))
    expert_button.x_loc = (X // 2) - 150
    expert_button.y_loc = (4.5 * Y // 5) - 35
    expert_button.width = 300
    expert_button.height = 65
    difficulty_layout = Layout.Layout([random_button, beginner_button, amateur_button, hard_button, expert_button])

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
                elif action == "RANDOM" or action == "BEGINNER" or action == "AMATEUR" or action == "HARD" or action == "EXPERT":
                    gui.update_active_screen(in_game_layout)
                    current_game = Layout.Layout.get_game(GameGUI.GameGUI.get_active_screen(gui))
                    if action == "RANDOM":
                        current_game.computer_ai.set_difficulty(1)
                    elif action == "BEGINNER":
                        current_game.computer_ai.set_difficulty(2)
                    elif action == "AMATEUR":
                        current_game.computer_ai.set_difficulty(3)
                    elif action == "HARD":
                        current_game.computer_ai.set_difficulty(4)
                    elif action == "EXPERT":
                        current_game.computer_ai.set_difficulty(5)
                    in_game_layout.new_game()
                    title_location = (20, 20)
                elif action == 'NEW GAME':
                    gui.update_active_screen(difficulty_layout)

        SCREEN.fill(BACKGROUND)

        if GameGUI.GameGUI.get_active_screen(gui) == difficulty_layout:
            font = pygame.font.Font('freesansbold.ttf', 60)
            text_surf = font.render("Difficulty:", True, BLACK)
            text_pos = [380, 200]
            SCREEN.blit(text_surf, text_pos)
        elif GameGUI.GameGUI.get_active_screen(gui) == in_game_layout:
            font = pygame.font.Font('freesansbold.ttf', 65)
            text_surf = font.render("\'s Turn", True, BLACK)
            text_pos = [180, 265]
            SCREEN.blit(text_surf, text_pos)
        elif GameGUI.GameGUI.get_active_screen(gui) == end_layout:
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

        SCREEN.blit(TITLE, title_location)
        gui.draw(SCREEN)
        pygame.display.update()

        if GameGUI.GameGUI.get_active_screen(gui) == in_game_layout:
            current_game: Game.Game = Layout.Layout.get_game(GameGUI.GameGUI.get_active_screen(gui))

            if Game.Game.is_over(current_game):
                gui.update_active_screen(end_layout)
                title_location = ((X // 2) - (452 // 2), 50)
            if Game.Game.has_no_valid_moves(current_game) and not Game.Game.is_over(current_game):
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                time.sleep(1)
                pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
                current_game.skip_move()
            if current_game.computer_move():
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                time.sleep(1)
                pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
                gui.draw(SCREEN)
        pygame.display.update()

        clock.tick(15)


def quit_game():
    pygame.quit()
    quit()


gui_game()
quit_game()
