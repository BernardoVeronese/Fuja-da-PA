import pygame
from Menu import *
from Functions import *
from Game import *
from pygame.locals import *
from Levels import *

# Definição de capa inicial
Capa1 = Background('./assets/fase1.png', [0, 0])
Capa2 = Background('./assets/fase2.png', [0, 0])
Capa3 = Background('./assets/fase3.png', [0, 0])
imagem = [Capa1, Capa2, Capa3]

def nivel(screen):  # Função que promove o menu de escolha de Fases

    relogio = pygame.time.Clock()
    focus = 0
    screen.blit(imagem[focus].image, imagem[focus].rect)

    while True:
        screen.blit(imagem[focus].image, imagem[focus].rect)  # Blit novamente da imagem de fundo
        relogio.tick(10)  # Pequeno intervalo de tempo antes do início do Loop
        for event in pygame.event.get():  # Lidando com os eventos do Usuário
            # 1ro evento - Sair do jogo
            if event.type == QUIT:  # se evento for terminar
                quitgame()
            # 2ndo evento - Teclado o 'ESC'
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                quitgame()
            # 3ro evento - Clicado algum botão do Mouse
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # se o botão é o botão direito
                    # Se a posição do clique está dentro do escopo dos itens
                    if 287 < event.pos[0] < 631 and 385 < event.pos[1] < 535:
                        if event.pos[1] < 435:
                            game(fase1(screen), screen)
                        elif event.pos[1] < 485:
                            game(fase2(screen), screen)
                        else:
                            game(fase3(screen), screen)
            # 4to evento - Movimento do Mouse
            elif event.type == MOUSEMOTION:
                # Se as posições do movimento estiverem dentro do escopo dos itens
                if 287 < event.pos[0] < 631 and 385 < event.pos[1] < 535:
                    if event.pos[1] < 435:
                        focus = 0
                        screen.blit(imagem[focus].image, imagem[focus].rect)
                    elif event.pos[1] < 485:
                        focus = 1
                        screen.blit(imagem[focus].image, imagem[focus].rect)
                    else:
                        focus = 2
                        screen.blit(imagem[focus].image, imagem[focus].rect)
            # 5to evento - Tecla pressionada
            elif event.type == KEYDOWN:
                # Considerando setas do teclado
                if event.key in (K_DOWN, K_RIGHT):
                    focus = focus + 1
                    screen.blit(imagem[focus].image, imagem[focus].rect)
                elif event.key in (K_UP, K_LEFT):
                    focus = focus - 1
                    screen.blit(imagem[focus].image, imagem[focus].rect)
                # Considerando teclas de Return e Espaço
                elif event.key in (K_RETURN, K_SPACE, K_KP_ENTER):
                    if focus == 0:
                        game(fase1(screen), screen)
                    elif focus == 1:
                        game(fase2(screen), screen)
                    elif focus == 2:
                        game(fase3(screen), screen)
                elif event.key == K_BACKSPACE:
                    return
                else:
                    pass

        pygame.display.update()  # Atualizar display
        relogio.tick(20)  # Time do Clock