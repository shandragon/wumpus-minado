import pygame

class Jogador:
    def move(self, pos_atual):
        linha, coluna = pos_atual
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:    return (linha - 1, coluna)
                if event.key == pygame.K_DOWN:  return (linha + 1, coluna)
                if event.key == pygame.K_LEFT:  return (linha, coluna - 1)
                if event.key == pygame.K_RIGHT: return (linha, coluna + 1)
        return pos_atual  # Fica parado se não houver opção