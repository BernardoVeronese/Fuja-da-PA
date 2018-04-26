import pygame
import sys
import time
from pygame.locals import *
from Functions import *
from Levels import *
from highscore import *
from Menu import *
from LevelSelection import *
from Game import *

# Este arquivo .py contém:
# def main: função que promove o Menu inicial do Jogo
# def nivel: função que promove o Menu de escolha de fase
# def highscore: função que promove o Menu de visualização de HighScore

# Parâmetros da Tela
SCREENWIDTH = 945 #largura
SCREENHEIGHT = 565 #altura
MARGEMD = 120
MARGEMC = 200
ESPACAMENTO = 50

# Definição de capa inicial
Capa1 = Background('./assets/menu1.png', [0, 0])
Capa2 = Background('./assets/menu2.png', [0, 0])
Capa3 = Background('./assets/menu3.png', [0, 0])
imagem = [Capa1, Capa2, Capa3]
Capa12 = Background('./assets/fase1.png', [0, 0])
Capa22 = Background('./assets/fase2.png', [0, 0])
Capa32 = Background('./assets/fase3.png', [0, 0])
imagem2 = [Capa12, Capa22, Capa32]
tuto = Background('./assets/comojogar.png', [0,0])

#Parâmetros de dimensão do Botão
BUTTONWIDTH = 180 #largura
BUTTONHEIGHT = 30 #altura

# Cores RGB
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (155,   0,   0)
GREEN = (0, 155,   0)
BRIGHT_RED = (255,   0,   0)
BRIGHT_GREEN = (0, 255,   0)
GREY = (150, 150, 150)

# Variaveis Globais
relogio = pygame.time.Clock() #relógio
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT]) #tela

# Inicialização de pacotes Pygame
pygame.init()

def howtoplay():
    screen.blit(tuto.image, tuto.rect)
    while True:
        pygame.display.update()
        relogio.tick(10)  # Pequeno intervalo de tempo antes do início do Loop
        for event in pygame.event.get():  # Lidando com os eventos do Usuário
            # 1ro evento - Sair do jogo
            if event.type == QUIT:  # se evento for terminar
                quitgame()
            # 2ndo evento - Teclado o 'ESC'
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                quitgame()
            # 3ro evento - Pressionando tecla
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    return
                else:
                    pass
            pygame.display.update()


def highscore():  # Função que promove o menu para visualização de HighScores
    relogio = pygame.time.Clock()
    focus = 0
    screen.blit(imagem2[focus].image, imagem2[focus].rect)

    while True:
        screen.blit(imagem2[focus].image, imagem2[focus].rect)  # Blit novamente da imagem de fundo
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
                            filename = './data_highscore/highscore1.txt'
                            show_top10(screen, filename, focus)
                        elif event.pos[1] < 485:
                            filename = './data_highscore/highscore2.txt'
                            show_top10(screen, filename, focus)
                        else:
                            filename = './data_highscore/highscore3.txt'
                            show_top10(screen, filename, focus)
            # 4to evento - Movimento do Mouse
            elif event.type == MOUSEMOTION:
                # Se as posições do movimento estiverem dentro do escopo dos itens
                if 287 < event.pos[0] < 631 and 385 < event.pos[1] < 535:
                    if event.pos[1] < 435:
                        focus = 0
                        screen.blit(imagem2[focus].image, imagem2[focus].rect)
                    elif event.pos[1] < 485:
                        focus = 1
                        screen.blit(imagem2[focus].image, imagem2[focus].rect)
                    else:
                        focus = 2
                        screen.blit(imagem2[focus].image, imagem2[focus].rect)
            # 5to evento - Tecla pressionada
            elif event.type == KEYDOWN:
                # Considerando setas do teclado
                if event.key in (K_DOWN, K_RIGHT):
                    focus = (focus + 1) % 3
                    screen.blit(imagem2[focus].image, imagem2[focus].rect)
                elif event.key in (K_UP, K_LEFT):
                    focus = (focus - 1) % 3
                    screen.blit(imagem2[focus].image, imagem2[focus].rect)
                # Considerando teclas de Return e Espaço
                elif event.key in (K_RETURN, K_SPACE, K_KP_ENTER):
                    if focus == 0:
                        filename = './data_highscore/highscore1.txt'
                        show_top10(screen, filename, focus)
                    elif focus == 1:
                        filename = './data_highscore/highscore2.txt'
                        show_top10(screen, filename, focus)
                    elif focus == 2:
                        filename = './data_highscore/highscore3.txt'
                        show_top10(screen, filename, focus)
                elif event.key == K_BACKSPACE:
                    return
                else:
                    pass

            pygame.display.update()  # Atualização do Display


def main():  # Função que promove o menu de início de Jogo
    # Definição de Legenda da Tela
    pygame.display.set_caption("Game - Fuja da PA!")

    # Chamada do menu de início do jogo
    focus = 0
    screen.blit(imagem[focus].image, imagem[focus].rect)

    while True:  # Loop relacionado ao menu inicial do Jogo

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
                            nivel(screen)
                        elif event.pos[1] < 485:
                            howtoplay()
                        else:
                            highscore()
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
                    focus = (focus + 1) % 3
                    screen.blit(imagem[focus].image, imagem[focus].rect)
                elif event.key in (K_UP, K_LEFT):
                    focus = (focus - 1) % 3
                    screen.blit(imagem[focus].image, imagem[focus].rect)
                # Considerando teclas de Return e Espaço
                elif event.key in (K_RETURN, K_SPACE, K_KP_ENTER):
                    if focus == 0:
                        nivel(screen)
                    elif focus == 1:
                        howtoplay()
                    elif focus == 2:
                        highscore()
                    else:
                        pass

        pygame.display.update()  # Atualizar display
        relogio.tick(20)  # Time do Clock


if __name__ == '__main__':
    main()
