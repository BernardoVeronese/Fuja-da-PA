import pygame
import math
from random import *

#Simple player object
class Capivara(pygame.sprite.Sprite):

    # Initialization
    def __init__(self,x0,y0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x0
        self.y = y0
        self.state = False
        self.original_image = pygame.image.load(os.path.join('assets\car.png'))#change path directory
        self.image = self.original_image

        # Capivara position
        self.rect = self.image.get_rect()
        self.rect.center = (x0, y0)


    #Method to draw object
    def draw(self):
        window.blit(self.image,(self.x,self.y))#mudar para load image algo


    def state_change(self):
        if self.state:
            self.killer(screen_size)
        else:
            self.spawner(screen_size)
        time_delay(self)


    def time_delay(self):
        clock = pygame.time.Clock()
        counter = 0
        while not collided(self, sprite) and counter < 30:
            clock.tick(20)
            counter = counter + 1


    def spawner(self, screen_size):#screen_size addition later
        x_pos = randint(0, screen_size)
        y_pos = randint(0, screen_size)
        while not verify_street(x_pos, y_pos):#update later
            x_pos = randint(0, screen_size)
            y_pos = randint(0, screen_size)
        self.x = x_pos
        self.y = y_pos
        update_pos(self)
        self.state = True


    def killer(self, screen_size):#screen_size addition later
        x_pos = randint(0, screen_size)
        y_pos = randint(0, screen_size)
        while verify_street(x_pos,y_pos):  # update later
            x_pos = randint(0, screen_size)
            y_pos = randint(0, screen_size)
        self.x = x_pos
        self.y = y_pos
        update_pos(self)
        self.state = False


    def update_pos(self):
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (self.x, self.y)  # Put the new rect's center at old center.


    def collided(self,sprite):
        return self.rect.colliderect(sprite.rect)
