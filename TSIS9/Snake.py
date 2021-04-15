import pygame, random, sys, json
from pygame.math import Vector2
from pygame import *

pygame.init()

json_file = open('Materials/snake.json', 'r', encoding='utf-8')
myDict = json.load(json_file)
counter_for_level = 0
list_bodies_snake_after_pause = []
direction_snake_after_pause = None

PAUSE = False
score = 0
mouse_click = False
eat_sound = pygame.mixer.Sound('Materials/eat.wav')
eat_sound.set_volume(0.1)
font = pygame.font.SysFont('roboto', 60)
font_small = pygame.font.SysFont('roboto', 20)
bg_block_image = pygame.image.load('Materials/bg.png')
wall_block_image = pygame.image.load('Materials/wall.png')
apple_image = pygame.image.load('Materials/apple.png')
table_image = pygame.image.load('Materials/table.png')
table_image.set_alpha(200)
sizeOfCeil = 40
numOfCeil = 20
DISPLAY_SIZE = [800, 800]
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((sizeOfCeil * numOfCeil, sizeOfCeil * numOfCeil))
pygame.display.set_caption('SNAKE')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw_text(text, color, xpos, ypos):
    textobj = font.render(text, True, color)
    text_rect = textobj.get_rect(center=(xpos, ypos))
    SCREEN.blit(textobj, text_rect)
    return text_rect


class Bacgraund:
    def __init__(self):
        pass

    def draw(self):
        # bg draw
        for x in range(numOfCeil):
            for y in range(numOfCeil):
                SCREEN.blit(bg_block_image, (x * sizeOfCeil * 2, y * sizeOfCeil * 2))

        # wall draw
        for x in range(numOfCeil):
            SCREEN.blit(wall_block_image, (x * sizeOfCeil, 0))
            SCREEN.blit(wall_block_image, (x * sizeOfCeil, sizeOfCeil * (numOfCeil - 1)))
        for y in range(numOfCeil):
            SCREEN.blit(wall_block_image, (0, y * sizeOfCeil))
            SCREEN.blit(wall_block_image, (sizeOfCeil * (numOfCeil - 1), y * sizeOfCeil))
        # table and score draw
        SCREEN.blit(table_image, table_image.get_rect(topright=(numOfCeil * sizeOfCeil, 0)))
        score_image = font_small.render(f'Score: {score}', True, BLACK)
        SCREEN.blit(score_image, score_image.get_rect(topleft=((numOfCeil - 3) * sizeOfCeil, 0)))


class Snake(pygame.sprite.Sprite):
    def __init__(self, body=None, direction=None):
        super(Snake, self).__init__()
        if body == None:
            self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        else:
            self.body = body
        if direction == None:
            self.direction = Vector2(1, 0)
        else:
            self.direction = direction
        self.needToAdd = False

    def draw(self):
        for block in self.body:
            x_pos = block.x * sizeOfCeil
            y_pos = block.y * sizeOfCeil
            blockRect = pygame.Rect(x_pos, y_pos, sizeOfCeil, sizeOfCeil)
            pygame.draw.rect(SCREEN, BLUE, blockRect)

    def move(self):
        if self.needToAdd:
            self.needToAdd = False
            body_copy = self.body[:]
        else:
            body_copy = self.body[1:]

        body_copy.append(self.body[-1] + self.direction)
        self.body = body_copy
        self.checkCollisionWithFruit()
        self.condiotions_game_over()

    def checkCollisionWithFruit(self):
        global score
        if self.body[-1] == fruit.posFruit:
            fruit.x = random.randint(1, numOfCeil - 2)
            fruit.y = random.randint(1, numOfCeil - 2)
            fruit.posFruit = Vector2(fruit.x, fruit.y)
            self.needToAdd = True
            score += 1
            eat_sound.play()

    def condiotions_game_over(self):
        if not 1 <= self.body[-1].x < numOfCeil - 1 or not 1 <= self.body[-1].y < numOfCeil - 1:
            self.kill()
            self.game_over()

        for block in self.body[:-1]:
            if block == self.body[-1]:
                self.kill()
                self.game_over()
        pass

    def game_over(self):

        menu()


