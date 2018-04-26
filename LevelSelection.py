import pygame
from Menu import *
from Functions import *
from Game import *

def nivel(screen):  # Função que promove o menu de escolha de Fases

    # Parâmetros da Tela
    SCREENWIDTH = 945  # largura
    SCREENHEIGHT = 565  # altura
    MARGEMD = 120
    MARGEMC = 200
    ESPACAMENTO = 50

    # Definição de capa inicial
    Capa = Background('./assets/capa.png', [0, 0])

    # Parâmetros de dimensão do Botão
    BUTTONWIDTH = 180  # largura
    BUTTONHEIGHT = 30  # altura

    # Cores RGB
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (155, 0, 0)
    GREEN = (0, 155, 0)
    BRIGHT_RED = (255, 0, 0)
    BRIGHT_GREEN = (0, 255, 0)
    GREY = (150, 150, 150)

    # Definição da Fonte
    Font = pygame.font.SysFont("arial", 20, True)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            # 1ro evento - Finalização do Jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Criação dos botões relacionados aos níveis do jogo
            itemsnivel = [
                ('Nível 1', 'fase1', 'button'),
                ('Nível 2', 'fase2', 'button'),
                ('Nível 3', 'fase3', 'button'),
                ('Voltar', 'voltar', 'button')
            ]

            # Chamada do menu de níveis do jogo
            result = menu(screen, itemsnivel, MARGEMD, MARGEMC, BUTTONHEIGHT, ESPACAMENTO, BUTTONWIDTH, Font, Capa)

            # Conferindo resultado dos botões
            if result == 'fase1':
                image = Background('./assets/Map_3.png', [0, 0])
                phase = fase1(screen, image)
            elif result == 'fase2':
                image = Background('./assets/Map_3.png', [0, 0])
                phase = fase2(screen, image)
            elif result == 'voltar':
                return
            else:
                image = Background('./assets/Map_3.png', [0, 0])
                phase = fase3(screen, image)

            # Inicialização da Fase pressionada
            game(phase)

            pygame.display.update()  # Atualização de tela
            clock.tick(20)  # Time do relógio