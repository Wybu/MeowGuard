import pygame
import builtins
import sys

from src.components.game_status import GameStatus
from src.config import Config
from src.game_phases import main_menu_phase, gameplay_phase, exit_game_phase
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
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        #
        #         # Lấy vị trí chuột
        #     elif event.type == pygame.MOUSEMOTION:
        #         mouse_pos = event.pos
        #
        #         # Giới hạn vị trí chuột trong khung hình
        # mouse_pos = (min(max(mouse_pos[0], 0), Config.WIDTH), min(max(mouse_pos[1], 0), Config.HEIGHT))

        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAMEPLAY:
            gameplay_phase()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
            mouse_pos = (min(max(mouse_pos[0], 0), Config.WIDTH), min(max(mouse_pos[1], 0), Config.HEIGHT))
        # efif GlobalState.GAME_STATE == GameStatus.PAUSE:
        #     gameplay_pause()
        # elif GlobalState.GAME_STATE == GameStatus.CHANGETHEME:
        #     changetheme_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAME_END:
            exit_game_phase()

        MusicService.start_background_music()
        update_game_display()


if __name__ == "__main__":
    main()
