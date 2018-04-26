import pygame


class GameOver(object):
    def __init__(self):
        self.state = False

    def measure_state(self, player, group):
        if not pygame.sprite.spritecollideany(player, group) == "None":
            self.state = True
