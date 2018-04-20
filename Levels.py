from pygame.locals import *
import pygame
from Main import *
from Functions import *

class fase1:

    #Flags relacionadas às missões
    flag1 = False
    flag2 = False
    time_flag = 0

    # Asset relacionada à missão 1
    M1X = 796 # 19.9cm
    M1Y = 140 # 3.5cm

    # Asset relacionada à missão 2
    M2X = 148 # 3.7cm
    M2Y = 460 # 11.5cm
    M2WIDTH = 40 # 1.0cm
    M2HEIGHT = 144 # 3.6cm

    #Asset relacionada ao Rancho
    RANCHOX = 456 #11.4cm
    RANCHOY = 196 #4.9cm
    RANCHOWIDTH = 136 #3.4cm
    RANCHOHEIGHT = 132 #3.3cm

    #Asset relacionada ao Novo Fund
    FUNDX = 192 # 4.8cm
    FUNDY = 196 # 4.9cm
    FUNDWIDTH = 176 # 4.4cm
    FUNDHEIGHT = 148 # 3.7cm

    def __init__(self):
        BackGround = Background('.\Data\Mapa.png', [0, 0])
        screen.blit(BackGround.image, BackGround.rect)
        self.id = '1'

    def file(self):
        return './Data/highscore1.txt'

    def obstaculo(self, x, y):
        if fase1.RANCHOX < x < fase1.RANCHOX+fase1.RANCHOWIDTH and fase1.RANCHOY < y < fase1.RANCHOY+fase1.RANCHOHEIGHT:
            return True
        elif fase1.FUNDX < x < fase1.FUNDX+fase1.FUNDWIDTH and fase1.FUNDY < y < fase1.FUNDY+fase1.FUNDHEIGHT:
            return True
        return False

    def verificamissao(self, x, y):
        if fase1.M1X < x and y < fase1.M1Y:
            fase1.flag1 = True
            fase1.time_flag = pygame.time.get_ticks()
            #Inserir texto de primeira parte cumprida
            return True
        if fase1.M2X < x < fase1.M2X+fase1.M2WIDTH and fase1.M2Y < y < fase1.M2Y+fase1.M2HEIGHT:
            if fase1.flag1:
                fase1.flag2 = True
                time_flag = pygame.time.get_ticks()
            #Inserir texto de segunda parte cumprida

            return True
        return False

    def vencedor(self):
        if fase1.flag1 and fase1.flag2:
            return True
        return False

    def street(self, x, y):
        if y < 180:
            if x < 372 or 512 < x < 592 or 692 < x < 772:
                return False
        elif fase1.RANCHOY < y < fase1.RANCHOY+fase1.RANCHOHEIGHT:
            if fase1.FUNDX < x < fase1.FUNDX+fase1.FUNDWIDTH or fase1.RANCHOX < x < fase1.RANCHOX+fase1.RANCHOWIDTH:
                return False
        elif 440 < y and 188 < x < 632:
            return False
        elif 135 < y and 632 < x < 836:
            return False
        return True

class fase2:

    def file(self):
        return './Data/highscore2.txt'

class fase3:

    def file(self):
        return './Data/highscore3.txt'