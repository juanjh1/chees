import pygame
import pygame.event
from board import Cell


pygame.init()

WIDTH = 700
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Chees")
logo = pygame.image.load("./img/util/tower.png")
pygame.display.set_icon(logo)

WIDTH_UNITY = WIDTH // 8
HEIGHT_UNITY = HEIGHT // 8
runing = True

def draw_lines():
    for x in range(0, WIDTH, WIDTH // 8):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, HEIGHT // 8):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (WIDTH, y), width=1)

def draw_rect():
    for x in range(0, WIDTH, WIDTH // 8):
        for y in range(0, HEIGHT, HEIGHT // 8):
            
            if ( x // WIDTH_UNITY ) % 2 == 0: 
                if ( y // HEIGHT_UNITY ) % 2 != 0:
                    pygame.draw.rect(screen,(255, 255, 255),(x , y , WIDTH // 8, HEIGHT // 8))
                else:
                    pygame.draw.rect(screen,(170, 215, 200),(x , y, WIDTH // 8, HEIGHT // 8))
                    
            else:
                if  ( y // HEIGHT_UNITY )  % 2 == 0:
                    pygame.draw.rect(screen,(255, 255, 255),(x , y, WIDTH // 8, HEIGHT // 8))
                    
                else:
                    pygame.draw.rect(screen,(170, 215, 200), (x , y, WIDTH // 8, HEIGHT // 8))


while runing:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False

    draw_rect()
    draw_lines()
    pygame.display.flip() 
    

pygame.quit()