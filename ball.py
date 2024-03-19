import pygame
pygame.init()

w = 400
h = 400

WHITE = (255, 255, 255)
RED = (255, 0, 0)

radius = 25
size = radius * 2

ball_x = (w - size) // 2
ball_y = (h - size) // 2

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Exercise_3")

while True:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), radius)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - 20 >= 0:
                    ball_y -= 20
            elif event.key == pygame.K_DOWN:
                if ball_y + size - 20 <= h:
                    ball_y += 20
            elif event.key == pygame.K_LEFT:
                if ball_x - 20 >= 0:
                    ball_x -= 20
            elif event.key == pygame.K_RIGHT:
                if ball_x + size - 20 <= w:
                    ball_x += 20
