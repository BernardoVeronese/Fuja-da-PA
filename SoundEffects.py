import pygame

def music_selection(level):
    if level.id == '1':
        pass
    elif level.id == '2':
        pygame.mixer.music.load('./assets/SoundEffects/Track2.mp3')
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load('./assets/SoundEffects/Track3.mp3')
        pygame.mixer.music.play()

def game_over_sound():
    pygame.mixer.music.load('./assets/SoundEffects/GameOver.mp3')
    pygame.mixer.music.play()