import pygame
from pygame.transform import scale


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(x, y, 150, 150)
        self.image = scale(pygame.image.load("images/cheese_v2.png"), (150, 150))
        self.xvel = 0
        self.yvel = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, left, right, up, down):
        if left:
            self.xvel = -15
        if right:
            self.xvel = 15
        if up:
            self.yvel = -15
        if down:
            self.yvel = 15
        #if shoot_left:
            #pass
        #if shoot_right:
            #pass
        #if shoot_up:
            #pass
        #if shoot_down:
            # pass
        if not (left or right):
            self.xvel = 0
        if not (down or up):
            self.yvel = 0
        if self.rect.x <= 100:
            self.rect.x = 100
        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y <= 40:
            self.rect.y = 40
        if self.rect.y >= 780:
            self.rect.y = 780
        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def game_over():
        screen.blit(end, (0, 0))


pygame.init()
screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("Gamer")

sky = scale(pygame.image.load("images/walls.jpg"), (1280, 1024))
end = scale(pygame.image.load("images/directed_by.jpg"), (1280, 1024))
door_up = pygame.image.load("images/Door(up, down).png")
# создаем сыр в точке 400 400
ship = Spaceship(640, 512)


# заведем переменные, чтобы помнить, какие клавиши нажаты
left = False
right = False
down = False
up = False
lives = 6


while True:
    for e in pygame.event.get():
        # если нажата клавиша - меняем переменную
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            left = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            right = True

        # если отпущена клавиша - меняем переменную
        if e.type == pygame.KEYUP and e.key == pygame.K_a:
            left = False
        if e.type == pygame.KEYUP and e.key == pygame.K_d:
            right = False

        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            up = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            down = True

        # если отпущена клавиша - меняем переменную
        if e.type == pygame.KEYUP and e.key == pygame.K_w:
            up = False
        if e.type == pygame.KEYUP and e.key == pygame.K_s:
            down = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_4:
            pass
        if lives == 0:
            game_over()
        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")
    # рисуем фон
    screen.blit(sky, (0, 0))
    screen.blit(door_up, (100, 0))
    # перемещаем сыр
    ship.update(left, right, up, down)
    # просим сыр нарисоваться
    ship.draw(screen)

    pygame.display.update()