class Friut(pygame.sprite.Sprite):
    def __init__(self):
        super(Friut, self).__init__()
        self.x = random.randint(1, numOfCeil - 2)
        self.y = random.randint(1, numOfCeil - 2)
        self.posFruit = Vector2(self.x, self.y)

    def draw(self):
        SCREEN.blit(apple_image, (self.x * sizeOfCeil, self.y * sizeOfCeil))


fruit = Friut()

bg = Bacgraund()


def game_loop(level, body_snake_after_pause, direction_snake):
    global list_bodies_snake_after_pause, direction_snake_after_pause
    snake = Snake(body_snake_after_pause, direction_snake)
    game_obj = []
    game_obj.extend([bg, fruit, snake])
    # every 100 ms rum snake.move
    global PAUSE
    level += 1
    ms = 120 // level
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, ms)
    while not PAUSE:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == SCREEN_UPDATE:
                snake.move()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if snake.direction.x != 1:
                        snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_d:
                    if snake.direction.x != -1:
                        snake.direction = Vector2(1, 0)
                elif event.key == pygame.K_w:
                    if snake.direction.y != 1:
                        snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_s:
                    if snake.direction.y != -1:
                        snake.direction = Vector2(0, 1)
                elif event.key == K_ESCAPE:
                    PAUSE = True
                    list_bodies_snake_after_pause = snake.body
                    direction_snake_after_pause = snake.direction

        for obj in game_obj:
            obj.draw()

        pygame.display.flip()
        clock.tick(60)


def menu():
    global mouse_click, PAUSE, list_bodies_snake_after_pause, direction_snake_after_pause, counter_for_level, myDict

    level = ['Easy', 'Medium', 'even dont try please']

    while True:

        # counter handler
        if counter_for_level > 2:
            counter_for_level = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_click = True

        SCREEN.fill(BLACK)
        rect_start = draw_text('start game', WHITE, DISPLAY_SIZE[0] // 2, 200)
        rect_level = draw_text(f'level: {level[counter_for_level]}', WHITE, DISPLAY_SIZE[0] // 2, 300)
        rect_resume = draw_text('resume', WHITE, DISPLAY_SIZE[0] // 2, 400)
        rect_save = draw_text('save', WHITE, DISPLAY_SIZE[0] // 2, 500)
        rect_quit = draw_text('quit', WHITE, DISPLAY_SIZE[0] // 2, 600)
        x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()

        if rect_start.collidepoint((x_pos_mouse, y_pos_mouse)):
            draw_text('start game', RED, DISPLAY_SIZE[0] // 2, 200)
            if mouse_click:
                mouse_click = False
                game_loop(counter_for_level, None, None)

        if rect_level.collidepoint((x_pos_mouse, y_pos_mouse)):
            draw_text(f'level: {level[counter_for_level]}', RED, DISPLAY_SIZE[0] // 2, 300)
            if mouse_click:
                mouse_click = False
                counter_for_level += 1
        if rect_resume.collidepoint((x_pos_mouse, y_pos_mouse)):
            draw_text('resume', RED, DISPLAY_SIZE[0] // 2, 400)
            if mouse_click:
                PAUSE = False
                game_loop(counter_for_level, list_bodies_snake_after_pause, direction_snake_after_pause)
        if rect_save.collidepoint((x_pos_mouse, y_pos_mouse)):
            draw_text('save', RED, DISPLAY_SIZE[0] // 2, 500)
            if mouse_click:
                pass
        if rect_quit.collidepoint((x_pos_mouse, y_pos_mouse)):
            draw_text('quit', RED, DISPLAY_SIZE[0] // 2, 600)
            if mouse_click:
                sys.exit()

        mouse_click = False
        pygame.display.update()

if __name__ == '__main__':

    menu()
