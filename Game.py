import pygame
import math
from GameOver import *
from Player import *
from Heli import *
from Capivara import *
from highscore import *
from Functions import *

# Parâmetros da Tela
SCREENWIDTH = 945 #largura
SCREENHEIGHT = 565 #altura

def tutorial(phase, screen):
    # Definição da Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    bx = 400  # x-size of box
    by = 400  # y-size of box

    # make the presentation box
    box = pygame.surface.Surface((bx, by))
    box.fill(WHITE)
    pygame.draw.rect(box, SKYBLUE, (50, 12, bx - 100, 35), 0)
    pygame.draw.rect(box, SKYBLUE, (50, by - 60, bx - 100, 42), 0)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = Font.render("Fase iniciada", True, BLACK)  # headline
    txt_rect = txt_surf.get_rect(center=(bx // 2, 30))
    box.blit(txt_surf, txt_rect)
    txt_surf = Font.render("ENTER para Fugir da PA", True, BLACK)  # bottom line
    txt_rect = txt_surf.get_rect(center=(bx // 2, 360))
    box.blit(txt_surf, txt_rect)

    txt_surf = []
    if phase == 1:
        txt_surf.append(Font.render("Fase: entregando relatorio", True, BLACK))
        txt_surf.append(Font.render("como um aluno iteano. Voce", True, BLACK))
        txt_surf.append(Font.render("precisa ir ao H8, pegar seu", True, BLACK))
        txt_surf.append(Font.render("relatorio do Osamu, e", True, BLACK))
        txt_surf.append(Font.render("entregar no prédio da COMP!", True, BLACK))
        txt_surf.append(Font.render("Os checkpoints correspondem", True, BLACK))
        txt_surf.append(Font.render("aos pontos em vermelho nos", True, BLACK))
        txt_surf.append(Font.render("mapas. Fique atento ao tempo,", True, BLACK))
        txt_surf.append(Font.render("ele também conta no Score!", True, BLACK))
        txt_surf.append(Font.render("Bom jogo. Fuja da PA!!!", True, BLACK))
    elif phase == 2:
        txt_surf.append(Font.render("Fase: levando o amigo à DS", True, BLACK))
        txt_surf.append(Font.render("Apesar de estar em apuros", True, BLACK))
        txt_surf.append(Font.render("com a PA, voce nao deixará", True, BLACK))
        txt_surf.append(Font.render("seu amigo na mão! Ele está", True, BLACK))
        txt_surf.append(Font.render("no H8 passando mal, e você", True, BLACK))
        txt_surf.append(Font.render("o levará na DS! Atente", True, BLACK))
        txt_surf.append(Font.render("aos pontos em vermelho nos", True, BLACK))
        txt_surf.append(Font.render("mapas. Fique atento ao tempo,", True, BLACK))
        txt_surf.append(Font.render("ele também conta no Score!", True, BLACK))
        txt_surf.append(Font.render("Bom jogo. Fuja da PA!!!", True, BLACK))
    else:
        txt_surf.append(Font.render("Fase: fuja do CTA", True, BLACK))
        txt_surf.append(Font.render("Você terá que sair do CTA", True, BLACK))
        txt_surf.append(Font.render("dessa vez. Mas, antes, voce", True, BLACK))
        txt_surf.append(Font.render("realizará compras no Villa", True, BLACK))
        txt_surf.append(Font.render("e se despedirá de seus", True, BLACK))
        txt_surf.append(Font.render("professores na ELE - COMP", True, BLACK))
        txt_surf.append(Font.render("Agora são três checkpoints", True, BLACK))
        txt_surf.append(Font.render("Fique atento ao tempo,", True, BLACK))
        txt_surf.append(Font.render("ele também conta no Score!", True, BLACK))
        txt_surf.append(Font.render("Bom jogo. Fuja da PA!!!", True, BLACK))

    for i in range(10):
        txt_rect = txt_surf[i].get_rect(center=(bx // 2, 30 * i + 60))
        box.blit(txt_surf[i], txt_rect)

    screen.blit(box, (SCREENWIDTH / 4, SCREENHEIGHT / 10))
    pygame.display.flip()

    while True:  # wait for user to acknowledge and return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
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
    tutorial(level.id, screen)

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
            player.handle_event(event)
        #Handle terrain
        screen.blit(image.image, image.rect)
        terrain_factor = measure_terrain(player, level, screen)

        #Player movement
        player.move(terrain_factor, angle_step)

        #Bot reaction
        '''bot_1.follow(player.x, player.y)
        bot_2.follow(player.x, player.y)'''
        heli.follow(player.x, player.y)
        #capivara.state_change()
        player.update_pos(angle_step)
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

