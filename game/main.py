import pygame
import builtins
import sys

from src.components.game_status import GameStatus
from src.config import Config
from src.game_phases import main_menu_phase, gameplay_phase, exit_game_phase, pause_menu_phase
from src.global_state import GlobalState
from src.services.music_service import MusicService

pygame.init()

FramePerSec = pygame.time.Clock()


def update_game_display():
    pygame.display.update()
    FramePerSec.tick(Config.FPS)


def main():
    mouse_pos=(0,0)
    while True:

        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAMEPLAY:
            gameplay_phase()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        GlobalState.GAME_STATE = GameStatus.PAUSE_MENU
                        pause_menu_phase()  # Gọi hàm để hiển thị menu tạm dừng
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
            mouse_pos = (min(max(mouse_pos[0], 0), Config.WIDTH), min(max(mouse_pos[1], 0), Config.HEIGHT))
        elif GlobalState.GAME_STATE == GameStatus.PAUSE_MENU:
            pause_menu_phase()  # Gọi hàm để hiển thị menu tạm dừng
        elif GlobalState.GAME_STATE == GameStatus.GAME_END:
            exit_game_phase()



        MusicService.start_background_music()
        update_game_display()


if __name__ == "__main__":
    main()
