# Requisitos do Projeto: Labirinto Híbrido (Minas & Tesouros)

Este documento define as regras e o funcionamento do ambiente onde o agente irá operar.

## O Ambiente (Grid)

- Estrutura: Uma matriz $N \times N$ (ex: 8x8). Parametrizável para permitir diferentes tamanhos.
- Células: Cada célula pode estar "Oculta" ou "Revelada".
- Configuração: O tabuleiro é gerado aleatoriamente a cada jogo, com uma distribuição de:
  - Minas: 10% das células.
  - Monstros: 1 das células.
  - Tesouros: 5% das células.
  - O restante são células vazias.
- Conteúdo: Uma célula pode conter:
  - Vazia: Nada acontece.
  - Mina (Perigo): Se o agente entrar, o jogo termina (derrota).
  - Monstro (Perigo): Se o agente entrar, o jogo termina (derrota).
  - Tesouro (Objetivo): O agente deve coletar todos ou chegar ao fim.

## Regras de Percepção (Sensores)

O agente não vê o que está nas células adjacentes, mas recebe "pistas":

- Números (Estilo Campo Minado): Quando o agente está numa célula segura, ele vê um número que indica quantas minas existem nas 8 células vizinhas.
- Brilho (Estilo Wumpus): Se o agente estiver numa célula adjacente (norte, sul, leste, oeste) a um tesouro, ele sente um "Brilho".
- Fedor (Estilo Wumpus): Se o agente estiver numa célula adjacente a um monstro, ele sente um "Fedor".
 
## Ações do Agente

- Movimentar: Norte, Sul, Leste, Oeste.
- Atacar: Norte, Sul, Leste, Oeste. (para tentar eliminar o monstro)
- Coletar: Para pegar um tesouro na célula atual.

## Condições de Vitória/Derrota

- Vitória: Coletar todos os tesouros e chegar à saída.
- Derrota: Pisar em uma mina ou entrar na sala do monstro.

## Panorama Geral da Solução

Para programarmos isto, vamos seguir estes passos:

1. Criação do Tabuleiro: Uma classe em Python para gerir a matriz e colocar as minas/monstro/tesouros aleatoriamente.
2. Lógica de Sensores: Funções que calculam os números de proximidade e o brilho.
3. Interface de Feedback: Uma forma de mostrar o tabuleiro usando PyGame.
4. O Agente: Inicialmente, um controle manual para testares as regras, evoluindo depois para um agente que decide o caminho sozinho.