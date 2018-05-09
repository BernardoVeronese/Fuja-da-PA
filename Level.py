# Libraries
import pygame

# -------------------------------------- #
# VARIABLES

# RGB Colors
RED = (255, 0, 0)
STREET = (77, 77, 77)
WHITE = (255, 255, 255)
WHITE2 = (246, 239, 220)
BLACK = (0, 0, 0)

# -------------------------------------- #
# CLASSES


class Level:
    # -------------------------------------- #
    # LOCAL VARIABLES
    flag1 = False  # first checkpoint boolean
    flag2 = False  # second checkpoint boolean

    # -------------------------------------- #
    # METHODS AND FUNCTIONS
    def __init__(self, levelmap, file, focus):
        self.id = focus
        self.map = levelmap
        self.filet = file

    def mapa(self, screen):
        screen.blit(self.map.image, self.map.rect)

    def file(self):
        return self.filet

    def verificarmissao(self, player, sprite1, sprite2):
        if pygame.sprite.collide_rect(player, sprite1):
            if not self.flag1:
                self.flag1 = True
                return True
        if pygame.sprite.collide_rect(player, sprite2):
            if not self.flag2:
                self.flag2 = True
                return True
        return False

    def vencedor(self):
        if self.flag1 and self.flag2:
            return True
        return False

    def street(self, x, y, screen):
        x = int(x)
        y = int(y)
        if screen.get_at((x, y)) in (STREET, WHITE, WHITE2):
            return True
        return False
