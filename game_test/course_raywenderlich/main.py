import pygame
import math


def draw_bg():
    for x in range(width // grass.get_width() + 1):
        for y in range(height // grass.get_height() + 1):
            screen.blit(grass, (x * grass.get_width(), y * grass.get_height()))


def draw_castles():
    for y in range(height // castle.get_height()):
        screen.blit(castle, (0, y * castle.get_height() + 30))


def quiting():
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            pygame.quit()
            exit(0)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Rabbit Game")
    width, height = 640, 480
    x, y = 100, 100
    screen = pygame.display.set_mode((width, height))
    movement = 10

    # images

    player = pygame.image.load('resources/images/dude.png')
    grass = pygame.image.load('resources/images/grass.png')
    castle = pygame.image.load('resources/images/castle.png')

    while 1:
        pygame.time.Clock().tick(30)

        draw_bg()
        draw_castles()
        quiting()
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w]:
            y -= movement
        elif pressed[pygame.K_a]:
            x -= movement
        elif pressed[pygame.K_s]:
            y += movement
        elif pressed[pygame.K_d]:
            x += movement
        #### this part i didnt understand yet
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1] - (y + 32), position[0] - (x + 26))
        playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
        playerpos1 = (x - playerrot.get_rect().width / 2, y - playerrot.get_rect().height / 2)
        #####
        screen.blit(playerrot, playerpos1)


        pygame.display.update()



