import pygame

def main():
    #Definições dos objetos
    pygame.init()
    tela = pygame.display.set_mode([300,300])#display do jogo
    pygame.display.set_caption("Fuja da PA!")
    relogio = pygame.time.Clock()
    sup=pygame.Surface((200,200))

    sair = False

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        relogio.tick(27)#passar tempo antes de continuar o loop
        tela.fill((255,255,255))#muda o fundo para cor branca
        tela.blit(sup,[50,50])#adicionar superfície em cima do display
        pygame.display.update()  # update na tela

    pygame.quit()

main()