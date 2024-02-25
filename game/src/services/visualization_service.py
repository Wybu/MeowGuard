import pygame

from paths import ASSETS_DIR, MENU_DIR
from src.config import Config
from src.utils.tools import sine


class VisualizationService:
    @staticmethod
    def get_right_hand_image():
        return pygame.image.load(ASSETS_DIR / "right_hand.png").convert_alpha()

    @staticmethod
    def get_left_hand_image():
        return pygame.image.load(ASSETS_DIR / "left_hand.png").convert_alpha()

    @staticmethod
    def get_player_image():
        return pygame.image.load(ASSETS_DIR / "char2.png").convert_alpha()

    @staticmethod
    def get_title2_img():
        return pygame.image.load(MENU_DIR / "title2.png").convert_alpha()

    @staticmethod
    def get_dotted_line():
        return pygame.image.load(ASSETS_DIR / "dotted_line.png").convert_alpha()

    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSETS_DIR / "bg.png").convert_alpha()

    @staticmethod
    def get_background_image2():
        return pygame.image.load(ASSETS_DIR / "bg2.png").convert_alpha()
    @staticmethod
    def get_santa_hand():
        return pygame.image.load(ASSETS_DIR / "santa_hand.png").convert_alpha()

    @staticmethod
    def get_score_backing():
        return pygame.image.load(ASSETS_DIR / "scoreboard.png").convert_alpha()

    @staticmethod
    def get_leftbg():
        return pygame.image.load(ASSETS_DIR/"bg_left1.png").convert_alpha()

    @staticmethod
    def get_rightbg():
        return pygame.image.load(ASSETS_DIR / "bg_right1.png").convert_alpha()
    @staticmethod
    def get_press_key_image():
        return pygame.image.load(MENU_DIR / "press_any_key1.png").convert_alpha()

    @staticmethod
    def get_title_image():
        return pygame.image.load(MENU_DIR / "title5.png").convert_alpha()

    @staticmethod
    def get_holding_gift_image():
        return pygame.image.load(MENU_DIR / "holding_gift1.png").convert_alpha()

    @staticmethod
    def get_main_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 40)

    @staticmethod
    def get_credit_font_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 12)

  #  @staticmethod
  #  def get_score_font():
#     return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 26)

    @staticmethod
    def load_main_game_displays():
        pygame.display.set_caption("Meow Guard")
        gift = VisualizationService.get_player_image()
        pygame.display.set_icon(gift)

    @staticmethod
    def draw_background_with_scroll(screen, scroll):
        background = VisualizationService.get_background_image()
        screen.blit(background, (0, scroll))

    @staticmethod
    def draw_author_credits(screen):
        credit_font = VisualizationService.get_credit_font_font()
        author_credits = credit_font.render("Nhóm 12 LT Python", True, (0, 0, 0))
        credits_rect = author_credits.get_rect(center=(Config.WIDTH // 2, 700))
        screen.blit(author_credits, credits_rect)

    def draw_best_score(screen, max_score, font_size=20):  # Set a reasonable default font size
        score_font = VisualizationService.get_score_font(font_size)
        best_score = score_font.render(f"Best score: {max_score}", True, (0, 0, 0))
        best_score_rect = best_score.get_rect(center=(Config.WIDTH // 2, 13))
        screen.blit(best_score, best_score_rect)

    @staticmethod
    def get_score_font(font_size):  # Remove the default value for font_size
        # Your code to create and return the font object
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf",  font_size)  # Adjust None to your preferred font or font file

    # Adjust None to your preferred font or font file
    @staticmethod
    def draw_title(screen):
        y = sine(200.0, 1280, 10.0, 100)
        title = VisualizationService.get_title_image()
        screen.blit(title, (-40, y))
        holding_gift = VisualizationService.get_holding_gift_image()
        screen.blit(holding_gift, (-5, 350))

    @staticmethod
    def draw_press_key(screen, press_y):
        press_key = VisualizationService.get_press_key_image()
        screen.blit(press_key, (0, press_y))

    @staticmethod
    def draw_cat_hand(screen, press_y):
        # Lấy hình ảnh của leftbg và rightbg
        left_bg = VisualizationService.get_leftbg()
        right_bg = VisualizationService.get_rightbg()

        # Tính toán tọa độ x cho leftbg và rightbg
        left_bg_x = -300  # Vẽ leftbg ở góc trái của màn hình
        right_bg_x = 50  # Vẽ rightbg ở góc phải của màn hình

        # Vẽ leftbg và rightbg
        screen.blit(left_bg, (left_bg_x, press_y))
        screen.blit(right_bg, (right_bg_x, press_y))

    @staticmethod
    def draw_cat_hand2(screen, press_y):
        # Lấy hình ảnh của leftbg và rightbg
        left_bg = VisualizationService.get_leftbg()
        right_bg = VisualizationService.get_rightbg()

        # Tính toán tọa độ x cho leftbg và rightbg
        left_bg_x = -300
        right_bg_x = 40

        # Vẽ leftbg và rightbg
        screen.blit(left_bg, (left_bg_x, press_y))
        screen.blit(right_bg, (right_bg_x, press_y))

    @staticmethod
    def draw_main_menu(screen, max_score, press_y):
        VisualizationService.draw_author_credits(screen)
        VisualizationService.draw_cat_hand(screen, press_y)
        VisualizationService.draw_cat_hand2(screen, 10)
        VisualizationService.draw_best_score(screen, max_score)
        VisualizationService.draw_title(screen)
        VisualizationService.draw_press_key(screen, press_y)

