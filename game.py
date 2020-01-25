import pygame
from pygame.transform import scale

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(x, y, 150, 150)
        self.image = scale(pygame.image.load("/home/asp-159/hakaton/images/photo_2020-01-25_13-40-53.jpg"), (150, 150))
        self.xvel = 0
        self.yvel = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def update(self, left, right, up, down):
        if left:
            self.xvel = -12

        if right:
            self.xvel = 12
        if up:
            self.yvel = -12
        if down:
            self.yvel = 12
        if not (left or right):
            self.xvel = 0
        if not (down or up):
            self.yvel = 0
        self.rect.x += self.xvel
        self.rect.y += self.yvel
    def game_over():
        screen.blit(end, (0, 0)) 

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("Asteroids")

sky = scale(pygame.image.load("/home/asp-159/hakaton/images/photo_2020-01-25_14-17-55.jpg"), (1280, 1024))
end = scale(pygame.image.load("/home/asp-159/Загрузки/Telegram Desktop/photo_2020-01-25_15-38-15.jpg"), (1280, 1024))
# создаем сыр в точке 400 400
ship = Spaceship(400, 400)


# заведем переменные, чтобы помнить, какие клавиши нажаты
left = False
right = False
down = False
up = False


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

        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")
    # рисуем фон
    screen.blit(sky, (0, 0))

    # перемещаем сыр
    ship.update(left, right, up, down)
    # просим сыр нарисоваться
    ship.draw(screen)

    pygame.display.update()