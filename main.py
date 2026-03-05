import pygame
from menu import Menu
from play_game import PlayGame

# Configurações Constantes
WIDTH = 1280
HEIGHT = 720

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Labirinto Inteligente: Minas & Tesouros")

    menu = Menu(screen, WIDTH, HEIGHT)
    play = PlayGame(screen)

    while True:
        escolha = menu.draw()
        print(escolha)
        if escolha == 1: play.play()

if __name__ == "__main__":
    main()