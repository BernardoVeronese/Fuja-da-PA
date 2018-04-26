import pygame
from Menu import *

def nivel():  # Função que promove o menu de escolha de Fases
    while True:
        for event in pygame.event.get():
            # 1ro evento - Finalização do Jogo4
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Criação dos botões relacionados aos níveis do jogo
        itemsnivel = [
            ('Nível 1', 'fase1', 'button'),
            ('Nível 2', 'fase2', 'button'),
            ('Nível 3', 'fase3', 'button')
        ]

        # Chamada do menu de níveis do jogo
        result = menu(screen, itemsnivel, MARGEMD, MARGEMC, BUTTONHEIGHT, ESPAÇAMENTO, BUTTONWIDTH, Font, Capa)

        # Conferindo resultado dos botões
        if result == 'fase1':
            phase = fase1()
        elif result == 'fase2':
            phase = fase2()
        else:
            phase = fase3()

        # Inicialização da Fase pressionada
        game(phase)

        pygame.display.update()  # Atualização de tela
        clock.tick(20)  # Time do relógio