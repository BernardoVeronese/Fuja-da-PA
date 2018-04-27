import pygame

# Parâmetros da Tela
SCREENWIDTH = 945 #largura
SCREENHEIGHT = 565 #altura

#Simple player object
class PassiveSprite(pygame.sprite.Sprite):

    # Initialization
    def __init__(self, x0, y0, filename):
        pygame.sprite.Sprite.__init__(self)
        self.x = x0
        self.y = y0
        self.original_image = pygame.image.load(filename)#change path directory
        #self.image = pygame.transform.scale(self.original_image, (70, 70))

        #Sprite position
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

def constants(level, object_name):
    if level.id =='1':
    elif level.id =='2':
        if object_name =='ELE_COMP':
            x0 = 125/945 * SCREENWIDTH
            y0 = 368/565 * SCREENHEIGHT
            filename = './assets/PassiveSprites/ELE-COMP_2.png'
        if object_name == 'DS':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/DS.png'
        if object_name == 'HTS':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/HTS.png'
        if object_name == 'RANCHO':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/RANCHO.png'
        if object_name == 'NOVOFUND':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/NOVOFUND.png'
        if object_name == 'IGREJA':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/IGREJA.png'
        if object_name == 'HT0':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/HTO.png'
        if object_name == 'H8C':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/H8C.png'
        if object_name == 'H8B':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/H8B.png'
        if object_name == 'H8A':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/H8A_2.png'
        if object_name == 'CPOR':
            x0 =
            y0 =
            filename = './assets/PassiveSprites/CPOR_2.png'

    else:
