import pygame
import pygame.event
from board import Cell
import utils.imports as asets 
from game import gameBoard
from pices import Pice
from game import Sides, movingPice, displayBoard, change_turn, table, BLACKPLAYER, WITEPLAYER, Gameturn
from threading import Thread
import asyncio
import varibales

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

def draw_cell(board_cell, color):
    pygame.draw.rect(screen, color, board_cell)

def draw_rect():
    font = pygame.font.Font(None, 40)
    for x in range(0, WIDTH, WIDTH_UNITY):
        for y in range(0, HEIGHT, HEIGHT_UNITY):
            board_cell = pygame.Rect(x, y, WIDTH_UNITY, HEIGHT_UNITY)
            if 0 <= x // WIDTH_UNITY < len(gameBoard.get_board) and 0 <= y // HEIGHT_UNITY < len(gameBoard.get_board[0]):
                if (x // WIDTH_UNITY) % 2 == 0:
                    color = Cell.BK_CLASSIC_COLOR() if ( y // HEIGHT_UNITY) % 2 != 0 else Cell.WT_CLASSIC_COLOR()
                else:
                    color =  Cell.WT_CLASSIC_COLOR() if ( y // HEIGHT_UNITY) % 2 != 0 else Cell.BK_CLASSIC_COLOR()
                
                draw_cell(board_cell, color) 
                
                center_x, center_y = board_cell.center
                pice = gameBoard.get_board[y // HEIGHT_UNITY][x // WIDTH_UNITY]
                if isinstance(pice, Pice):
                    img = pice.get_pice_img()
                    img = pygame.transform.scale(img, (WIDTH_UNITY, HEIGHT_UNITY))
                    screen.blit(img, (center_x - ( img.width // 2 ), center_y - (img.height // 2)))
            else:
                continue
        
font = pygame.font.Font(None, 40)


while runing:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                clicked_col = mouse_pos[0] // WIDTH_UNITY
                clicked_row = mouse_pos[1] // HEIGHT_UNITY
                if table[clicked_row][clicked_col] is not  varibales.BoardStates.VOID:
                    print(table[clicked_row][clicked_col].moves_factory((clicked_row, clicked_col), table))
            
        #draw_rect()
    
        #draw_lines()
        """screen.fill('#262522')
        text = font.render("Juega al ajedrez", True, 'white')
        button1 = pygame.Rect( (WIDTH // 2 ) - ((text.width + asets.BLIT.height + 50 )// 2 ) , 175, text.width + asets.BLIT.height + 50 , 50)
        pygame.draw.rect(screen,(255, 255, 255),button1)
        screen.blit(text,(( WIDTH // 2 )- (text.width // 2) , 50 ))
        screen.blit(asets.BLIT, ( button1.width , button1.height ))
        screen.blit(asets.BANER, (( WIDTH // 2 ) - ( asets.BANER.width // 2 ), 75 ))  

        """
        draw_rect()
        pygame.display.flip()

        

pygame.quit()