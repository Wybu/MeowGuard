import sys
import time
import pygame

from src.components.game_status import GameStatus
from src.components.hand import Hand
from src.components.hand_side import HandSide
from src.components.player import Player
from src.components.scoreboard import Scoreboard
from src.global_state import GlobalState
from src.services.music_service import MusicService
from src.services.visualization_service import VisualizationService
from src.utils.tools import update_background_using_scroll, update_press_key, is_close_app_event
from src.config import Config
GlobalState.load_main_screen()
VisualizationService.load_main_game_displays()

scoreboard = Scoreboard()
P1 = Player()
H1 = Hand(HandSide.RIGHT)
H2 = Hand(HandSide.LEFT)
# Sprite Groups
hands = pygame.sprite.Group()
hands.add(H1)
hands.add(H2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(H1)
all_sprites.add(H2)
def main_menu_phase():
    scoreboard.reset_current_score()
    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return

        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            GlobalState.GAME_STATE = GameStatus.GAMEPLAY

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)
    GlobalState.PRESS_Y = update_press_key(GlobalState.PRESS_Y)
    VisualizationService.draw_main_menu(GlobalState.SCREEN, scoreboard.get_max_score(), GlobalState.PRESS_Y)
#Game play
def gameplay_phase():
    events = pygame.event.get()
    mouse_pos = (0, 0)
    for event in events:
        if is_close_app_event(event):
            game_over()
            return

    P1.update()
    H1.move(scoreboard, P1.player_position)
    H2.move(scoreboard, P1.player_position)

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)

    P1.draw(GlobalState.SCREEN)
    H1.draw(GlobalState.SCREEN)
    H2.draw(GlobalState.SCREEN)
    scoreboard.draw(GlobalState.SCREEN)

    if pygame.sprite.spritecollide(P1, hands, False, pygame.sprite.collide_mask):
        scoreboard.update_max_score()
        MusicService.play_slap_sound()
        time.sleep(0.3)
        game_over()
# def gameplay_pause():
def exit_game_phase():
    pygame.quit()
    sys.exit()
def pause_menu_phase():
    while True:
        for event in pygame.event.get():
            if is_close_app_event(event):
                game_over()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    GlobalState.GAME_STATE = GameStatus.PAUSE
                    VisualizationService.draw_pause_menu()
                elif event.key == pygame.K_BACKSPACE and GlobalState.GAME_STATE == GameStatus.PAUSE:
                    GlobalState.GAME_STATE = GameStatus.GAMEPLAY
                    return

def game_over():
    P1.reset()
    H1.reset()
    H2.reset()
    GlobalState.GAME_STATE = GameStatus.MAIN_MENU
    time.sleep(0.5)
