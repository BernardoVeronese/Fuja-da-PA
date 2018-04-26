# Libraries
import pygame
import sys
from Functions import *

# Parâmetros da Tela
SCREENWIDTH = 945 #largura
SCREENHEIGHT = 565 #altura

tela1 = Background('./assets/highscore1.png', [0, 0])
tela2 = Background('./assets/highscore2.png', [0, 0])
tela3 = Background('./assets/highscore3.png', [0, 0])
imagem = [tela1, tela2, tela3]

# Cores RGB
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (155,   0,   0)
GREEN = (0, 155,   0)
BRIGHT_RED = (255,   0,   0)
BRIGHT_GREEN = (0, 255,   0)
GREY = (150, 150, 150)
SKYBLUE = (135, 206, 235)
YELLOW = (251, 223, 60)

# Retorno de nome e Score do HighScore a partir do histórico dos dados de Score
def read_from_file_and_find_highscore(file_name):
    file = open(file_name, 'r')  # Ler arquivo
    lines = file.readlines()  # Ler linhas do código...
    file.close  # fechar arquivo

    # Inicialmente, o Score é zero
    high_score = 0

    # Para cada linha, há a comparação
    for line in lines:
        name, score = line.strip().split(",")
        score = int(score)

        if score > high_score:
            high_score = score
            high_name = name

    return high_name, high_score

# Escrita de Score de um Jogo no arquivo de Texto
def write_to_file(file_name, your_name, points):
    score_file = open(file_name, 'a')
    print(your_name + ",", points, file=score_file)
    score_file.close()

# Mostrar Top 10 de Scores feitos
def show_top10(screen, file_name, fase):
    if fase == 0:
        screen.blit(imagem[fase].image, imagem[fase].rect)
    elif fase == 1:
        screen.blit(imagem[fase].image, imagem[fase].rect)
    else:
        screen.blit(imagem[fase].image, imagem[fase].rect)

    # Definição da Fonte
    Font = pygame.font.SysFont("aleo", 30, True)

    file = open(file_name, 'r')  # abrindo o arquivo
    lines = file.readlines()  # lendo linhas do arquivo

    all_score = []
    for line in lines:  # para cada linha,
        sep = line.index(',')
        name = line[:sep]
        score = int(line[sep + 1:-1])
        all_score.append((score, name))  # todos os dados armazenados em all_score
    file.close

    # ordenando o vetor de score
    all_score.sort(reverse=True)  # sort from largest to smallest
    best = all_score[:10]  # top 10 values)

    # write the top-10 data to the box
    for i, entry in enumerate(best):
        text = Font.render(entry[1] + "    " + str(entry[0]), True, BLACK)
        screen.blit(text, (300, 75 + i*29))

    pygame.display.flip()

    while True:  # wait for user to acknowledge and return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_BACKSPACE]:
                return
        pygame.time.wait(20)


def enterbox(screen, txt):
    def blink(screen):
        for color in [GREY, WHITE]:
            pygame.draw.circle(box, color, (bx // 2, int(by * 0.7)), 7, 0)
            screen.blit(box, (0, by // 2))
            pygame.display.flip()
            pygame.time.wait(300)

    def show_name(screen, name):
        # Definição da Fonte
        Font = pygame.font.SysFont("arial", 20, True)
        pygame.draw.rect(box, WHITE, (50, 60, bx - 100, 20), 0)
        txt_surf = Font.render(name, True, BLACK)
        txt_rect = txt_surf.get_rect(center=(bx // 2, int(by * 0.7)))
        box.blit(txt_surf, txt_rect)
        screen.blit(box, (0, by // 2))
        pygame.display.flip()

    # Definiçãoda Fonte
    Font = pygame.font.SysFont("arial", 20, True)

    bx = 480
    by = 100

    # make box
    box = pygame.surface.Surface((bx, by))
    box.fill(GREY)
    pygame.draw.rect(box, BLACK, (0, 0, bx, by), 1)
    txt_surf = Font.render(txt, True, BLACK)
    txt_rect = txt_surf.get_rect(center=(bx // 2, int(by * 0.3)))
    box.blit(txt_surf, txt_rect)

    name = ""
    show_name(screen, name)

    # Loop para coletar a digitação do nome
    while True:
        for event in pygame.event.get():
            # 1ro evento - Finalização do programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 2ndo evento - Pressionando alguma tecla
            elif event.type == pygame.KEYDOWN:
                inkey = event.key
                if inkey in [13, 271]:  # enter/return key
                    return name
                elif inkey == 8:  # backspace key
                    name = name[:-1]
                elif inkey <= 300:  # characters keys
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT and 122 >= inkey >= 97:
                        inkey -= 32  # handles CAPITAL input
                    name += chr(inkey)

        if name == "":
            blink(screen)
        show_name(screen, name)


# Método relacionado a coletar o Score de cada pessoa ao fim de cada fase
def get_score(screen, file_name, your_points):
    # pegar highscore atual
    high_name, high_score = read_from_file_and_find_highscore(file_name)

    if your_points > high_score:  # se o score é maior que o HighScore
        your_name = enterbox(screen, "Você bateu o High Score! Qual seu nome?")

    elif your_points == high_score:  # se o score é igual ao HighScore
        your_name = enterbox(screen, "Você conseguiu o mesmo Score do High Score. Qual seu nome?")

    elif your_points < high_score:  # Se o score é menor que o HighScore
        st1 = "O Highscore é "
        st2 = " feito por "
        st3 = "   Qual o seu nome?"
        txt = st1 + str(high_score) + st2 + high_name + st3
        your_name = enterbox(screen, txt)

    if your_name == None or len(your_name) == 0:
        return  # do not update the file unless a name is given

    # escrever score que foi registrado no arquivo
    write_to_file(file_name, your_name, your_points)
    return
