# Libraries
from Main import *
from math import *

# Este arquivo .py contém:
# def quitgame: responsável por finalizar programa

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# Método relacionado a finalizar o programa
def quitgame ():
    pygame.quit()
    sys.exit()