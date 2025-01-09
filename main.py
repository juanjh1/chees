import pygame
import pygame.event
from board import Cell


pygame.init()

WIDTH = 720
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Chees")
logo = pygame.image.load("./img/util/tower.png")
pygame.display.set_icon(logo)

runing = True



while runing:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    

pygame.quit()