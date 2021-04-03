import pygame
import math
import sys
from settings import SIZE, WHITE, RED, BLUE, BLACK, GREEN

pygame.init()
win = pygame.display.set_mode(SIZE)
pygame.display.set_caption("FUNCTION")
play = True
font = pygame.font.SysFont("comicsansms", 15)
t0 = font.render("1.00", True, (BLACK))
t1 = font.render("0.75", True, (BLACK))
t2 = font.render("0.50", True, (BLACK))
t3 = font.render("0.25", True, (BLACK))
t4 = font.render("0.00", True, (BLACK))
t5 = font.render("0.25", True, (BLACK))
t6 = font.render("0.50", True, (BLACK))
t7 = font.render("0.75", True, (BLACK))
t8 = font.render("1.00", True, (BLACK))

listOfStrX = ['-3п', '-5п/2', '-2п', '-3п/2', '-п', '-п/2', '0', 'п/2', 'п', '3п/2', '2п', '5п/2', '3п']
tableSize = [660, 540]
i = 0
k = 70

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
    win.fill(WHITE)

    pygame.draw.rect(win, BLACK, (70, 10, 660, 540), 2)
    pygame.draw.line(win, BLACK, (70, 280), (730, 280), 2)
    pygame.draw.line(win, BLACK, (400, 10), (400, 550), 2)
    pygame.draw.line(win, BLACK, (70, 40), (730, 40))
    pygame.draw.line(win, BLACK, (70, 520), (730, 520))
    pygame.draw.line(win, BLACK, (100, 10), (100, 550))
    pygame.draw.line(win, BLACK, (700, 10), (700, 550))

    for x in range(100, 701, 100):
        pygame.draw.line(win, BLACK, (x, 10), (x, 550))

    for x in range(100, 701, 50):
        pygame.draw.line(win, BLACK, (x, 10), (x, 30))

        pygame.draw.line(win, BLACK, (x, 550), (x, 530))

    for x in range(100, 701, 25):
        pygame.draw.line(win, BLACK, (x, 10), (x, 20))
        pygame.draw.line(win, BLACK, (x, 550), (x, 540))

    for y in range(40, 521, 60):
        pygame.draw.line(win, BLACK, (70, y), (730, y))

    for y in range(40, 521, 30):
        pygame.draw.line(win, BLACK, (70, y), (90, y))
        pygame.draw.line(win, BLACK, (710, y), (730, y))

    for y in range(40, 521, 15):
        pygame.draw.line(win, BLACK, (70, y), (80, y))
        pygame.draw.line(win, BLACK, (720, y), (730, y))

    for x in range(114, 701, 25):
        pygame.draw.line(win, BLACK, (x, 10), (x, 15))
        # mini lines
    for x in range(114, 701, 25):
        pygame.draw.line(win, BLACK, (x, 550), (x, 545))

    for x in range(340, 550, 60):
        pygame.draw.line(win, BLACK, (30, x), (35, x))
    for y in range(54, 351, 50):
        pygame.draw.line(win, BLACK, (30 + y, 558), (35 + y, 558))

        win.blit(t0, (37, 28))
        win.blit(t1, (37, 88))
        win.blit(t2, (37, 148))
        win.blit(t3, (37, 208))
        win.blit(t4, (37, 268))
        win.blit(t5, (37, 328))
        win.blit(t6, (37, 388))
        win.blit(t7, (37, 448))
        win.blit(t8, (37, 508))

    for x in range(k, k + tableSize[0] + 1, tableSize[0] // 13):
        text = font.render(listOfStrX[i], True, BLACK)
        win.blit(text, (100, 550))
        while i < len(listOfStrX) + 1:
            i += 1

    for x in range(100, 700):
        cos_y1 = 240 * math.cos((x - 100) / 100 * math.pi)
        cos_y2 = 240 * math.cos((x - 99) / 100 * math.pi)
        pygame.draw.aalines(win, BLUE, False, [(x, 280 + cos_y1), ((x + 1), 280 + cos_y2)])
