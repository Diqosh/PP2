import pygame
from math import atan2

widthSurface = 640
heightSurface = 480
keys = [False, False, False, False]
playerpos = [100, 100]
vel = 5

# images
player = pygame.image.load('resources/images/dude.png')
grass = pygame.image.load('resources/images/grass.png')
castle = pygame.image.load('resources/images/castle.png')


def blitGrassAndCastle():
    for x in range(widthSurface // grass.get_width() + 1):
        for y in range(heightSurface // grass.get_height() + 1):
            surface.blit(grass, (x * grass.get_width(), y * grass.get_height()))
    surface.blit(castle, (0, 30))
    surface.blit(castle, (0, 135))
    surface.blit(castle, (0, 240))
    surface.blit(castle, (0, 345))


def movePlayer():
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and playerpos[0] > 0:
        playerpos[0] -= vel

    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and playerpos[0] + player.get_width() < widthSurface:
        playerpos[0] += vel

    if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and playerpos[1] > 0:
        playerpos[1] -= vel

    if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and playerpos[1] + player.get_height() < heightSurface:
        playerpos[1] += vel


if __name__ == '__main__':

    pygame.init()

    surface = pygame.display.set_mode((widthSurface, heightSurface))
    while True:
        pygame.time.delay(30)
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        movePlayer()

        positionOfMouse = pygame.mouse.get_pos()
        angle = atan2(positionOfMouse[1] - (playerpos[1] + player.get_rect().height//2), positionOfMouse[0] - (playerpos[0] + player.get_rect().width//2))

        playerRotated = pygame.transform.rotate(player, -angle * 57.29)

        rotatedPlayerPos = (playerpos[0]-playerRotated.get_rect().width/2, playerpos[1]-playerRotated.get_rect().height/2)
        
        blitGrassAndCastle()

        surface.blit(playerRotated, rotatedPlayerPos)

        pygame.display.update()
