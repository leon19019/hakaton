import pygame
from pygame.transform import scale
#from df import gamer
import time
import random

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
            number = 1
            for i in range(number):
                num = random.randint(1,5)
                m = pygame.image.load('images/m-'+str(num)+'.png')
                x = random.randint(1,500)
                y = random.randint(1,500)
                screen.blit(m, (x,y))
        if (self.rect.x <= 630 or self.rect.x >= 670) and self.rect.y >= 670:
            self.rect.x = 550
            self.rect.y = -0
            number = 1
            for i in range(number):
                num = random.randint(1,5)
                m = pygame.image.load('images/m-'+str(num)+'.png')
                x = random.randint(1,500)
                y = random.randint(1,500)
                screen.blit(m, (x,y))
        
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
ship = Spaceship(640, 512)


left = False
right = False
down = False
up = False
lives = 6
go_door_up = False


while True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            left = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            right = True

        if e.type == pygame.KEYUP and e.key == pygame.K_a:
            left = False
        if e.type == pygame.KEYUP and e.key == pygame.K_d:
            right = False

        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            up = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            down = True

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
    screen.blit(sky, (0, 0))
    screen.blit(door_up, (100, 0))
    screen.blit(door_down, (-100, 0))
    ship.update(left, right, up, down)
    ship.draw(screen)

    pygame.display.update()
