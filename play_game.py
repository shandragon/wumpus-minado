import pygame
from labirinto import Labirinto
from agente import Agente
from jogador import Jogador

class PlayGame:
    def __init__(self, screen):
        self.screen = screen
        self.size = 8
        self.fps = 30
        self.tile_size = 60
        self.is_player_mode = True  # Alterna entre IA e Player

    def play(self):
        clock = pygame.time.Clock()

        jogo = Labirinto(self.size)
        fonte = pygame.font.SysFont("Arial", 24)
        running = True

        ia = Agente(self.size)
        jogador = Jogador()

        while running:
            self.screen.fill("gray")

            # Dentro do loop principal, em vez de esperar teclas:
            pygame.time.delay(500)  # Pausa de 0.5s para conseguires ver o movimento

            linha, coluna = jogo.agente_pos
            minas = jogo.get_minas_vizinhas(linha, coluna)
            brilho = jogo.tem_brilho(linha, coluna)

            proxima_pos = (0, 0)
            if self.is_player_mode:
                proxima_pos = jogador.move(jogo.agente_pos)
            else:
                # IA decide para onde ir
                proxima_pos = ia.decidir_movimento(jogo.agente_pos, minas, brilho)

            dr = proxima_pos[0] - linha
            dc = proxima_pos[1] - coluna

            status = jogo.mover(dr, dc)

            if status == 1:  # Pisou em Mina
                print("Atingiu uma mina!")
                running = False
            elif status == 2:  # Achou Tesouro
                print("Encontrou um TESOURO!")

            # Desenhar Grid
            for r in range(self.size):
                for c in range(self.size):
                    rect = pygame.Rect(c * self.tile_size, r * self.tile_size, self.tile_size, self.tile_size)

                    if jogo.revelado[r][c]:
                        pygame.draw.rect(self.screen, "white", rect)
                        # Pista de Minas (Número)
                        minas = jogo.get_minas_vizinhas(r, c)
                        if minas > 0:
                            img = fonte.render(str(minas), True, "black")
                            self.screen.blit(img, (c * self.tile_size + 20, r * self.tile_size + 15))
                        # Pista de Tesouro (Brilho)
                        if jogo.tem_brilho(r, c):
                            pygame.draw.circle(self.screen, "gold", rect.center, 5)

                    pygame.draw.rect(self.screen, "blue", rect, 1)

            # Desenhar Agente
            agente_rect = pygame.Rect(jogo.agente_pos[1] * self.tile_size + 10,
                                      jogo.agente_pos[0] * self.tile_size + 10,
                                      self.tile_size - 20, self.tile_size - 20)
            pygame.draw.ellipse(self.screen, "green", agente_rect)

            pygame.display.flip()
            clock.tick(self.fps)
