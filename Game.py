import pygame
import math
from GameOver import *
from Player import *
from Heli import *
from Capivara import *
from highscore import *
from Functions import *
from Soldier import *
from pygame.locals import *
from Constants import *
from SoundEffects import *

# Parâmetros da Tela
SCREENWIDTH = 945 #largura
SCREENHEIGHT = 565 #altura

# Imagem de Pause
pausa = Background('./assets/pause.png', [0, 0])
gameover = Background('./assets/GAMEOVER.png', [0, 0])

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
    music_selection(level)

    #Level selection
    if level.id == '1':
        image = Background('./assets/Map_1.png', [0, 0])

    elif level.id == '2':
        image = Background('./assets/Map_2.png', [0, 0])

    else:
        image = Background('./assets/Map_3.png', [0, 0])

    screen.blit(image.image, image.rect)
    pygame.mixer.music.play()

    #Initialization variables
    player_x0, player_y0, player_angle = player_constants(level)
    heli_x0, heli_y0, heli_angle, patrol_radius = heli_constants(level)

    #Terrain parameters
    angle_step = 7.5
    terrain_factor = 1

    #Class initialization
    object_group = pygame.sprite.Group()
    player = Player(player_x0, player_y0, player_angle)
    heli = Heli(SCREENWIDTH-1,SCREENHEIGHT-1, heli_angle)
    second_heli = Heli(heli_x0, heli_y0, heli_angle)
    capivara = Capivara()
    soldier = Soldier()
    object_group.add(heli)
    object_group.add(second_heli)
    object_group.add(capivara)
    object_group.draw(screen)
    screen.blit(player.image, player.rect)
    if soldier.state:
        screen.blit(soldier.image, soldier.rect)

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

        # Atualização de Score e Verificação de Flags das etapas dos Jogos
        if level.verificarmissao(player.x, player.y, screen):
            time_flag = pygame.time.get_ticks()
            Font = pygame.font.SysFont("arial", 20, True)
            txt_surf = Font.render("CHECKPOINT ACEITO", True, WHITE)
            screen.blit(txt_surf, (900, 450))
            score += int(1000 - 5 * (time_flag / 1000 - time_initial / 1000))  # modelo de Score

        if level.vencedor():
            get_score(screen, level.file(), score)
            break

        #Player movement
        player.move(terrain_factor, angle_step)

        #Bot reaction
        '''bot_1.follow(player.x, player.y)
        bot_2.follow(player.x, player.y)'''
        capivara.time_counter(level, screen, SCREENHEIGHT)
        soldier.time_counter(level, screen, SCREENHEIGHT)
        player.update_pos(angle_step)
        heli.follow(player.x, player.y)
        second_heli.patrol(heli_x0, heli_y0, patrol_radius)
        heli.update_pos(player.x)
        second_heli.update_pos(player.x)
        screen.blit(image.image, image.rect)
        screen.blit(player.image, player.rect)
        object_group.draw(screen)
        if soldier.state:
            screen.blit(soldier.image, soldier.rect)

        #Game over verification
        object_group.add(soldier)
        game_over.measure_state(player, object_group)
        object_group.remove(soldier)

        #Screen update
        pygame.display.update()
        clock.tick(20)  # Time do relógio

    if game_over.state:
        pygame.mixer.music.stop()
        screen.blit(gameover.image, gameover.rect)
        pygame.display.update()
        game_over_sound()
        while True:  # wait for user to acknowledge and return
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER,
                                                                  pygame.K_BACKSPACE]:
                    return
            pygame.time.wait(20)
    #else:

