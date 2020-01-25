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
background_image = pygame.image.load('/home/asp-159/hakaton/images/photo_2020-01-25_14-17-55.jpg')
class gamer:
    pass

    

while True:
    screen.blit(background_image, (0, 0))
    screen.blit(p1Paddle, (250, 500))
    pygame.display.update()
    clock.tick(60)

    pygame.display.update()
while not done:
   for event in pygame == pygame.Quit:
       done = True
#class wall:
    #x_velocityinats = 0
    #y_coordinats = 0

