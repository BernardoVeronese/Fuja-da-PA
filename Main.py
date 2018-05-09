# Libraries
import pygame
import sys
import time
from pygame.locals import *
from Background import *
from Level import *
from Highscore import *
from LevelSelection import *
from Game import *

# -------------------------------------- #
# VARIABLES

# Screen parameters
SCREENWIDTH = 945
SCREENHEIGHT = 565
MARGEMD = 120
MARGEMC = 200
ESPACAMENTO = 50

# Visual Screen definitions
Capa1 = Background('./Images/Visual Screen/menuinicial_1.png', [0, 0])
Capa2 = Background('./Images/Visual Screen/menuinicial_2.png', [0, 0])
Capa3 = Background('./Images/Visual Screen/menuinicial_3.png', [0, 0])
menuinicial = [Capa1, Capa2, Capa3]  # Initial menu options

Capa12 = Background('./Images/Visual Screen/levelselection_1.png', [0, 0])
Capa22 = Background('./Images/Visual Screen/levelselection_2.png', [0, 0])
Capa32 = Background('./Images/Visual Screen/levelselection_3.png', [0, 0])
levelselection = [Capa12, Capa22, Capa32]  # Level seletion options

# State Screen definitions
tutorial = Background('./Images/State Screen/howtoplay_screen.png', [0, 0])  # How to Play instructions

# RGB Colorsd
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (155,   0,   0)
GREEN = (0, 155,   0)
BRIGHT_RED = (255,   0,   0)
BRIGHT_GREEN = (0, 255,   0)
GREY = (150, 150, 150)

# Others global variables
relogio = pygame.time.Clock()  # clock
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])  # screen

# Initialiazing pygame ...
pygame.init()

# -------------------------------------- #
# METHODS


# howtoplay() displays how to play instructions until BACKSPACE is pressed
def howtoplay():
    screen.blit(tutorial.image, tutorial.rect)
    pygame.display.update()
    while True:
        relogio.tick(10)
        for event in pygame.event.get():
            # 1ro evento - Sair do jogo
            if event.type == QUIT:
                quitgame()
            # 2ndo evento - Teclado o 'ESC'
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                quitgame()
            # 3ro evento - Pressionando tecla BACKSPACE
            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    return
                else:
                    pass
            pygame.display.update()


# highscore() asks the player which highscore's level he wants to check, and show it
def highscore():
    focus = 0  # First screen options
    while True:
        screen.blit(levelselection[focus].image, levelselection[focus].rect)
        relogio.tick(10)
        for event in pygame.event.get():
            # 1ro evento - Sair do jogo
            if event.type == QUIT:
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
                            filename = './Data_highscore/highscore1.txt'
                            show_top10(screen, filename, focus)
                        elif event.pos[1] < 485:
                            filename = './Data_highscore/highscore2.txt'
                            show_top10(screen, filename, focus)
                        else:
                            filename = './Data_highscore/highscore3.txt'
                            show_top10(screen, filename, focus)
            # 4to evento - Movimento do Mouse
            elif event.type == MOUSEMOTION:
                # Se as posições do movimento estiverem dentro do escopo dos itens
                if 287 < event.pos[0] < 631 and 385 < event.pos[1] < 535:
                    if event.pos[1] < 435:
                        focus = 0
                        screen.blit(levelselection[focus].image, levelselection[focus].rect)
                    elif event.pos[1] < 485:
                        focus = 1
                        screen.blit(levelselection[focus].image, levelselection[focus].rect)
                    else:
                        focus = 2
                        screen.blit(levelselection[focus].image, levelselection[focus].rect)
            # 5to evento - Tecla pressionada
            elif event.type == KEYDOWN:
                # Considerando setas do teclado
                if event.key in (K_DOWN, K_RIGHT):
                    focus = (focus + 1) % 3
                    screen.blit(levelselection[focus].image, levelselection[focus].rect)
                elif event.key in (K_UP, K_LEFT):
                    focus = (focus - 1) % 3
                    screen.blit(levelselection[focus].image, levelselection[focus].rect)
                # Considerando teclas de Return, Enter e Espaço
                elif event.key in (K_RETURN, K_SPACE, K_KP_ENTER):
                    if focus == 0:
                        filename = './Data_highscore/highscore1.txt'
                        show_top10(screen, filename, focus)
                    elif focus == 1:
                        filename = './Data_highscore/highscore2.txt'
                        show_top10(screen, filename, focus)
                    elif focus == 2:
                        filename = './Data_highscore/highscore3.txt'
                        show_top10(screen, filename, focus)
                # Considerando BACKSPACE
                elif event.key == K_BACKSPACE:
                    return
                else:
                    pass

            pygame.display.update()


# main() provides the game start, and the player must choose between how to play, play or check high scores
def main():
    pygame.display.set_caption("Game - Fuja da PA!")  # Definição de Legenda da Tela
    focus = 0  # First screen options
    while True:
        screen.blit(menuinicial[focus].image, menuinicial[focus].rect)
        for event in pygame.event.get():
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
                        screen.blit(menuinicial[focus].image, menuinicial[focus].rect)
                    elif event.pos[1] < 485:
                        focus = 1
                        screen.blit(menuinicial[focus].image, menuinicial[focus].rect)
                    else:
                        focus = 2
                        screen.blit(menuinicial[focus].image, menuinicial[focus].rect)
            # 5to evento - Tecla pressionada
            elif event.type == KEYDOWN:
                # Considerando setas do teclado
                if event.key in (K_DOWN, K_RIGHT):
                    focus = (focus + 1) % 3
                    screen.blit(menuinicial[focus].image, menuinicial[focus].rect)
                elif event.key in (K_UP, K_LEFT):
                    focus = (focus - 1) % 3
                    screen.blit(menuinicial[focus].image, menuinicial[focus].rect)
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

        pygame.display.update()
        relogio.tick(20)


if __name__ == '__main__':
    main()
