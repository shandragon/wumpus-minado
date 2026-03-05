import pygame, sys
from utils import get_font
from button import Button

class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.menu_text = get_font(75).render("Labirinto Inteligente Game", True, (200, 0, 0))
        self.menu_rect = self.menu_text.get_rect(center=(width / 2, 100))

        self.play = Button(pos=(640, 300), text_input="PLAY", font=get_font(50), base_color="blue", hovering_color="aqua")
        self.options = Button(pos=(640, 400), text_input="OPTIONS", font=get_font(50), base_color="blue", hovering_color="aqua")
        self.quit = Button(pos=(640, 500), text_input="QUIT", font=get_font(50), base_color="blue", hovering_color="aqua")

    def draw(self):
        while True:
            self.screen.fill("gray")
            self.screen.blit(self.menu_text, self.menu_rect)

            mouse_pos = pygame.mouse.get_pos()

            for button in [self.play, self.options, self.quit]:
                button.changeColor(mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play.checkForInput(mouse_pos):
                        print("Play button clicked!")
                        return 1
                    if self.options.checkForInput(mouse_pos):
                        print("Options button clicked!")
                        return 2
                    if self.quit.checkForInput(mouse_pos):
                        print("Quit button clicked!")
                        pygame.quit()
                        sys.exit()

            pygame.display.update()