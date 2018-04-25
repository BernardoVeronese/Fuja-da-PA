import pygame
from GameOver import *
from LevelSelection import *

def game(level):

    score = 0
    time_initial = pygame.time.get_ticks()

    #Initialization variables
    player_x0 = 0
    player_y0 = 0
    player_angle = 0

    heli_x0 = 0
    heli_y0 = 0
    heli_angle = 0



    #Class initialization
    player = Player(player_x0, player_y0, player_angle)
    screen.blit(player.image, player.rect)
    '''if level.id == '1':
        bot_1 = Bot(x,y,image,speed)
        bot_2 = Bot(x, y, image, speed)

    if level.id == '2':
        bot_1 = Bot(x,y,image,speed)
        bot_2 = Heli(x,y,angle)

    if level.id == '3':
        bot_1 = Heli(x,y,angle)
        bot_2 = Heli(x,y,angle)'''

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
        player.update_pos(angle_step)

        if game_over.measure_state(PLAYER, ENEMIES):
            #Mensagem de Game Over
            game_over.state = True

        # Atualização de Score e Verificação de Flags das etapas dos Jogos
        if level.verificamissao(Player.x, Player.y):
            score += 1000-5*(level.time_flag/1000-time_initial/1000) #modelo de Score

        if level.vencedor(level):
            # Mensagem de parabéns
            get_score(screen, level.file, score)
            game_over.state = True

        #Screen update
        pygame.display.update()  # update na tela

    nivel()