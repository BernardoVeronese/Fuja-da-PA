# Libraries
import pygame

# -------------------------------------- #
# CLASSES


class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, x0, y0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x0
        self.y = y0
        self.origimage = pygame.image.load('./Images/Icons/checkpoint.png')
        self.image = pygame.transform.scale(self.origimage, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (x0, y0)
