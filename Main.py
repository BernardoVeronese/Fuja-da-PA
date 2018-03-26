import pygame
import sys
import time
from pygame.locals import *
from Bot import Bot
from GeographyGraph import GeographyGraph
from Player import Player
from Functions import *
from Levels import *

# Parâmetros da Tela
SCREENWIDTH = 1000
SCREENHEIGHT = 600

#Parâmetros de dimensão do Botão
BUTTONWIDTH = 100
BUTTONHEIGHT = 50

# Cores RGB
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (155,   0,   0)
GREEN = (0, 155,   0)
BRIGHT_RED = (255,   0,   0)
BRIGHT_GREEN = (0, 255,   0)

# Variaveis Globais
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
highsc1 = 0
highsc2 = 0
highsc3 = 0

# Inicialização de pacotes Pygame
pygame.init()

#Função que será responsável por lidar com os eventos do jogo
def game(level):

    score = 0
    time_initial = pygame.time.get_ticks()

    while True:

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            Player.move(-1, 0)
        if keys[K_UP]:
            Player.move(0, 1)
        if keys[K_RIGHT]:
            Player.move(1, 0)
        if keys[K_DOWN]:
            Player.move(0, -1)

        # Atualização de Score e Verificação de Flags das etapas dos Jogos
        if level.verificamissao(Player.x, Player.y):
            score += 1000-5*(level.time_flag/1000-time_initial/1000) #modelo de Score

        if level.vencedor(level):
            #Mensagem de parabéns
            #Registrar Score
            nivel()

        pygame.display.update()  # update na tela

#Função relacionada a mostrar os HighScores
#def highscore():
    #Printar highsc1
    #Printar highsc2

#Função que promove o menu de escolha de Fases
def nivel():
    Font = pygame.font.SysFont("calibri", 14)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ItemsJogar = [
            ('Nível 1', 'fase1', 'button'),
            ('Nível 2', 'fase2', 'button'),
            ('Nível 3', 'fase3', 'button')
        ]

        result = menu(screen, ItemsJogar, 30, 200, 30, 30, 50, 300, Font)

        if result(0) == 'fase1':
            fase = fase1()
        #elif result(0) == 'fase2':
         #   fase = fase2()
        #elif result(0) == 'fase3':
         #   fase = fase3()

        pygame.display.update()
        clock.tick(20)

        game(fase)

def main(): #Função que promove o menu de início de Jogo

    #Definição de Legenda da Tela
    pygame.display.set_caption("Game - Fuja da PA!")
    #Preenchimento da Tela em branco
    screen.fill(WHITE)

    Font = pygame.font.SysFont("calibri", 14)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Items = [('Fuja da PA', 'jogar', 'button'),
                 ('Highscores', 'score', 'button'),
                 ('Quit', 'exit', 'button'),
                 ]

        result = menu(screen, Items, 30, 200, 30, 30, 50, 300, Font)

        if result[0] == 'exit':
            quitgame()
        elif result[0] == 'jogar':
            nivel()
        elif result[0] == 'score':
            i = 0
            #highscore()

        pygame.display.update()
        clock.tick(20)

if __name__ == '__main__': main()