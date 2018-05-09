# Libraries
import pygame
import math
from random import *

# -------------------------------------- #
# VARIABLES

# Constants
COUNTER_THRESHOLD = 150
GRASS = (62, 192, 96)

# -------------------------------------- #
# METHODS


def grass(x, y, screen):
    x = int(x)
    y = int(y)
    if screen.get_at((x, y)) == GRASS:
        return True
    return False

# -------------------------------------- #
# CLASSES


class Capivara(pygame.sprite.Sprite):

    # Initialization
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = -50
        self.y = -50
        self.state = False
        self.original_image = pygame.image.load('./Images/Icons/capivara.png')  # change path directory
        self.image = pygame.transform.scale(self.original_image, (70, 70))
        self.change_state = False
        self.counter = 0

        # Capivara position
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def state_change(self, level, screen, screen_size):
        if self.state:
            self.killer(level, screen, screen_size)
        else:
            self.spawner(level, screen, screen_size)

    def collided(self,sprite):
        return self.rect.colliderect(sprite.rect)

    def time_counter(self, level, screen, screen_size):
        self.counter += 1
        if self.counter >= COUNTER_THRESHOLD:
            self.state_change(level, screen, screen_size)
            self.counter = 0
        # ADD IF(COLLIDED) > SELF.KILLER()

    def update_pos(self):
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (self.x, self.y)  # Put the new rect's center at old center.

    def spawner(self, level, screen, screen_size):  # screen_size addition later
        x_pos = randint(0, screen_size)  # Change
        y_pos = randint(0, screen_size)
        while not level.street(x_pos, y_pos, screen):
            x_pos = randint(0, screen_size)
            y_pos = randint(0, screen_size)
        self.x = x_pos
        self.y = y_pos
        self.update_pos()
        self.state = True

    def killer(self, level, screen, screen_size):  # screen_size addition later
        x_pos = randint(0, screen_size)  # Change
        y_pos = randint(0, screen_size)
        while not grass(x_pos, y_pos, screen):
            x_pos = randint(0, screen_size)
            y_pos = randint(0, screen_size)
        self.x = x_pos
        self.y = y_pos
        self.update_pos()
        self.state = False
