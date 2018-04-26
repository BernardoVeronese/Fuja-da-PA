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
Capa = Background('./assets/capa.png', [0, 0])

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
clock = pygame.time.Clock() #relógio
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT]) #tela

# Inicialização de pacotes Pygame
pygame.init()


def highscore():  # Função que promove o menu para visualização de HighScores
    # Definição da Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    while True:
        for event in pygame.event.get():
            # 1ro evento - Finalização do programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Criação dos botões relacionado ao Menu
            itemsnivel = [
                ('Nível 1', 'fase1', 'button'),
                ('Nível 2', 'fase2', 'button'),
                ('Nível 3', 'fase3', 'button'),
                ('Voltar', 'voltar', 'button')
            ]

            # Chamada do Menu
            result = menu(screen, itemsnivel, MARGEMD, MARGEMC-50, BUTTONHEIGHT, ESPACAMENTO, BUTTONWIDTH, Font, Capa)

            # Conferindo o resultado do clique de botões, selecionando arquivo da Fase
            if result == 'fase1':
                filename = './data_highscore/highscore1.txt'
            elif result == 'fase2':
                filename = './data_highscore/highscore2.txt'
            elif result == 'voltar':
                return
            else:
                filename = './data_highscore/highscore3.txt'

            # Mostrar Top10 Scores relacionados àquela fase
            show_top10(screen, filename)

            pygame.display.update()  # Atualização do Display
            clock.tick(20)  # Time do relógio


def main():  # Função que promove o menu de início de Jogo
    # Definição da Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    # Definição de Legenda da Tela
    pygame.display.set_caption("Game - Fuja da PA!")

    # Preenchimento da Tela em branco
    screen.blit(Capa.image, Capa.rect)

    while True:  # Loop relacionado ao menu inicial do Jogo
        for event in pygame.event.get():  # Enquanto o programa não é finalizado
            if event.type == pygame.QUIT:
                quitgame()

        # Botões relacionados ao menu do jogo
        items = [('FUJA DA PA', 'jogar', 'button'),
                 ('HIGH SCORE', 'score', 'button'),
                 ('QUIT', 'exit', 'button'),
                 ]

        # Chamada do menu de início do jogo
        result = menu(screen, items, MARGEMD, MARGEMC, BUTTONHEIGHT, ESPACAMENTO, BUTTONWIDTH, Font, Capa)

        # Conferindo resultado de botões
        if result == 'exit':  # sair
            quitgame()
        elif result == 'score':  # mostrar tela de Scores
            highscore()
        else:
            nivel(screen)

        pygame.display.update()  # Atualizar display
        clock.tick(20)  # Time do Clock


if __name__ == '__main__':
    main()
