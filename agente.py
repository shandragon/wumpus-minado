import collections

class Agente:
    def __init__(self, n):
        self.n = n
        self.visitados = set()
        self.seguros = set()  # Células confirmadas sem minas
        self.fronteira = collections.deque([(0, 0)])  # Próximos passos planejados

    def decidir_movimento(self, pos_atual, num_minas, tem_brilho):
        """
        Lógica central: Se o número de minas ao redor é 0,
        todas as vizinhas são seguras para explorar.
        """
        r, c = pos_atual
        self.visitados.add((r, c))

        # Se a célula atual diz que há 0 minas ao redor,
        # todas as 8 vizinhas são seguras!
        if num_minas == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.n and 0 <= nc < self.n:
                        if (nr, nc) not in self.visitados:
                            self.seguros.add((nr, nc))

        # Adiciona vizinhos seguros à fila de exploração (Fronteira)
        for seg in self.seguros:
            if seg not in self.visitados and seg not in self.fronteira:
                self.fronteira.append(seg)

        # Escolhe o próximo passo da fronteira
        if self.fronteira:
            return self.fronteira.popleft()

        # Se não houver caminho seguro conhecido, tenta um movimento aleatório adjacente
        # (Isso acontece quando o agente fica 'preso' por números altos)
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n and (nr, nc) not in self.visitados:
                return (nr, nc)

        return pos_atual  # Fica parado se não houver opção