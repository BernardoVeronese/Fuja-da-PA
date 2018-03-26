from pygame.locals import *
import pygame
from Main import *

class fase1:

    #Flags relacionadas às missões
    flag1 = False
    flag2 = False

    # Asset relacionada à missão 1
    M1X =  # 19.9cm
    M1Y =  # 3.5cm

    # Asset relacionada à missão 2
    M2X =  # 3.7cm
    M2Y =  # 11.5cm
    M2WIDTH =  # 1.0cm
    M2HEIGHT =  # 3.6cm

    #Asset relacionada ao Rancho
    RANCHOX = #11.4cm
    RANCHOY = #4.9cm
    RANCHOWIDTH = #3.4cm
    RANCHOHEIGHT =  #3.3cm

    #Asset relacionada ao Novo Fund
    FUNDX =  # 4.8cm
    FUNDY =  # 4.9cm
    FUNDWIDTH =  # 4.4cm
    FUNDHEIGHT =  # 3.7cm

    def obstaculo(self, x, y):
        if RANCHOX < x < RANCHOX+RANCHOWIDTH and RANCHOY < y < RANCHOY+RANCHOHEIGHT:
            return True
        elif FUNDX < x < FUNDX+FUNDWIDTH and FUNDY < y < FUNDY+FUNDHEIGHT:
            return True
        return False

    def verificamissao(self, x, y):
        if M1X < x and y < M1Y:
            flag1 = True
            #Inseir texto de primeira parte cumprida
        if M2X < x < M2X+M2WIDTH and M2Y < y < M2Y+M2HEIGHT:
            if flag1:
                flag2 = True
            # Inseir texto de segunda parte cumprida

    def vencedor(self):
        if flag1 and flag2:
            # Inseir texto de vencedor
            return True
        return False

    def street(self, x, y):



class fase2:


def level1():
    return fase1

def level2():
    return fase2