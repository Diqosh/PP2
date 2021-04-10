from pygame.locals import *
import sys
import random, time
from vars import *

pygame.init()





def render_score():
    global SCORE
    scores = font_small.render(str(SCORE), True, BLACK)
    SCREEN.blit(scores, (DISPLAY_SIZE[0] - 10 - scores.get_width(), 10))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        self.image = pygame.image.load('Materials/coin.png')
        self.surf = pygame.Surface((20, 20))
        self.rect = self.surf.get_rect(
            midbottom=(random.randint(DISPLAY_SIZE[0] // 4, DISPLAY_SIZE[0] - DISPLAY_SIZE[0] // 4), 0))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > DISPLAY_SIZE[1]):

            self.rect.bottom = 0
            self.rect.centerx = (random.randint(1,4))*100

    def draw(self):
        SCREEN.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('Materials/Enemy.png')
        self.surf = pygame.Surface((int(self.image.get_width()), int(self.image.get_height())))
        self.rect = self.surf.get_rect(
            bottomleft=(random.randint(0, 3) * 100 + 20, 0))
        self.speed = random.randint(1, 5)

    def move(self):
        self.rect.move_ip(0, self.speed * 2)
        if (self.rect.top > DISPLAY_SIZE[1]):
            self.rect.bottom = 0
            self.rect.left = random.randint(0, 3) * 100 + 20
            self.speed = random.randint(1, 5)

    def draw(self):
        SCREEN.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image_small = pygame.image.load('Materials/car2.png')
        self.image = pygame.transform.rotozoom(self.image_small, 0, 2.5)
        self.surf = pygame.Surface((int(self.image.get_width()), int(self.image.get_height())))
        self.rect = self.surf.get_rect(midbottom=(DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1]))



    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-SPEED, 0)
        if self.rect.right < DISPLAY_SIZE[0]:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(SPEED, 0)
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -SPEED)
        if self.rect.bottom < DISPLAY_SIZE[1]:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, SPEED)

    def draw(self):
        SCREEN.blit(self.image, self.rect)

player = Player()
enemy1 = Enemy()
enemy2 = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy1)


all_sprites.add(coin)

enemies = pygame.sprite.Group()
enemies.add(enemy1)

coins = pygame.sprite.Group()
coins.add(coin)






if __name__ == '__main__':
    pygame.time.delay(60)
    bg_sound.play(loops=-1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(road_image, road_image.get_rect(centerx=(DISPLAY_SIZE[0]//2)))

        for sprite in all_sprites:
            sprite.move()
            sprite.draw()



        render_score()

        if pygame.sprite.spritecollideany(player, enemies):
            pygame.mixer.stop()
            crash_sound.play()
            show_game_over()
        if pygame.sprite.spritecollideany(player, coins):
            coin_gotten_sound.play()
            SCORE += 1
            coin.rect.bottom = 0
            coin.rect.centerx = (random.randint(DISPLAY_SIZE[0] // 4, DISPLAY_SIZE[0] - DISPLAY_SIZE[0] // 4))

        pygame.display.update()

        FramePerSec.tick(FPS)
