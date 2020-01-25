import pygame
import random
import os

#class сыр:
    #pass

no_image = pygame.image.load("/home/asp-159/Загрузки/Telegram Desktop/photo_2020-01-25_13-09-10.jpg")
x_coord = 0
y_coord = 0
no_position = [x_coord,y_coord]

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
clock = pygame.time.Clock()
background_image = pygame.image.load('/home/asp-159/hakaton/images/photo_2020-01-25_13-00-32.jpg')
class gamer:
    pass

    

while True:
    screen.blit(background_image, (0, 0))
    screen.blit(no_image, (250, 500))
    pygame.display.update()
    clock.tick(60)
while not done:
   for event in pygame == pygame.Quit:
       done = True
#class wall:
    #x_coordinats = 0
    #y_coordinats = 0

