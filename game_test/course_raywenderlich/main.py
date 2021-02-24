import pygame
from math import atan2, cos , sin


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
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append(
                [atan2(position[1] - (playerpos1[1]), position[0] - (playerpos1[0])), playerpos1[0],
                 playerpos1[1]])
angle = 0

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Rabbit Game")
    width, height = 640, 480
    positionPlayer = [100, 100]
    screen = pygame.display.set_mode((width, height))
    movement = 10
    acc = [0, 0]
    arrows = []

    # images

    player = pygame.image.load('resources/images/dude.png')
    grass = pygame.image.load('resources/images/grass.png')
    castle = pygame.image.load('resources/images/castle.png')
    arrow = pygame.image.load('resources/images/bullet.png')

    while 1:
        pygame.time.Clock().tick(10)

        draw_bg()
        draw_castles()
        quiting()
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w]:
            positionPlayer[1] -= movement
        elif pressed[pygame.K_a]:
            positionPlayer[0] -= movement
        elif pressed[pygame.K_s]:
            positionPlayer[1] += movement
        elif pressed[pygame.K_d]:
            positionPlayer[0] += movement

        position = pygame.mouse.get_pos()
        angle = atan2(position[1] - (positionPlayer[1] + 23), position[0] - (positionPlayer[0] + 32)) * 57.32
        playerrot = pygame.transform.rotate(player, 360 - angle)
        playerpos1 = (positionPlayer[0] - playerrot.get_width() // 2, positionPlayer[1] - playerrot.get_height() // 2)
        print("mouse" , position)
        for event in pygame.event.get():
            if event.type is pygame.MOUSEBUTTONDOWN:
                posMouse = pygame.mouse.get_pos()
                acc[1] += 1
                arrows.append([atan2(posMouse[1] - (positionPlayer[1] + 23), posMouse[0] - (positionPlayer[0] + 32)), positionPlayer[0] + 32, positionPlayer[1] + 23])
                print(positionPlayer, positionPlayer)
        for bullet in arrows:
            index = 0
            velx = cos(bullet[0])*movement
            vely = sin(bullet[0])*movement
            bullet[1] += velx
            bullet[2] += vely
            if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
                arrows.pop(index)
            index += 1
            for projectile in arrows:
                arrowrot = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
                screen.blit(arrowrot, (projectile[1], projectile[2]))

        screen.blit(playerrot, playerpos1)


        pygame.display.update()
