import pygame
import os

pygame.init()
track_files = [f for f in os.listdir('tracks') if f.endswith('.mp3')]
pygame.mixer.init()
W,H = 612, 512

sc = pygame.display.set_mode((W,H), pygame.RESIZABLE)
music = pygame.image.load('music.jpg')

def play(file):
    pygame.mixer.music.load(os.path.join('tracks', file))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next():
    global cur_music
    cur = track_files.index(cur_music)
    cur_music = (track_files[(cur + 1)%len(track_files)])
    play(cur_music)

def previous():
    global cur_music
    cur = track_files.index(cur_music)
    cur_music = (track_files[(cur - 1) if cur - 1 >= 0 else len(track_files) - 1])
    play(cur_music)

running = True
cur_music = track_files[0]
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer.music.get_busy():
                    stop()
                else:
                    play(cur_music)
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_n:
                next()
            elif event.key == pygame.K_b:
                previous()
        elif event.type == pygame.QUIT:
            running = False

pygame.quit()