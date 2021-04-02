from math import cos, sin, pi

import pygame
import sys


class GameObjects:
    def __init__(self, x=100, y=50):
        self.x = x
        self.y = y
        self.table_size = [display_size[0] - self.x * 2, display_size[1] - self.y * 2]


class MyTable(GameObjects):
    def __init__(self, x=60, y=50, k=30):
        self.k = k
        GameObjects.__init__(self, x, y)

    def draw(self):

        for x in range(self.x, self.x + self.table_size[0] + 1, self.table_size[0] // 6):
            pygame.draw.line(screen, BLACK, (x, self.y - self.k),
                             (x, self.y + self.table_size[1] + self.k))  # x - windows
        # x - axis черточки
        y1 = self.table_size[1] + self.y + self.k
        step = self.table_size[0] // 6
        for x in range(self.x, self.x + self.table_size[0], self.table_size[0] // 6):
            pygame.draw.line(screen, BLACK, (x + step / 8, self.y - self.k) , (x + step / 8, self.y - 0.8 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 4, self.y - self.k), (x + step / 4, self.y - 0.5 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 3, self.y - self.k), (x + step / 8 * 3, self.y - 0.8 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 2, self.y - self.k),
                             (x + step / 2, self.y - 0.2 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 5, self.y - self.k),
                             (x + step / 8 * 5, self.y - 0.8 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 4 * 3, self.y - self.k), (x + step / 4 * 3, self.y - 0.5 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 7, self.y - self.k), (x + step / 8 * 7, self.y - 0.8 * self.k))


            pygame.draw.line(screen, BLACK, (x + step / 8, y1), (x + step / 8, y1 - 0.2 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 4, y1), (x + step / 4, y1 - self.k * 0.5))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 3, y1),
                             (x + step / 8 * 3, y1 - 0.2 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 2, y1),
                             (x + step / 2, y1 - self.k * 0.8))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 5, y1),
                             (x + step / 8 * 5, y1 - 0.2 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 4 * 3, y1), (x + step / 4 * 3 , y1 - self.k * 0.5))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 7, y1),
                             (x + step / 8 * 7, y1 - 0.2 * self.k))


        for y in range(self.y, self.y + self.table_size[1] + 1, self.table_size[1] // 8):
            pygame.draw.line(screen, BLACK, (self.x - self.k, y),
                             (self.x + self.table_size[0] + self.k, y))  # y - windows

        # y - axis черточки
        x1 = self.table_size[0] + self.x + self.k
        step = self.table_size[1] // 8
        for y in range(self.y, self.y + self.table_size[1], self.table_size[1] // 8):
            pygame.draw.line(screen, BLACK, (self.x - self.k, y + step//4), (self.x - self.k * 0.8, y + step//4))
            pygame.draw.line(screen, BLACK, (self.x - self.k, y + step // 2), (self.x - self.k * 0.5, y + step // 2))
            pygame.draw.line(screen, BLACK, (self.x - self.k, y + step // 4 * 3), (self.x - self.k * 0.8, y + step // 4 * 3))

            pygame.draw.line(screen, BLACK, (x1, y + step // 4), (x1 - self.k * 0.2, y + step // 4))
            pygame.draw.line(screen, BLACK, (x1, y + step // 2), (x1 - self.k * 0.5, y + step // 2))
            pygame.draw.line(screen, BLACK, (x1, y + step // 4 * 3), (x1 - self.k * 0.2, y + step // 4 * 3))





        pygame.draw.line(screen, BLACK, (self.x + self.table_size[0] // 2, self.y - self.k),
                         (self.x + self.table_size[0] // 2, self.y + self.table_size[1] + self.k), 3)  # y = axis
        pygame.draw.line(screen, BLACK, (self.x - self.k, self.y + self.table_size[1] // 2),
                         (self.x + self.table_size[0] + self.k, self.y + self.table_size[1] // 2), 3)  # X - axis

        pygame.draw.rect(screen, BLACK, pygame.Rect(self.x - self.k, self.y - self.k, self.table_size[0] + self.k * 2,
                                                    self.table_size[1] + self.k * 2), 3)  # border outside




class MyCos(GameObjects):
    def __init__(self, x=60, y=50, points=None):

        GameObjects.__init__(self, x, y)
        if points is None:
            points = []

        self.points = points
        self.k = (self.table_size[0]) / (6 * pi)
        self.Amplitude = self.table_size[1] // 2
        # getting points for cos
        for x in range(self.table_size[0]):
            y = int(cos(x / self.k) * self.Amplitude + display_size[1] // 2)
            self.points.append([x + self.x, y])

    def draw(self):
        pygame.draw.aalines(screen, BLUE, False, self.points)


class MySin(GameObjects):
    def __init__(self, x=60, y=50, points=None):
        GameObjects.__init__(self, x, y)
        if points is None:
            points = []
        self.points = points

        self.k = (self.table_size[0]) / (6 * pi)
        self.Amplitude = self.table_size[1] // 2

        # getting points for sin
        for x in range(self.table_size[0] + 1):
            y = int(sin(x / self.k) * self.Amplitude + display_size[1] // 2)
            self.points.append([x + self.x, y])
        print(self.table_size)

    def draw(self):
        pygame.draw.aalines(screen, RED, False, self.points, 1)


display_size = [1050, 700]
screen = pygame.display.set_mode(display_size)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
graphObjects = []

if __name__ == '__main__':
    pygame.init()

    myCos = MyCos()
    mySin = MySin()
    myTable = MyTable()
    graphObjects.extend([myTable, mySin, myCos])

    screen.fill(WHITE)

    for obj in graphObjects:
        obj.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
