import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
clock = pygame.time.Clock()
background_image = pygame.image.load('/home/asp-159/hakaton/images/photo_2020-01-25_11-53-51.jpg')
class gamer:
    pass
    

while True:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)
class wall:
    x_coordinats = 0
    y_coordinats = 0

