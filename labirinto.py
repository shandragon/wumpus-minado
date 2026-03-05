import random

class Labirinto:
    def __init__(self, size):
        self.size = size
        # 0: Vazio, 1: Mina, 2: Tesouro
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.revelado = [[False for _ in range(self.size)] for _ in range(self.size)]
        self.agente_pos = [0, 0]
        self.revelado[0][0] = True
        self._gerar_elementos()

    def _gerar_elementos(self):
        # Coloca 5 minas e 3 tesouros aleatoriamente (evitando a posição [0,0])
        for tipo, qtd in [(1, 5), (2, 3)]:
            count = 0
            while count < qtd:
                r, c = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
                if (r, c) != (0, 0) and self.grid[r][c] == 0:
                    self.grid[r][c] = tipo
                    count += 1

    def get_minas_vizinhas(self, r, c):
        """Lógica Campo Minado: Conta minas nas 8 células ao redor."""
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.size and 0 <= nc < self.size and self.grid[nr][nc] == 1:
                    count += 1
        return count

    def tem_brilho(self, r, c):
        """Lógica Wumpus: Deteta tesouro nas 4 direções cardinais."""
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.size and 0 <= nc < self.size and self.grid[nr][nc] == 2:
                return True
        return False

    def mover(self, dr, dc):
        nr, nc = self.agente_pos[0] + dr, self.agente_pos[1] + dc
        if 0 <= nr < self.size and 0 <= nc < self.size:
            self.agente_pos = [nr, nc]
            self.revelado[nr][nc] = True
            return self.grid[nr][nc]
        return None