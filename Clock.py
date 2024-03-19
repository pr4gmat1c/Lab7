import pygame
from datetime import datetime

pygame.init()


screenSize = {"x":829, "y":836}
rightSize = {"x":410, "y":180}
leftSize = {"x":546, "y":140}
screen = pygame.display.set_mode((829, 836), pygame.RESIZABLE)
Mickey = pygame.image.load('main-clock.png')
right = pygame.image.load('right-hand.png')
left = pygame.image.load('left-hand.png')

angleRight = 0
angleLeft = 0
done = False


while not done:
    now = datetime.now()
    min = now.minute
    sec = now.second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    rotatedRight = pygame.transform.rotate(right, angleRight)
    rotatedRightRect = rotatedRight.get_rect()

    rotatedLeft = pygame.transform.rotate(left, angleLeft)
    rotatedLeftRect = rotatedLeft.get_rect()

    angleRight = 90 - min*6 - sec/10
    angleLeft = 90 - sec*6
    screen.blit(Mickey, (0, 0))
    screen.blit(rotatedRight, ((screenSize["x"] - rotatedRightRect.width) / 2, (screenSize["y"] - rotatedRightRect.height) / 2))
    screen.blit(rotatedLeft, ((screenSize["x"] - rotatedLeftRect.width)/2, (screenSize["y"] - rotatedLeftRect.height)/2))
    pygame.display.flip()


