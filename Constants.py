import math

# Parâmetros da Tela
SCREENWIDTH = 945 #largura
SCREENHEIGHT = 565 #altura

# Initialization variables
def player_constants(level):
    if level.id == '1':
        player_x0 = 0.7 * SCREENWIDTH
        player_y0 = 0.5 * SCREENHEIGHT
        player_angle = 0
    elif level.id == '2':
        player_x0 = 0.035 * SCREENWIDTH
        player_y0 = 0.168 * SCREENHEIGHT
        player_angle = 0
    else:
        player_x0 = 0.445 * SCREENWIDTH
        player_y0 = 0.1 * SCREENHEIGHT
        player_angle = 3*math.pi/2
    return (player_x0, player_y0, player_angle)


def heli_constants(level):
    if level.id == '1':
        heli_x0 = 0.7 * SCREENWIDTH
        heli_y0 = 0.5 * SCREENHEIGHT
        heli_angle = 0
        patrol_radius = 60
    elif level.id == '2':
        heli_x0 = 0.8 * SCREENWIDTH
        heli_y0 = 0.32 * SCREENHEIGHT
        heli_angle = 0
        patrol_radius = 130
    else:
        heli_x0 = 0.74 * SCREENWIDTH
        heli_y0 = 0.32 * SCREENHEIGHT
        heli_angle = 0
        patrol_radius = 65
    return (heli_x0, heli_y0, heli_angle, patrol_radius)


# Terrain parameters
angle_step = 7.5
terrain_factor = 1