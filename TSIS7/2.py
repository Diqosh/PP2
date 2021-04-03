import pygame
import math

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((780, 560))
surface = pygame.Surface((600, 318))
surface.fill(WHITE)
win_ceny = surface.get_height() // 2
xpos = 0
xpos2 = 0
ypos = 0
step = -3 * math.pi
step2 = -3 * math.pi
clock = pygame.time.Clock()
fps = 10000
run = True
font = pygame.font.SysFont("cerif", 25, False, True)
font2 = pygame.font.SysFont("cerif", 35, False, True)
x_txt = font2.render("X", True, BLACK)
text2 = font.render("-3П    -2,5П    -2П    -1,5П    -П    -0,5П    0      0,5П     П     1,5П     2П     2,5П    3П",
                    True, BLACK)
l1 = (-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        run = False

    screen.blit(surface, (80, 22))
    for i in l1:
        text = font.render(str(i), True, BLACK)
        screen.blit(text, (5, -i * 159 + 170))
        pygame.draw.line(screen, BLACK, (50, -i * 159 + 180), (705, -i * 159 + 180))

    screen.blit(text2, (60, 365))
    pygame.draw.line(screen, BLACK, (50, 5), (50, 360), 3)
    pygame.draw.line(screen, BLACK, (380, 5), (380, 360), 3)
    pygame.draw.line(screen, BLACK, (705, 5), (705, 360), 3)
    pygame.draw.line(screen, BLACK, (50, 5), (705, 5), 3)
    pygame.draw.line(screen, BLACK, (50, 180), (705, 180), 3)
    pygame.draw.line(screen, BLACK, (50, 360), (705, 360), 3)

    for i in range(7):
        pygame.draw.line(screen, BLACK, (i * 100 + 80, 5), (i * 100 + 80, 360))

    for i in range(8):
        pygame.draw.line(screen, BLACK, (50, i * 40 + 40), (65, i * 40 + 40))
        pygame.draw.line(screen, BLACK, (50, i * 40 + 30), (60, i * 40 + 30))
        pygame.draw.line(screen, BLACK, (50, i * 40 + 50), (60, i * 40 + 50))

        pygame.draw.line(screen, BLACK, (705, i * 40 + 40), (690, i * 40 + 40))
        pygame.draw.line(screen, BLACK, (705, i * 40 + 30), (695, i * 40 + 30))
        pygame.draw.line(screen, BLACK, (705, i * 40 + 50), (695, i * 40 + 50))

    for i in range(6):
        pygame.draw.line(screen, BLACK, (i * 100 + 130, 5), (i * 100 + 130, 18))
        pygame.draw.line(screen, BLACK, (i * 100 + 130, 360), (i * 100 + 130, 347))

        pygame.draw.line(screen, BLACK, (i * 100 + 105, 360), (i * 100 + 105, 351))
        pygame.draw.line(screen, BLACK, (i * 100 + 105, 5), (i * 100 + 105, 14))
        pygame.draw.line(screen, BLACK, (i * 100 + 155, 360), (i * 100 + 155, 351))
        pygame.draw.line(screen, BLACK, (i * 100 + 155, 5), (i * 100 + 155, 14))

        pygame.draw.line(screen, BLACK, (i * 100 + 90, 360), (i * 100 + 90, 355))
        pygame.draw.line(screen, BLACK, (i * 100 + 90, 5), (i * 100 + 90, 10))
        pygame.draw.line(screen, BLACK, (i * 100 + 120, 360), (i * 100 + 120, 355))
        pygame.draw.line(screen, BLACK, (i * 100 + 120, 5), (i * 100 + 120, 10))
        pygame.draw.line(screen, BLACK, (i * 100 + 145, 360), (i * 100 + 145, 355))
        pygame.draw.line(screen, BLACK, (i * 100 + 145, 5), (i * 100 + 145, 10))
        pygame.draw.line(screen, BLACK, (i * 100 + 170, 360), (i * 100 + 170, 355))
        pygame.draw.line(screen, BLACK, (i * 100 + 170, 5), (i * 100 + 170, 10))
    screen.blit(x_txt, (370, 400))

    ypos = -1 * math.sin(step) * 158 + win_ceny
    ypos2 = -1 * math.cos(step2) * 158 + win_ceny
    pygame.draw.circle(surface, (255, 0, 0), (int(xpos), int(ypos)), 1)
    pygame.draw.circle(surface, (0, 0, 255), (int(xpos2), int(ypos2)), 1)
    xpos += 0.255
    xpos2 += 1.02
    step += 0.008
    step2 += 0.032
    pygame.display.flip()
    clock.tick(fps)
