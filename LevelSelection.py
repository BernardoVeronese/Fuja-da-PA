import pygame
from Menu import *
from Functions import *
from Game import *
from pygame.locals import *
from Levels import *

# Método responsável por criar um Menu, dada a entrada dos botões e as configurações espaciais
def menu(Surface, Items, Xoffset, Yoffset, itemheight, totalheight, boxwidth, Font, Image, focus=0):
    # Cores RGB
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (155, 0, 0)
    GREEN = (0, 155, 0)
    BRIGHT_RED = (255, 0, 0)
    BRIGHT_GREEN = (0, 255, 0)
    GREY = (150, 150, 150)

    # Parâmetros de dimensão do Botão
    BUTTONWIDTH = 180  # largura
    BUTTONHEIGHT = 30  # altura

    # Inicialização de relógio
    relogio = pygame.time.Clock()

    while True:
        Surface.blit(Image.image, Image.rect)  # Blit novamente da imagem de fundo
        relogio.tick(10)  # Pequeno intervalo de tempo antes do início do Loop
        for event in pygame.event.get():  # Lidando com os eventos do Usuário
            # 1ro evento - Sair do jogo
            if event.type == QUIT:  # se evento for terminar
                return 'exit'
            # 2ndo evento - Teclado o 'ESC'
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return 'cancel'
            # 3ro evento - Clicado algum botão do Mouse
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # se o botão é o botão direito
                    # Se a posição do clique está dentro do escopo dos itens
                    if Xoffset < event.pos[0] < Xoffset+boxwidth and Yoffset < event.pos[1] < totalheight*len(Items):
                        clicked_item = int((event.pos[1] - 20)/totalheight)  # Percebendo o item que foi clicado
                        if Items[clicked_item][2] in ('button', 'cancelbutton'):
                            return Items[clicked_item][1]
            # 4to evento - Movimento do Mouse
            elif event.type == MOUSEMOTION:
                # Se as posições do movimento estiverem dentro do escopo dos itens
                if Xoffset < event.pos[0] < Xoffset+boxwidth and Yoffset < event.pos[1] < totalheight*len(Items):
                    focus = int((event.pos[1] - Yoffset)/totalheight)  # Atualizar Focus
            # 5to evento - Tecla pressionada
            elif event.type == KEYDOWN:
                # Considerando setas do teclado
                if event.key in (K_DOWN, K_RIGHT):
                    focus = (focus + 1) % len(Items)
                elif event.key in (K_UP, K_LEFT):
                    focus = (focus - 1) % len(Items)
                # Considerando teclas de Return e Espaço
                elif event.key in (K_RETURN, K_SPACE):
                    if Items[focus][2] in ('button', 'cancelbutton'):
                        return Items[focus][1]
                else:
                    pass

        # Ressalva caso o número de itens (botões) supere a altura da tela
        if Yoffset + focus*totalheight + itemheight > Surface.get_height():
            ymod = Yoffset + (focus+1)*totalheight + itemheight - Surface.get_height()
        else:
            ymod = 0

        for n in range(len(Items)):  # para cada um dos itens
            draw_item = Items[n][0]
            draw_type = Items[n][2]
            if n == focus:  # desenho caso haja foco no respectivo item
                if draw_type == 'button':
                    pygame.draw.rect(Surface, WHITE, (Xoffset, Yoffset + n*totalheight - ymod, boxwidth, itemheight))
                    drawcolor = BLACK
                elif draw_type == 'cancelbutton':
                    pygame.draw.rect(Surface, (200, 200, 200), (Xoffset, Yoffset + n*totalheight - ymod, boxwidth,
                                                                itemheight))
                    drawcolor = (0, 0, 0)
            else:  # desenho caso não haja foco no respectivo item
                if draw_type == 'button':
                    pygame.draw.rect(Surface, BLACK, (Xoffset, Yoffset + n*totalheight - ymod, boxwidth, itemheight), 1)
                    drawcolor = WHITE
                elif draw_type == 'cancelbutton':
                    pygame.draw.rect(Surface, (200, 200, 200), (Xoffset, Yoffset + n*totalheight - ymod,
                                                                boxwidth, itemheight), 1)
                    drawcolor = (200, 200, 200)
            # Desenho da configuração do Botão
            Surface.blit(Font.render(draw_item, True, drawcolor), (Xoffset + BUTTONWIDTH/5,
                                                                   Yoffset + 3 + n*totalheight - ymod))
        pygame.display.update()


def nivel(screen):  # Função que promove o menu de escolha de Fases

    # Parâmetros da Tela
    SCREENWIDTH = 945  # largura
    SCREENHEIGHT = 565  # altura
    MARGEMD = 120
    MARGEMC = 200
    ESPACAMENTO = 50

    # Definição de capa inicial
    Capa = Background('./assets/capa.png', [0, 0])

    # Parâmetros de dimensão do Botão
    BUTTONWIDTH = 180  # largura
    BUTTONHEIGHT = 30  # altura

    # Cores RGB
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (155, 0, 0)
    GREEN = (0, 155, 0)
    BRIGHT_RED = (255, 0, 0)
    BRIGHT_GREEN = (0, 255, 0)
    GREY = (150, 150, 150)

    # Definição da Fonte
    Font = pygame.font.SysFont("arial", 20, True)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            # 1ro evento - Finalização do Jogo4
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
            result = menu(screen, itemsnivel, MARGEMD, MARGEMC, BUTTONHEIGHT, ESPACAMENTO, BUTTONWIDTH, Font, Capa)

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
            game(phase, screen)

            pygame.display.update()  # Atualização de tela
            clock.tick(20)  # Time do relógio