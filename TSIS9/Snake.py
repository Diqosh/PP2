import pygame, random
from pygame.math import Vector2

pygame.init()
score = 0
eat_sound = pygame.mixer.Sound('Materials/eat.wav')
font = pygame.font.SysFont('roboto', 60)
font_small = pygame.font.SysFont('roboto', 20)
bg_block_image = pygame.image.load('Materials/bg.png')
wall_block_image = pygame.image.load('Materials/wall.png')
apple_image = pygame.image.load('Materials/apple.png')
table_image = pygame.image.load('Materials/table.png')
table_image.set_alpha(200)
sizeOfCeil = 40
numOfCeil = 20
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((sizeOfCeil * numOfCeil, sizeOfCeil * numOfCeil))
pygame.display.set_caption('SNAKE')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


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
        SCREEN.blit(table_image,table_image.get_rect(topright=(numOfCeil * sizeOfCeil, 0)))
        score_image = font_small.render(f'Score: {score}',True, BLACK)
        SCREEN.blit(score_image,score_image.get_rect(topleft=((numOfCeil-3) * sizeOfCeil, 0)))

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
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
        # if not 1 <= self.body[-1].x < numOfCeil - 1 or  not 1 <= self.body[-1].y < numOfCeil - 1:
        #     self.game_over()
        # for block in self.body[:-1]:
        #     if block == self.body[-1]:
        #         self.game_over()
        pass

    def game_over(self):
        pygame.quit()


class Friut(pygame.sprite.Sprite):
    def __init__(self):
        super(Friut, self).__init__()
        self.x = random.randint(1, numOfCeil - 2)
        self.y = random.randint(1, numOfCeil - 2)
        self.posFruit = Vector2(self.x, self.y)

    def draw(self):
        SCREEN.blit(apple_image, (self.x * sizeOfCeil, self.y * sizeOfCeil))


# every 100 ms rum snake.move
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 120)

fruit = Friut()
snake = Snake()
bg = Bacgraund()

game_obj = []
game_obj.extend([bg, fruit, snake])
if __name__ == '__main__':
    while True:

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

        SCREEN.fill(WHITE)

        for obj in game_obj:
            obj.draw()

        pygame.display.flip()
        clock.tick(60)
