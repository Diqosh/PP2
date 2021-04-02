import pygame, sys
from math import cos, sin, pi


class GameObjects:
    def __init__(self, x=100, y=50):
        self.x = x
        self.y = y
        self.table_size = [display_size[0] - self.x * 2, display_size[1] - self.y * 2]


class MyTable(GameObjects):
    def __init__(self, x=60, y=50):
        GameObjects.__init__(self, x, y)

    def draw(self):
        for x in range(self.x, self.x + self.table_size[0] + 1, self.table_size[0] // 6):
            pygame.draw.line(screen, BLACK, (x, self.y), (x, self.y + self.table_size[1]))

        for y in range(self.y, self.y + self.table_size[1] + 1, self.table_size[1] // 8):
            pygame.draw.line(screen, BLACK, (self.x, y), (self.x + self.table_size[0], y))

        pygame.draw.line(screen, BLACK, (self.x + self.table_size[0] // 2, self.y),
                         (self.x + self.table_size[0] // 2, self.y + self.table_size[1]), 3)  # y = axis
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.table_size[1] // 2),
                         (self.x + self.table_size[0], self.y + self.table_size[1] // 2), 3)  # X - axis


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
        for x in range(self.table_size[0]):
            y = int(sin(x / self.k) * self.Amplitude + display_size[1] // 2)
            self.points.append([x + self.x, y])
        print(self.table_size)

    def draw(self):
        pygame.draw.aalines(screen, RED, False, self.points)


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
    graphObjects.extend([mySin, myCos, myTable])

    screen.fill(WHITE)

    for obj in graphObjects:
        obj.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
