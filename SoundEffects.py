import pygame

def music_selection(level):
    if level.id == '1':
        pass
    elif level.id == '2':
        pygame.mixer.music.load('./assets/SoundEffects/Track2.mp3')
    else:
        pygame.mixer.music.load('./assets/SoundEffects/Track3.mp3')