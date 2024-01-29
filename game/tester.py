import sys
import pygame

# ... (import các modules và lớp cần thiết)

def main():
    pygame.init()

    # Kích thước cửa sổ và một số cài đặt khác
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Game Title")

    # Tạo một hộp (button) cho việc chọn theme
    theme_button_rect = pygame.Rect(50, 50, 150, 50)
    theme_button_color = (100, 100, 100)
    theme_button_text = "Change Theme"
    font = pygame.font.Font(None, 36)

    game = Game()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or is_close_app_event(event):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if theme_button_rect.collidepoint(event.pos):
                    game.change_theme("new_theme")  # Thay đổi thành tên theme mới

        # Vẽ hộp (button) cho việc chọn theme
        pygame.draw.rect(screen, theme_button_color, theme_button_rect)
        text_surface = font.render(theme_button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=theme_button_rect.center)
        screen.blit(text_surface, text_rect)

        # Các bước cập nhật và vẽ game khác ở đây

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
