import pygame
import sys
import time
from pygame.locals import *
from GeographyGraph import GeographyGraph
from Player import Player
from Functions import *
from Levels import *
from Highscore import *
from Menu import *
from Heli import *
from Bot import *

# Este arquivo .py contém:
# def main: função que promove o Menu inicial do Jogo
# def nivel: função que promove o Menu de escolha de fase
# def highscore: função que promove o Menu de visualização de HighScore

# Parâmetros da Tela
SCREENWIDTH = 945 #largura
SCREENHEIGHT = 565 #altura
MARGEMD = 120
MARGEMC = 200
ESPAÇAMENTO = 50

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

#Função que será responsável por lidar com os eventos do jogo
def game(level):#CHANGE TO GAME.PY

    score = 0
    time_initial = pygame.time.get_ticks()
    player = Player(x, y, angle)
    screen.blit (player.image, player.rect)
    if level.id == '1':
        bot_1 = Bot(x, y, image, speed)
        bot_2 = Bot(x, y, image, speed)
        image = Background('./assets/Map_1.png', [0, 0])

    elif level.id == '2':
        bot_1 = Bot(x, y, image, speed)
        bot_2 = Heli(x, y, angle)
        image = Background('./assets/Map_2.png', [0, 0])

    else:
        bot_1 = Heli(x, y, angle)
        bot_2 = Heli(x, y, angle)
        image = Background('./assets/Map_3.png', [0, 0])

    while True:
        level.mapa
        for event in pygame.event.get()
            # 1ro evento - Finalização do Jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # GET EVENT
        event = pygame.event.get()
        player.handle_event(event)
        player.move(terrain_factor, angle_step)
        bot_1.follow(player.x, player.y)
        bot_2.follow(player.x, player.y)

        # Atualização de Score e Verificação de Flags das etapas dos Jogos
        if level.Verificarmissao(player.x, player.y):
            score += 1000 - 5 * (level.time_flag / 1000 - time_initial / 1000)  # modelo de Score

        if level.Vencedor(level):
            # Mensagem de parabéns
            get_score(screen, level.file, score)
            return
        pygame.display.update()  # update na tela


def nivel():  # Função que promove o menu de escolha de Fases
    # Definição da Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    while True:
        for event in pygame.event.get():
            # 1ro evento - Finalização do Jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Criação dos botões relacionados aos níveis do jogo
            itemsnivel = [
                ('Nível 1', 'fase1', 'button'),
                ('Nível 2', 'fase2', 'button'),
                ('Nível 3', 'fase3', 'button'),
                ('Voltar', 'voltar', 'button')
            ]

            # Chamada do menu de níveis do jogo
            result = menu(screen, itemsnivel, MARGEMD, MARGEMC, BUTTONHEIGHT, ESPAÇAMENTO, BUTTONWIDTH, Font, Capa)

            # Conferindo resultado dos botões
            if result == 'fase1':
                image = Background('./assets/Map_3.png', [0, 0])
                phase = fase1(screen, image)
            elif result == 'fase2':
                image = Background('./assets/Map_3.png', [0, 0])
                phase = fase2(screen, image)
            elif result == 'voltar':
                return
            else:
                image = Background('./assets/Map_3.png', [0, 0])
                phase = fase3(screen, image)

            # Inicialização da Fase pressionada
            Game(phase)

            pygame.display.update()  # Atualização de tela
            clock.tick(20)  # Time do relógio


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
            result = menu(screen, itemsnivel, MARGEMD, MARGEMC-50, BUTTONHEIGHT, ESPAÇAMENTO, BUTTONWIDTH, Font, Capa)

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
        result = menu(screen, items, MARGEMD, MARGEMC, BUTTONHEIGHT, ESPAÇAMENTO, BUTTONWIDTH, Font, Capa)

        # Conferindo resultado de botões
        if result == 'exit':  # sair
            quitgame()
        elif result == 'score':  # mostrar tela de Scores
            highscore()

        pygame.display.update()  # Atualizar display
        clock.tick(20)  # Time do Clock


if __name__ == '__main__':
    main()
