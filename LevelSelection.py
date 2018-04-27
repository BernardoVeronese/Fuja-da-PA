# Libraries
import pygame
from Background import *
from Game import *
from pygame.locals import *
from Level import *

# -------------------------------------- #
# VARIABLES

# Visual Screen Definitions
Capa1 = Background('./Images/Visual Screen/levelselection_1.png', [0, 0])
Capa2 = Background('./Images/Visual Screen/levelselection_2.png', [0, 0])
Capa3 = Background('./Images/Visual Screen/levelselection_3.png', [0, 0])
levelselection = [Capa1, Capa2, Capa3]

# Clock
relogio = pygame.time.Clock()

# -------------------------------------- #
# METHODS


# nivel() asks which level the player wants to play and get the game to begin
def nivel(screen):
    focus = 0  # First screen options
    while True:
        screen.blit(levelselection[focus].image, levelselection[focus].rect)
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
                            game(Level(screen, Background('./Images/Maps/map_1.png', [0, 0]),
                                       './Data_highscore/highscore1.txt'), screen)
                        elif event.pos[1] < 485:
                            game(Level(screen, Background('./Images/Maps/map_2.png', [0, 0]),
                                       './Data_highscore/highscore2.txt'), screen)
                        else:
                            game(Level(screen, Background('./Images/Maps/map_3.png', [0, 0]),
                                       './Data_highscore/highscore3.txt'), screen)
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
                    focus = focus + 1
                    screen.blit(levelselection[focus].image, levelselection[focus].rect)
                elif event.key in (K_UP, K_LEFT):
                    focus = focus - 1
                    screen.blit(levelselection[focus].image, levelselection[focus].rect)
                # Considerando teclas de Return e Espaço
                elif event.key in (K_RETURN, K_SPACE, K_KP_ENTER):
                    if focus == 0:
                        game(Level(screen, Background('./Images/Maps/map_1.png', [0, 0]),
                                   './Data_highscore/highscore1.txt'), screen)
                    elif focus == 1:
                        game(Level(screen, Background('./Images/Maps/map_2.png', [0, 0]),
                                   './Data_highscore/highscore2.txt'), screen)
                    elif focus == 2:
                        game(Level(screen, Background('./Images/Maps/map_3.png', [0, 0]),
                                   './Data_highscore/highscore3.txt'), screen)
                elif event.key == K_BACKSPACE:
                    return
                else:
                    pass

        pygame.display.update()
        relogio.tick(20)
