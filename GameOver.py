# Libraries
import pygame

# -------------------------------------- #
# CLASSES

class GameOver(object):
    def __init__(self):
        self.state = False

    def measure_state(self, player, group):
        for sprite in group:
            if pygame.sprite.collide_rect(player, sprite):
                self.state = True
