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
SCREENWIDTH = 600
SCREENHEIGHT = 1000

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

# Inicialização de pacotes Pygame
pygame.init()

#Função que será responsável por lidar com os eventos do jogo
def game():

    while True:

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            if fase.obstaculo == False:
                Player.move(-1, 0)
        if keys[K_UP]:
            if fase.obstaculo == False:
                Player.move(0, 1)
        if keys[K_RIGHT]:
            if fase.obstaculo == False:
                Player.move(1, 0)
        if keys[K_DOWN]:
            if fase.obstaculo == False:
                Player.move(0, -1)

        pygame.display.update()  # update na tela

#Função que promove o menu de escolha de Fases
def nivel():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        fase = button("Fase 1", 150, 450, BUTTONWIDTH, BUTTONHEIGHT, GREEN, BRIGHT_GREEN, level1)
        fase = button("Fase 2", 350, 450, BUTTONWIDTH, BUTTONHEIGHT, RED, BRIGHT_RED, level2)

        pygame.display.update()
        clock.tick(20)

#Função que promove o menu de início de Jogo
def main():
    pygame.display.set_caption("Game - Fuja da PA!")
    screen.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        largetext = pygame.font.SysFont("calibri", 115)
        textsurf, textrect = ("Fuja da PA!", largetext)
        textrect.center = ((SCREENWIDTH / 2), (3*SCREENHEIGHT / 4))
        screen.blit(textsurf, textrect)

        button("Fuja da PA!", 150, 450, BUTTONWIDTH, BUTTONHEIGHT, GREEN, BRIGHT_GREEN, nivel)
        button("Quit", 350, 450, BUTTONWIDTH, BUTTONHEIGHT, RED, BRIGHT_RED, quitgame)

        pygame.display.update()
        clock.tick(20)
