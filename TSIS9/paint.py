import pygame, sys
from pygame import *

pygame.init()

counter_to_fix = 0

selected_eraser = False
selected_rect = False
selected_circle = False
mouse_click = False
prevPoint = list()
lastPoint = list()
to_draw = False
to_erase = False
font = pygame.font.SysFont('roboto', 40)
prevPoint = list()
lastPoint = list()
DISPLAY_SIZE = [800, 800]
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((DISPLAY_SIZE[0], DISPLAY_SIZE[1]))
pygame.display.set_caption('SNAKE')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
isPressed = False
color = BLACK


def save():
    pygame.image.save(SCREEN, 'Materials/imagePaint.png')

def draw_text(text, color, xpos, ypos):
    textobj = font.render(text, True, color)
    text_rect = textobj.get_rect(topleft=(xpos, ypos))
    SCREEN.blit(textobj, text_rect)
    return text_rect


class Rectangle:
    def __init__(self, first_points, second_points, color=BLACK, width=1):
        self.first_points = first_points
        self.second_points = second_points
        self.size = [second_points[0] - first_points[0], second_points[1] - first_points[1]]
        self.color = color
        self.width = width

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, Rect(*self.first_points, *self.size), self.width)


class Eraser:
    def __init__(self, points, width=10):
        self.center = points
        self.width = width

    def draw(self):
        pygame.draw.circle(SCREEN, WHITE, self.center, self.width)


class Circle:
    def __init__(self, first_points, second_points, color=RED, width=1):
        self.first_points = first_points
        self.second_points = second_points
        self.diameter = second_points[0] - first_points[0] if second_points[0] - first_points[0] < second_points[1] - \
                                                              first_points[1] else second_points[1] - first_points[1]
        self.radius = self.diameter // 2
        self.center = [(second_points[0] + first_points[0]) // 2, (second_points[1] + first_points[1]) // 2]
        self.color = color
        self.width = width

    def draw(self):
        pygame.draw.circle(SCREEN, self.color, self.center, self.radius, self.width)


if __name__ == '__main__':

    SCREEN.fill(WHITE)
    while True:
        x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()
        clock.tick(80)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                isPressed = True
                to_erase = True
                prevPoint_tuple = pygame.mouse.get_pos()
                prevPoint = list(prevPoint_tuple)
                mouse_click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                to_draw = True
                isPressed = False

            elif event.type == pygame.MOUSEMOTION and isPressed == True:
                lastPoint_tuple = pygame.mouse.get_pos()
                lastPoint = list(lastPoint_tuple)
                if to_erase and selected_eraser:
                    eraser = Eraser(lastPoint)
                    eraser.draw()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    color = BLACK
                elif event.key == pygame.K_r:
                    color = RED
                elif event.key == pygame.K_g:
                    color = GREEN
                elif event.key == pygame.K_b:
                    color = BLUE
                elif event.key == pygame.K_s:
                    save()

        rect_eraser = draw_text('eraser', BLUE, 10, 10)
        rect_rect = draw_text('rectangle', BLUE, 40 + rect_eraser.width, 10)
        rect_circle = draw_text('circle', BLUE, 70 + rect_eraser.width + rect_rect.width, 10)
        if rect_eraser.collidepoint((x_pos_mouse, y_pos_mouse)):
            draw_text('eraser', RED, 10, 10)
            if mouse_click:
                selected_eraser = True
                selected_rect = False
                selected_circle = False
                mouse_click = False

        if rect_rect.collidepoint((x_pos_mouse, y_pos_mouse)):
            draw_text('rectangle', RED, 40 + rect_eraser.width, 10)
            if mouse_click:
                counter_to_fix += 1
                selected_eraser = False
                selected_rect = True
                selected_circle = False
                mouse_click = False

        if rect_circle.collidepoint((x_pos_mouse, y_pos_mouse)):
            draw_text('circle', RED, 70 + rect_eraser.width + rect_rect.width, 10)
            if mouse_click:
                selected_eraser = False
                selected_rect = False
                selected_circle = True
                mouse_click = False

        if to_draw:
            to_draw = False

            if selected_rect:
                rect = Rectangle(prevPoint, lastPoint, color=color)
                rect.draw()
            if selected_circle:
                circle = Circle(prevPoint, lastPoint, color=color)
                circle.draw()

        pygame.display.flip()
