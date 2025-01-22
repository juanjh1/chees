import pygame
import pygame.event
from board import Cell
import utils.imports as asets 


pygame.init()

WIDTH = 820
HEIGHT = 620

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Chees")

pygame.display.set_icon(asets.LOGO)

WIDTH_UNITY = WIDTH // 8
HEIGHT_UNITY = HEIGHT // 8
runing = True

def draw_lines():
    for x in range(0, WIDTH, WIDTH_UNITY):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, HEIGHT_UNITY):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (WIDTH, y), width=1)

def draw_rect():
    for x in range(0, WIDTH, WIDTH_UNITY):
        for y in range(0, HEIGHT, HEIGHT_UNITY): 
            if ( x // WIDTH_UNITY ) % 2 == 0: 
                
                if ( y // HEIGHT_UNITY ) % 2 != 0:
                    pygame.draw.rect(screen,('#EBECD0'), (x , y , WIDTH_UNITY, HEIGHT_UNITY))
                else:
                    pygame.draw.rect(screen,("#739552"), (x , y, WIDTH_UNITY, HEIGHT_UNITY))
            else:
                if  ( y // HEIGHT_UNITY )  % 2 == 0:
                    pygame.draw.rect(screen,('#EBECD0'), (x , y, WIDTH_UNITY, HEIGHT_UNITY))
                else:
                    pygame.draw.rect(screen,('#739552'), (x , y, WIDTH_UNITY, HEIGHT_UNITY))

font = pygame.font.Font(None, 40)
while runing:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    draw_rect()
    #draw_lines()
    """screen.fill('#262522')
    text = font.render("Juega al ajedrez", True, 'white')
    button1 = pygame.Rect( (WIDTH // 2 ) - ((text.width + asets.BLIT.height + 50 )// 2 ) , 175, text.width + asets.BLIT.height + 50 , 50)
    pygame.draw.rect(screen,(255, 255, 255),button1)
    screen.blit(text,(( WIDTH // 2 )- (text.width // 2) , 50 ))
    screen.blit(asets.BLIT, ( button1.width , button1.height ))
    screen.blit(asets.BANER, (( WIDTH // 2 ) - ( asets.BANER.width // 2 ), 75 ))  

    """
    pygame.display.flip()


pygame.quit()