from math import cos, sin, pi

import pygame
import sys


class GameObjects:
    def __init__(self, x=75, y=100):
        self.x = x
        self.y = y
        self.table_size = [display_size[0] - self.x * 2, display_size[1] - self.y * 2]


class MyFonts(GameObjects):
    def __init__(self, k=30, font_size=17):
        self.k = k
        self.font_size = font_size
        GameObjects.__init__(self)
        self.listOfStrY = ['1.00', '0.75', '0.50', '0.25', '0.00', '-0.25', '-0.50', '-0.75', '-1.00']
        self.listOfStrX = ['-3п', '-5п', '-2п', '-3п', '-п', '-п', '0', 'п', 'п', '3п', '2п', '5п', '3п']
        self.font = pygame.font.SysFont("roboto", self.font_size, italic=True)
        self.two = self.font.render('2', font_size, True, WHITE)
        self.fontBI = pygame.font.SysFont("roboto", 30, bold=True, italic=True)
        self.fontI = pygame.font.SysFont("roboto", 30, italic=True)
        self.i = 0

    def draw(self):
        # y - axis
        for y in range(self.y, self.y + self.table_size[1] + 1, self.table_size[1] // 8):
            text = self.font.render(self.listOfStrY[self.i], True, BLACK)
            screen.blit(text, (5, y - 10))
            self.i += 1

        self.i = 0

        # x - axis
        for x in range(self.x, self.x + self.table_size[0] + 1, self.table_size[0] // 12):
            text = self.font.render(self.listOfStrX[self.i], True, BLACK)
            screen.blit(text, (x - text.get_width() // 2, self.table_size[1] + self.y + self.k))

            if self.i % 2 == 1 and self.i != 6:
                # draw a line for dividing
                pygame.draw.line(screen, BLACK,
                                 (x - text.get_width() // 2, self.table_size[1] + self.y + self.k + text.get_height()),
                                 (x + text.get_width() // 2, self.table_size[1] + self.y + self.k + text.get_height()))
                # divide by 2
                screen.blit(self.two, (x - 5, self.table_size[1] + self.y + self.k + text.get_height() + 2))

            self.i += 1

        # draw big X
        text = self.fontBI.render('X', True, BLACK)
        screen.blit(text, (
            self.x + self.table_size[0] // 2 - text.get_width() // 2, self.y * 1.2 + self.table_size[1] + self.k))

        # draw sin cos
        # 1)first clear one windows for draw cos and sin
        pygame.draw.line(screen, WHITE, (self.x + self.table_size[0] // 6 * 4, self.y + 1),
                         (self.x + self.table_size[0] // 6 * 4, self.y + self.table_size[1] // 8 - 1))
        # 2)draw them
        sin = self.fontI.render('sin x', self.font_size, BLACK)
        cos = self.fontI.render('cos x', self.font_size, BLACK)
        screen.blit(sin, (self.x + self.table_size[0] // 6 * 4 - sin.get_width() // 2, self.y))
        screen.blit(cos, (self.x + self.table_size[0] // 6 * 4 - sin.get_width() // 2, self.y + sin.get_height()))

        # 3) draw them lines
        lineWidht = 40
        pygame.draw.line(screen, RED,
                         (self.x + self.table_size[0] // 6 * 4 + sin.get_width() // 2, self.y + sin.get_height() // 2),
                         (self.x + self.table_size[0] // 6 * 4 + sin.get_width() // 2 + lineWidht,
                          self.y + sin.get_height() // 2))
        pygame.draw.line(screen, BLUE,
                         (self.x + self.table_size[0] // 6 * 4 + cos.get_width() // 2,
                          self.y + sin.get_height() + cos.get_height() // 2),
                         (self.x + self.table_size[0] // 6 * 4 + cos.get_width() // 2 + lineWidht,
                          self.y + + sin.get_height() + cos.get_height() // 2))


class MyTable(GameObjects):
    def __init__(self, k=30):
        self.k = k
        GameObjects.__init__(self)

    def draw(self):
        # x - windows
        for x in range(self.x, self.x + self.table_size[0] + 1, self.table_size[0] // 6):
            pygame.draw.line(screen, BLACK, (x, self.y - self.k),
                             (x, self.y + self.table_size[1] + self.k))

        # x - axis черточки
        y1 = self.table_size[1] + self.y + self.k
        step = self.table_size[0] // 6
        for x in range(self.x, self.x + self.table_size[0], self.table_size[0] // 6):
            pygame.draw.line(screen, BLACK, (x + step / 8, self.y - self.k), (x + step / 8, self.y - 0.8 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 4, self.y - self.k), (x + step / 4, self.y - 0.5 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 3, self.y - self.k),
                             (x + step / 8 * 3, self.y - 0.8 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 2, self.y - self.k),
                             (x + step / 2, self.y - 0.2 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 5, self.y - self.k),
                             (x + step / 8 * 5, self.y - 0.8 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 4 * 3, self.y - self.k),
                             (x + step / 4 * 3, self.y - 0.5 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 7, self.y - self.k),
                             (x + step / 8 * 7, self.y - 0.8 * self.k))

            pygame.draw.line(screen, BLACK, (x + step / 8, y1), (x + step / 8, y1 - 0.2 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 4, y1), (x + step / 4, y1 - self.k * 0.5))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 3, y1),
                             (x + step / 8 * 3, y1 - 0.2 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 2, y1),
                             (x + step / 2, y1 - self.k * 0.8))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 5, y1),
                             (x + step / 8 * 5, y1 - 0.2 * self.k))
            pygame.draw.line(screen, BLACK, (x + step / 4 * 3, y1), (x + step / 4 * 3, y1 - self.k * 0.5))
            pygame.draw.line(screen, BLACK, (x + step / 8 * 7, y1),
                             (x + step / 8 * 7, y1 - 0.2 * self.k))
        # y - windows
        for y in range(self.y, self.y + self.table_size[1] + 1, self.table_size[1] // 8):
            pygame.draw.line(screen, BLACK, (self.x - self.k, y),
                             (self.x + self.table_size[0] + self.k, y))

        # y - axis черточки
        x1 = self.table_size[0] + self.x + self.k
        step = self.table_size[1] // 8
        for y in range(self.y, self.y + self.table_size[1], self.table_size[1] // 8):
            pygame.draw.line(screen, BLACK, (self.x - self.k, y + step // 4), (self.x - self.k * 0.8, y + step // 4))
            pygame.draw.line(screen, BLACK, (self.x - self.k, y + step // 2), (self.x - self.k * 0.5, y + step // 2))
            pygame.draw.line(screen, BLACK, (self.x - self.k, y + step // 4 * 3),
                             (self.x - self.k * 0.8, y + step // 4 * 3))

            pygame.draw.line(screen, BLACK, (x1, y + step // 4), (x1 - self.k * 0.2, y + step // 4))
            pygame.draw.line(screen, BLACK, (x1, y + step // 2), (x1 - self.k * 0.5, y + step // 2))
            pygame.draw.line(screen, BLACK, (x1, y + step // 4 * 3), (x1 - self.k * 0.2, y + step // 4 * 3))

        pygame.draw.line(screen, BLACK, (self.x + self.table_size[0] // 2, self.y - self.k),
                         (self.x + self.table_size[0] // 2, self.y + self.table_size[1] + self.k), 3)  # y - axis
        pygame.draw.line(screen, BLACK, (self.x - self.k, self.y + self.table_size[1] // 2),
                         (self.x + self.table_size[0] + self.k, self.y + self.table_size[1] // 2), 3)  # x - axis

        pygame.draw.rect(screen, BLACK, pygame.Rect(self.x - self.k, self.y - self.k, self.table_size[0] + self.k * 2,
                                                    self.table_size[1] + self.k * 2), 3)  # border outside


class MyCos(GameObjects):
    def __init__(self, points=None):

        GameObjects.__init__(self)
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
        # draw cos
        pygame.draw.aalines(screen, BLUE, False, self.points)

        # make a dashed
        for x in range(self.x, self.x + self.table_size[0], self.table_size[0] // 3):
            y = self.table_size[1] + self.y
            pygame.draw.rect(screen, WHITE,
                             pygame.Rect(x + self.table_size[0] // (6 * 8) - 5, y - self.table_size[1] // (16) - 5, 20,
                                         20))
            pygame.draw.rect(screen, WHITE,
                             pygame.Rect(x + self.table_size[0] // (6 * 8) * 3 - 5,
                                         y - self.table_size[1] // 16 * 5 - 5,
                                         20, 20))
            pygame.draw.rect(screen, WHITE,
                             pygame.Rect(x + self.table_size[0] // (6 * 8) * 5 - 15,
                                         y - self.table_size[1] // (16) * 9 - 5,
                                         20, 20))
            pygame.draw.rect(screen, WHITE,
                             pygame.Rect(x + self.table_size[0] // (6 * 8) * 7 - 30,
                                         y - self.table_size[1] // 16 * 14 + 20,
                                         20, 20))
            pygame.draw.rect(screen, WHITE,
                             pygame.Rect(x + self.table_size[0] // 6 * 2 - 35, y - self.table_size[1] // (16) - 5, 20,
                                         20))
            pygame.draw.rect(screen, WHITE,
                             pygame.Rect(x + self.table_size[0] // (6) * 2 - 65,
                                         y - self.table_size[1] // 16 * 5 - 5,
                                         20, 20))
            pygame.draw.rect(screen, WHITE,
                             pygame.Rect(x + self.table_size[0] // (6) * 2 - 85,
                                         y - self.table_size[1] // (16) * 9 - 5,
                                         20, 20))
            pygame.draw.rect(screen, WHITE,
                             pygame.Rect(x + self.table_size[0] // (6) * 2 - 110,
                                         y - self.table_size[1] // 16 * 14 + 20,
                                         20, 20))

            # make dashed in window

            pygame.draw.rect(screen, WHITE, pygame.Rect(725, 143, 15, 20))


class MySin(GameObjects):
    def __init__(self, x=75, y=100, points=None):
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

    def draw(self):
        pygame.draw.aalines(screen, RED, False, self.points, 1)


display_size = [1050, 800]
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
    myFonts = MyFonts()
    graphObjects.extend([myTable, mySin, myFonts, myCos])

    screen.fill(WHITE)

    for obj in graphObjects:
        obj.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
