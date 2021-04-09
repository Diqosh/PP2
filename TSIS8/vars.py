import pygame, time, sys
pygame.init()
def show_game_over():
    for sprite in all_sprites:
        sprite.kill()
    fail_sound.play()
    SCREEN.fill(RED)
    SCREEN.blit(game_over, game_over.get_rect(center=(DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2)))
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    sys.exit()



SCORE = 0
SPEED = 5
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
FPS = 60
DISPLAY_SIZE = (400, 600)
SCREEN = pygame.display.set_mode(DISPLAY_SIZE)

bg_sound = pygame.mixer.Sound('Materials/background.wav')
crash_sound = pygame.mixer.Sound('Materials/crash.wav')
road_image = pygame.image.load('Materials/bg.png')
fail_sound = pygame.mixer.Sound('Materials/fail.wav')
coin_gotten_sound = pygame.mixer.Sound('Materials/coin_gotten.wav')

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
FramePerSec = pygame.time.Clock()
font = pygame.font.SysFont('roboto', 60)
font_small = pygame.font.SysFont('roboto', 20)
game_over = font.render('Game Over', True, BLACK)
listSpritesOfCoin = []