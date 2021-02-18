from sys import exit
import pygame

if __name__ == '__main__':

    pygame.init()
    win = pygame.display.set_mode((500, 500))

    pygame.display.set_caption("Tramp game")
    x = 500 // 2
    y = 430
    width = 40
    height = 40
    speed = 15
    isJump = False
    jumpCount = 10
    left = False
    right = False
    animCount = 0
    walkRight = [pygame.image.load('images//pygame_right_1.png'), pygame.image.load('images//pygame_right_2.png'),
                 pygame.image.load('images//pygame_right_3.png'), pygame.image.load('images//pygame_right_4.png'),
                 pygame.image.load('images//pygame_right_5.png'), pygame.image.load('images//pygame_right_6.png'), ]
    walkLeft = [pygame.image.load('images//pygame_left_1.png'), pygame.image.load('images//pygame_left_2.png'),
                pygame.image.load('images//pygame_left_3.png'), pygame.image.load('images//pygame_left_4.png'),
                pygame.image.load('images//pygame_left_5.png'), pygame.image.load('images//pygame_left_6.png'), ]

    playerStand = pygame.image.load('images//standing.png')
    bg = pygame.image.load('images//pygame_bg.jpg')
    clock = pygame.time.Clock()


    def drawWindow():
        global animCount
        win.blit(bg, (0, 0))
        if animCount + 1 >= 30:
            animCount = 0

        if left:
            win.blit(walkLeft[animCount // 5], (x, y))
            animCount += 1
        elif right:
            win.blit(walkRight[animCount // 5], (x, y))
            animCount += 1
        else:
            win.blit(playerStand, (x, y))

        pygame.display.update()


    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x >= speed:
            left = True
            right = False
            x -= speed
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and x < 500 - width - speed:
            x += speed
            right = True
            left = False
        else:
            right = False
            left = False
        if not isJump:
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount < 0:
                    y += jumpCount ** 2 // 2
                else:
                    y -= jumpCount ** 2 // 2
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10

        drawWindow()
