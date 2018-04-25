#Importação de bibliotecas necessárias
from Functions import * #Functions.py
from Levels import * #Levels.py
from Player import * #Player.py
from highscore import * #highscore.py
import pygame #módulo do Pygame
import sys #módulo do Sistema
from pygame.locals import * #Continuação do módulo do Pygame

# Parâmetros da Tela
SCREENWIDTH = 1000 #largura
SCREENHEIGHT = 600 #altura

#Parâmetros de dimensão do Botão
BUTTONWIDTH = 150 #largura
BUTTONHEIGHT = 50 #altura

# Cores RGB
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (155,   0,   0)
GREEN = (0, 155,   0)
BRIGHT_RED = (255,   0,   0)
BRIGHT_GREEN = (0, 255,   0)
GREY = (150, 150, 150)

# Inicialização de pacote Pygame
pygame.init()

# Variaveis Globais
clock = pygame.time.Clock() #inicialização de relógio
screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT]) #inicialização de tela
letra = pygame.font.get_default_font()

#Função que será responsável por lidar com os eventos do jogo
def game(level):

    score = 0 #Ao iniciar o jogo, o Score é zero
    time_initial = pygame.time.get_ticks() #Coleta de tempo inicial de início do jogo

    while True: #Loop
        #Movimento do Player
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

        # Verifica se o Player já é vencedor na Fase
        if level.vencedor(level):
            # Mensagem de parabéns
            get_score(screen, level.file, score) #pega a pontuação
            nivel() #Volta ao menu de fases disponíveis

        pygame.display.update()  # update na tela

#Função que mostra todos os HighScores
def highscore():
    while True: #Lidar com evento de Quit!
        flag = 0 #Flag para verificar se algum botão foi apertado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        ItemsJogar = [
            ('Nível 1', 'fase1', 'button'),
            ('Nível 2', 'fase2', 'button'),
            ('Nível 3', 'fase3', 'button'),
            ('Voltar', 'voltar', 'button')
        ] #um botão para cada fase
        result = menu(screen, ItemsJogar, 30, 200, 30, 30, BUTTONHEIGHT, BUTTONWIDTH, letra) #criação de menu

        # Verificação se o botão foi pressionado
        if result[0] == 'fase1':
            file_name = '/Data/highscore1.txt'
            flag = 1
        elif result[0] == 'fase2':
            file_name = '/Data/highscore2.txt'
            flag = 1
        elif result[0] == 'fase3':
            file_name = '/Data/highscore3.txt'
            flag = 1
        elif result[0] == 'voltar':
            return

        # Se um botão foi selecionado
        if flag:
            show_top10(screen, file_name)

        pygame.display.update()  # update na tela
        clock.tick(20)  # Frames para o Loop

#Função que promove o menu de escolha de Fases
def nivel():
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

        result = menu(screen, ItemsJogar, 30, 200, 30, 30, BUTTONHEIGHT, BUTTONWIDTH, letra)

        if result[0] == 'fase1':
            fase = fase1()
        elif result[0] == 'fase2':
            fase = fase2()
        elif result[0] == 'fase3':
            fase = fase3()
        game(fase)
        pygame.display.update()
        clock.tick(20)

def main(): #Função que promove o menu de início de Jogo
    #Definição de Legenda da Tela
    pygame.display.set_caption("Game - Fuja da PA!")
    #Preenchimento da Tela em branco
    BackGround = Background('./assets/capa.png', [0, 0])
    screen.blit(BackGround.image, BackGround.rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        Items = [('Fuja da PA', 'jogar', 'button'),
                 ('Highscores', 'score', 'button'),
                 ('Quit', 'exit', 'button'),
                 ]

        result = menu(screen, Items, 30, 200, 30, 30, BUTTONHEIGHT, BUTTONWIDTH, letra)

        if result[0] == 'exit':
            quitgame()
        elif result[0] == 'jogar':
            nivel()
        elif result[0] == 'score':
            highscore()

        pygame.display.update()
        clock.tick(20)

if __name__ == '__main__':
    main()