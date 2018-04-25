import pygame


class GameOver(object):
    def __init__(self):
        self.state = False

    def measure_state(self, player, enemies):
        if player.collided(bot1) or player.collided(bot2):
            self.state = True
