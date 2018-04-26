import pygame
import math
from GameOver import *
from Player import *
from Heli import *
from Capivara import *
from highscore import *

def game(level, screen):

    score = 0
    time_initial = pygame.time.get_ticks()
    clock = pygame.time.Clock()

    #Level selection
    if level.id == '1':
        image = Background('./assets/Map_1.png', [0, 0])

    elif level.id == '2':
        image = Background('./assets/Map_2.png', [0, 0])

    else:
        image = Background('./assets/Map_3.png', [0, 0])

    #Initialization variables
    player_x0 = 0
    player_y0 = 0
    player_angle = 0

    heli_x0 = 0
    heli_y0 = 0
    heli_angle = 0

    #Terrain parameters
    angle_step = 5*math.pi/180
    terrain_factor = 0.01

    #Class initialization
    object_group = pygame.sprite.Group()
    player = Player(player_x0, player_y0, player_angle)
    heli = Heli(heli_x0, heli_y0, heli_angle)
    capivara = Capivara()
    object_group.add(heli)
    object_group.add(capivara)
    object_group.draw(screen)
    screen.blit(player.image, player.rect)

    #Game Over criteria
    game_over = GameOver()

    while not game_over.state:
        # GET EVENT
        event = pygame.event.get()
        player.handle_event(event)
        player.move(terrain_factor, angle_step)
        #Bot reaction
        '''bot_1.follow(player.x, player.y)
        bot_2.follow(player.x, player.y)'''
        heli.follow(player.x, player.y)
        capivara.state_change()
        player.update_pos(angle_step)
        heli.update_pos()

        #Game over verification
        game_over.measure_state(player, object_group)

        # Atualização de Score e Verificação de Flags das etapas dos Jogos
        if level.verificamissao(player.x, player.y):
            score += 1000-5*(level.time_flag/1000-time_initial/1000) #modelo de Score

        if level.vencedor(level):
            # Mensagem de parabéns
            get_score(screen, level.file, score)
            game_over.state = True

        #Screen update
        pygame.display.update()
        clock.tick(20)  # Time do relógio

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
        for event in pygame.event.get():
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