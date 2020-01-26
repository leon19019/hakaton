import pygame
from pygame.transform import scale
#from df import gamer


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(x, y, 150, 150)
        self.image = scale(pygame.image.load("images/Male.png"), (200, 280))
        self.xvel = 0
        self.yvel = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, left, right, up, down):
        if left:
            self.xvel = -20
        if right:
            self.xvel = 20
        if up:
            self.yvel = -20
        if down:
            self.yvel = 20
        if not (left or right):
            self.xvel = 0
        if not (down or up):
            self.yvel = 0
        if self.rect.x <= 50:
            self.rect.x = 50
        if self.rect.x >= 1040:
            self.rect.x = 1040
        if self.rect.y <= -20:
            self.rect.y = -20
        if self.rect.y >= 670:
            self.rect.y = 670
        if (self.rect.x <= 630 or self.rect.x >= 670) and self.rect.y <= -10:
            self.rect.x = 550
            self.rect.y = 650
            screen.blit(m_2, (1196, 278))
            screen.blit(m_3, (848, 495))
            screen.blit(m_4, (527, 130))
            screen.blit(m_5, (370, 483))
            screen.blit(m_1, (212, 192))
        if (self.rect.x <= 630 or self.rect.x >= 670) and self.rect.y >= 670:
            self.rect.x = 550
            self.rect.y = -0
            screen.blit(m_2, (1196, 278))
            screen.blit(m_3, (848, 495))
            screen.blit(m_4, (527, 130))
            screen.blit(m_5, (370, 483))
            screen.blit(m_1, (212, 192))

        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def game_over():
        screen.blit(end, (0, 0))


pygame.init()
screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("Dungeon Master")

sky = scale(pygame.image.load("images/walls.jpg"), (1280, 1024))
end = scale(pygame.image.load("images/directed_by.jpg"), (1280, 1024))
door_up = pygame.image.load("images/Door_up.png")
door_down = pygame.image.load("images/Door_down.png")
m_1 = pygame.image.load("images/m-1.png")
m_2 = pygame.image.load("images/m-2.png")
m_3 = pygame.image.load("images/m-3.png")
m_4 = pygame.image.load("images/m-4.png")
m_5 = pygame.image.load("images/m-5.png")
# создаем сыр в точке 400 400
ship = Spaceship(640, 512)


# заведем переменные, чтобы помнить, какие клавиши нажаты
left = False
right = False
down = False
up = False
lives = 6
go_door_up = False


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
    screen.blit(door_down, (-100, 0))
    # перемещаем сыр
    ship.update(left, right, up, down)
    # просим сыр нарисоваться
    ship.draw(screen)

    pygame.display.update()
