import pygame
import math
from GameOver import *
from Player import *
from Heli import *
from Capivara import *
from highscore import *
from Functions import *
from pygame.locals import *

# Parâmetros da Tela
SCREENWIDTH = 945 #largura
SCREENHEIGHT = 565 #altura

# Imagem de Pause
pausa = Background('./assets/pause.png', [0, 0])

def pause(screen):
    screen.blit(pausa.image, pausa.rect)
    pygame.display.update()

    while True:  # wait for user to acknowledge and return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_BACKSPACE]:
                return
        pygame.time.wait(20)

def measure_terrain(player, level, screen):
    aux_terrain = 1
    upper_front_x, upper_front_y = player.x, player.y
    if not level.Street(upper_front_x, upper_front_y, screen):
        aux_terrain = 0.4
    return aux_terrain

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

    screen.blit(image.image, image.rect)

    #Initialization variables
    player_x0 = 0.1*SCREENWIDTH
    player_y0 = 0.28*SCREENHEIGHT
    player_angle = 0

    heli_x0 = 0
    heli_y0 = 0
    heli_angle = 0

    #Terrain parameters
    angle_step = 7.5
    terrain_factor = 1

    #Class initialization
    object_group = pygame.sprite.Group()
    player = Player(player_x0, player_y0, player_angle)
    heli = Heli(heli_x0, heli_y0, heli_angle)
    #capivara = Capivara()
    object_group.add(heli)
    #object_group.add(capivara)
    object_group.draw(screen)
    screen.blit(player.image, player.rect)

    #Game Over criteria
    game_over = GameOver()

    while not game_over.state:
        # GET EVENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_p:
                pause(screen)
            player.handle_event(event)
        #Handle terrain
        screen.blit(image.image, image.rect)
        terrain_factor = measure_terrain(player, level, screen)

        #Player movement
        player.move(terrain_factor, angle_step)

        #Bot reaction
        '''bot_1.follow(player.x, player.y)
        bot_2.follow(player.x, player.y)'''
        #capivara.state_change()
        player.update_pos(angle_step)
        heli.follow(player.x, player.y)
        heli.update_pos()
        screen.blit(image.image, image.rect)
        screen.blit(player.image, player.rect)
        object_group.draw(screen)

        #Game over verification
        #game_over.measure_state(player, object_group)

        # Atualização de Score e Verificação de Flags das etapas dos Jogos
        if level.verificarmissao(player.x, player.y, screen):
            score += 1000-5*(level.time_flag/1000-time_initial/1000) #modelo de Score

        if level.vencedor():
            get_score(screen, level.file, score)
            game_over.state = True

        #Screen update
        pygame.display.update()
        clock.tick(20)  # Time do relógio

