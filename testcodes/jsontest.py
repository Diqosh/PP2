import pygame, sys




if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    font = pygame.font.SysFont("arial", 30)

    text = font.render("Hello, World", True, (0, 128, 0))
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2) )
        print(pygame.mouse.get_pos() ,(320 - text.get_width() // 2, 240 - text.get_height() // 2) )

        pygame.display.flip()
