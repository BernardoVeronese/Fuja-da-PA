# Libraries
from Main import *

# Método responsável por criar um Menu, dada a entrada dos botões e as configurações espaciais
def menu(Surface, Items, Xoffset, Yoffset, itemheight, totalheight, boxwidth, Font, Image, focus=0):

    # Inicialização de relógio
    Clock = pygame.time.Clock()

    while True:
        Surface.blit(Image.image, Image.rect)  # Blit novamente da imagem de fundo
        Clock.tick(10)  # Pequeno intervalo de tempo antes do início do Loop
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
            Ymod = Yoffset + (focus+1)*totalheight + itemheight - Surface.get_height()
        else:
            Ymod = 0

        for n in range(len(Items)):  # para cada um dos itens
            draw_item = Items[n][0]
            draw_type = Items[n][2]
            if n == focus:  # desenho caso haja foco no respectivo item
                if draw_type == 'button':
                    pygame.draw.rect(Surface, WHITE, (Xoffset, Yoffset + n*totalheight - Ymod, boxwidth, itemheight))
                    drawcolor = BLACK
                elif draw_type == 'cancelbutton':
                    pygame.draw.rect(Surface, (200, 200, 200), (Xoffset, Yoffset + n*totalheight - Ymod, boxwidth,
                                                                itemheight))
                    drawcolor = (0, 0, 0)
            else:  # desenho caso não haja foco no respectivo item
                if draw_type == 'button':
                    pygame.draw.rect(Surface, BLACK, (Xoffset, Yoffset + n*totalheight - Ymod, boxwidth, itemheight), 1)
                    drawcolor = WHITE
                elif draw_type == 'cancelbutton':
                    pygame.draw.rect(Surface, (200, 200, 200), (Xoffset, Yoffset + n*totalheight - Ymod,
                                                                boxwidth, itemheight), 1)
                    drawcolor = (200, 200, 200)
            # Desenho da configuração do Botão
            Surface.blit(Font.render(draw_item, True, drawcolor), (Xoffset + BUTTONWIDTH/2,
                                                                   Yoffset + 3 + n*totalheight - Ymod))
        pygame.display.update()
