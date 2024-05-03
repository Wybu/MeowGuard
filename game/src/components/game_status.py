from enum import Enum


class GameStatus(Enum):
    MAIN_MENU = 0
    GAMEPLAY = 1
    GAME_END = 2
    PAUSE=3
    PAUSE_SCREEN = 4