import pygame
import sys
import time
from pygame.locals import *
from Bot import Bot
from GeographyGraph import GeographyGraph
from Player import Player
from Functions import *

# Parâmetros da Tela
SCREENWIDTH = 500
SCREENHEIGHT = 500
BUTTONWIDTH = 100
BUTTONHEIGHT = 50

# Cores
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (155,   0,   0)
GREEN = (0, 155,   0)
BRIGHT_RED = (255,   0,   0)
BRIGHT_GREEN = (0, 255,   0)


def game():

    while True:
        Player.__init__()
        GeographyGraph.__init__()
        Bot.__init__()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            Player.move(-1, 0)
        if keys[K_UP]:
            Player.move(0, 1)
        if keys[K_RIGHT]:
            Player.move(1, 0)
        if keys[K_DOWN]:
            Player.move(0, -1)

        pygame.display.update()  # update na tela

def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])
    pygame.display.set_caption("Game - Fuja da PA!")
    screen.fill(WHITE)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        largetext = pygame.font.SysFont("calibri", 115)
        textsurf, textrect = ("Fuja da PA!", largetext)
        textrect.center = ((SCREENWIDTH / 2), (SCREENHEIGHT / 2))
        screen.blit(textsurf, textrect)

        button("Fuja da PA!", 150, 450, BUTTONWIDTH, BUTTONHEIGHT, GREEN, BRIGHT_GREEN, game)
        button("Quit", 350, 450, BUTTONWIDTH, BUTTONHEIGHT, RED, BRIGHT_RED, quitgame)

        pygame.display.update()
        clock.tick(20)
