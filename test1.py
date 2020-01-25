import pygame
import random
import os

#class сыр:
    #pass

p1Paddle = pygame.image.load("/home/asp-159/Загрузки/Telegram Desktop/photo_2020-01-25_13-09-10.jpg")
x_velocity = 0
y_coord = 0
no_position = [x_velocity,y_coord]

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
clock = pygame.time.Clock()
background_image = pygame.image.load('/home/asp-159/hakaton/images/photo_2020-01-25_13-00-32.jpg')
class gamer:
    pass

    

while True:
    screen.blit(background_image, (0, 0))
    screen.blit(p1Paddle, (250, 500))
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p1Paddle.x_velocity = -10
            elif event.key == pygame.K_RIGHT:
                p1Paddle.x_velocity = 10
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                # if either the left or right arrow keys are released
                p1Paddle.x_velocity = 0
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #p1Paddle.x_distance += p1Paddle.x_velocity
    # other stuff here
    # drawing code here
    pygame.display.update()

    pygame.display.update()
while not done:
   for event in pygame == pygame.Quit:
       done = True
#class wall:
    #x_velocityinats = 0
    #y_coordinats = 0

