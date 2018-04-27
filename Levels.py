import pygame

class fase1:

    #Flags relacionadas às missões
    flag1 = False
    flag2 = False
    time_flag1 = 0
    time_flag2 = 0

    # Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    # Dimensões do Lago
    LAGOX = 397
    LAGOY = 414
    LAGOWIDTH = 325
    LAGOHEIGHT = 113

    # Cores relacionados à dinâmica de mapa
    OBSTACULO = (237, 237, 237)
    OBSTACULO2 = (216, 0, 39)
    OBSTACULO3 = (0, 0, 0)
    OBSTACULO4 = (37, 102, 3)
    RED = (255, 0, 0)
    STREET = (68, 57, 55)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (248, 202, 0)
    WHITE2 = (246, 239, 220)
    GRASS = (62, 192, 96)

    def __init__(self, screen):
        self.id = '1'

    def mapa(self, screen, background):
        screen.blit(background.image, background.rect)

    def file(self):
        return './data_highscore/highscore1.txt'

    def obstaculo(self, x, y, screen):
        x = int(x)
        y = int(y)
        if screen.get_at((x, y)) in (fase1.OBSTACULO, fase1.OBSTACULO2, fase1.OBSTACULO3, fase1.OBSTACULO4):
            return True
        elif fase1.LAGOX < x < fase1.LAGOX + fase1.LAGOWIDTH and fase1.LAGOY < y < fase1.LAGOY + fase1.LAGOHEIGHT:
            return True
        return False

    def verificarmissao(self, x, y, screen):
        x = int(x)
        y = int(y)
        if screen.get_at((x, y)) == fase1.YELLOW and x > 470:
            fase1.flag1 = True
            return True
        elif screen.get_at((x, y)) == fase1.YELLOW and x < 470:
            if fase1.flag1:
                fase1.flag2 = True
                fase1.time_flag2 = pygame.time.get_ticks()
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
    time_flag1 = 0
    time_flag2 = 0

    # Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    # Dimensões do Lago
    LAGOX = 227
    LAGOY = 320
    LAGOWIDTH = 302
    LAGOHEIGHT = 96

    # Cores relacionados à dinâmica de mapa
    OBSTACULO = (237, 237, 237)
    OBSTACULO2 = (216, 0, 39)
    OBSTACULO3 = (0, 0, 0)
    OBSTACULO4 = (37, 102, 3)
    RED = (255, 0, 0)
    STREET = (77, 77, 77)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (248, 202, 0)
    WHITE2 = (246, 239, 220)

    def __init__(self, screen):
        self.id = '2'

    def mapa(self, screen, background):
        screen.blit(background.image, background.rect)

    def file(self):
        return './data_highscore/highscore2.txt'

    def obstaculo(self, x, y, screen):
        x = int(x)
        y = int(y)
        if screen.get_at((x, y)) in (fase2.OBSTACULO, fase2.OBSTACULO2, fase2.OBSTACULO3, fase2.OBSTACULO4):
            return True
        elif fase2.LAGOX < x < fase2.LAGOX + fase2.LAGOWIDTH and fase2.LAGOY < y < fase2.LAGOY + fase2.LAGOHEIGHT:
            return True
        return False

    def verificarmissao(self, x, y, screen):
        x = int(x)
        y = int(y)
        if screen.get_at((x, y)) == fase2.YELLOW and x > 470:
            fase2.flag1 = True
            fase2.time_flag1 = pygame.time.get_ticks()
            pygame.draw.rect(screen, fase2.WHITE, (30, 30, 150, 30), 1)
            txt_surf = fase2.Font.render("Etapa 1 concluída", True, fase2.BLACK)
            txt_rect = txt_surf.get_rect(center=(150 // 2, 30))
            screen.blit(txt_surf, txt_rect)
        if screen.get_at((x, y)) == fase2.YELLOW and x < 470:
            if fase2.flag1:
                fase2.flag2 = True
                fase2.time_flag2 = pygame.time.get_ticks()
                pygame.draw.rect(screen, fase2.WHITE, (30, 30, 150, 30), 1)
                txt_surf = fase2.Font.render("Etapa 2 concluída", True, fase2.BLACK)
                txt_rect = txt_surf.get_rect(center=(150 // 2, 30))
                screen.blit(txt_surf, txt_rect)

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
    time_flag1 = 0
    time_flag2 = 0

    # Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    # Dimensões do Lago
    LAGOX = 227
    LAGOY = 320
    LAGOWIDTH = 302
    LAGOHEIGHT = 96

    # Cores relacionados à dinâmica de mapa
    OBSTACULO = (237, 237, 237)
    OBSTACULO2 = (216, 0, 39)
    OBSTACULO3 = (0, 0, 0)
    OBSTACULO4 = (37, 102, 3)
    RED = (255, 0, 0)
    STREET = (77, 77, 77)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (248, 202, 0)
    WHITE2 = (246, 239, 220)

    def __init__(self, screen):
        self.id = '3'

    def mapa(self, screen, background):
        screen.blit(background.image, background.rect)

    def file(self):
        return './data_highscore/highscore2.txt'

    def obstaculo(self, x, y, screen):
        x = int(x)
        y = int(y)
        if screen.get_at((x, y)) in (fase3.OBSTACULO, fase3.OBSTACULO2, fase3.OBSTACULO3, fase3.OBSTACULO4):
            return True
        elif fase3.LAGOX < x < fase3.LAGOX + fase3.LAGOWIDTH and fase3.LAGOY < y < fase3.LAGOY + fase3.LAGOHEIGHT:
            return True
        return False

    def verificarmissao(self, x, y, screen):
        x = int(x)+5
        y = int(y)+5
        if screen.get_at((x, y)) == fase3.YELLOW and x > 470:
            fase3.flag1 = True
            fase3.time_flag1 = pygame.time.get_ticks()
            pygame.draw.rect(screen, fase3.WHITE, (30, 30, 150, 30), 1)
            txt_surf = fase3.Font.render("Etapa 1 concluída", True, fase3.BLACK)
            txt_rect = txt_surf.get_rect(center=(150 // 2, 30))
            screen.blit(txt_surf, txt_rect)
        if screen.get_at((x, y)) == fase3.YELLOW and x < 470:
            if fase3.flag1:
                fase3.flag2 = True
                fase3.time_flag2 = pygame.time.get_ticks()
                pygame.draw.rect(screen, fase3.WHITE, (30, 30, 150, 30), 1)
                txt_surf = fase3.Font.render("Etapa 2 concluída", True, fase3.BLACK)
                txt_rect = txt_surf.get_rect(center=(150 // 2, 30))
                screen.blit(txt_surf, txt_rect)

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