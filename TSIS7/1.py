import pygame, sys
from math import cos, sin, pi


class MyTable:
    def __init__(self):
        pass

    def draw(self):
        x, y = 60, 10
        lineWight = 2
        table_size = [display_size[0] - 100, display_size[1] - 100]

        pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, table_size[0], table_size[1]), lineWight)  # main border
        pygame.draw.line(screen, BLACK, (table_size[0] // 2 + x, y), (table_size[0] // 2 + x, table_size[1] + y),
                         lineWight)  # y-axis
        pygame.draw.line(screen, BLACK, (x, table_size[1]//2 + y), (x + table_size[0], table_size[1]//2 + y), lineWight)# x-axis
`

class MyCos:
    def __init__(self, points=[]):
        self.points = points

        for x in range(display_size[0]):
            y = int(-cos(x / 840 * 6 * pi) * 200 + display_size[1] // 2)
            self.points.append([x, y])

    def draw(self):
        pygame.draw.lines(screen, RED, False, self.points, 3)


display_size = [840, 700]
screen = pygame.display.set_mode(display_size)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
graphObjects = []

if __name__ == '__main__':
    pygame.init()

    myCos = MyCos()
    myTable = MyTable()
    graphObjects.extend([myTable,myCos])

    screen.fill(WHITE)

    for object in graphObjects:
        object.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
