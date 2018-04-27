import pygame

class fase1:
    # Flags relacionadas às missões
    flag1 = False
    flag2 = False

    # Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    # Cores relacionados à dinâmica de mapa
    RED = (255, 0, 0)
    STREET = (77, 77, 77)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (248, 202, 0)
    YELLOW2 = (248, 201, 0)
    WHITE2 = (246, 239, 220)

    def __init__(self, screen):
        self.id = '1'

    def mapa(self, screen, background):
        screen.blit(background.image, background.rect)

    def file(self):
        return './data_highscore/highscore1.txt'

    def verificarmissao(self, player, sprite1, sprite2):
        if pygame.sprite.collide_rect(player, sprite1):
            if not fase1.flag1:
                fase1.flag1 = True
                return True
        if pygame.sprite.collide_rect(player, sprite2):
            if not fase1.flag2:
                fase1.flag2 = True
                return True
        return False

    def vencedor(self):
        if fase1.flag1 and fase1.flag2:
            return True
        return False

    def Street(self, x, y, screen):
        x = int(x)
        y = int(y)
        if screen.get_at((x, y)) in (fase1.STREET, fase1.WHITE, fase1.WHITE2):
            return True
        return False


class fase2:

    # Flags relacionadas às missões
    flag1 = False
    flag2 = False

    # Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    # Cores relacionados à dinâmica de mapa
    RED = (255, 0, 0)
    STREET = (77, 77, 77)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (248, 202, 0)
    YELLOW2 = (248, 201, 0)
    WHITE2 = (246, 239, 220)

    def __init__(self, screen):
        self.id = '2'

    def mapa(self, screen, background):
        screen.blit(background.image, background.rect)

    def file(self):
        return './data_highscore/highscore2.txt'

    def verificarmissao(self, player, sprite1, sprite2):
        if pygame.sprite.collide_rect(player, sprite1):
            if not fase2.flag1:
                fase2.flag1 = True
                return True
        if pygame.sprite.collide_rect(player, sprite2):
            if not fase2.flag2:
                fase2.flag2 = True
                return True
        return False

    def vencedor(self):
        if fase2.flag1 and fase2.flag2:
            return True
        return False

    def Street(self, x, y, screen):
        x = int(x)
        y = int(y)
        if screen.get_at((x, y)) in (fase2.STREET, fase2.WHITE, fase2.WHITE2):
            return True
        return False


class fase3:
    # Flags relacionadas às missões
    flag1 = False
    flag2 = False

    # Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    # Cores relacionados à dinâmica de mapa
    RED = (255, 0, 0)
    STREET = (77, 77, 77)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (248, 202, 0)
    YELLOW2 = (248, 201, 0)
    WHITE2 = (246, 239, 220)

    def __init__(self, screen):
        self.id = '3'

    def mapa(self, screen, background):
        screen.blit(background.image, background.rect)

    def file(self):
        return './data_highscore/highscore3.txt'

    def verificarmissao(self, player, sprite1, sprite2):
        if pygame.sprite.collide_rect(player, sprite1):
            if not fase3.flag1:
                fase3.flag1 = True
                return True
        if pygame.sprite.collide_rect(player, sprite2):
            if not fase3.flag2:
                fase3.flag2 = True
                return True
        return False

    def vencedor(self):
        if fase3.flag1 and fase3.flag2:
            return True
        return False

    def Street(self, x, y, screen):
        x = int(x)
        y = int(y)
        if screen.get_at((x, y)) in (fase3.STREET, fase3.WHITE, fase3.WHITE2):
            return True
        return False
