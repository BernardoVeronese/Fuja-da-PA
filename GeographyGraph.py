import pygame

#Simple player object
class GeographyGraph(object):

    # Initialization
    def __init__(self, x, y, image, speed):
        self.graph = map_graph #dictionary implementation

    # Method to draw object
    def draw(self):
        screen.blit(self.image, (self.x, self.y))  # mudar para load image algo
       