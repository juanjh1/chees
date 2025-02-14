from varibales import BoardStates , Sides
import pygame

class Board():
    
    def __init__(self):
        self.space = [[ BoardStates.VOID for j in range(8) ] for i in range(8)]
        self.turn = Sides.WHITE
        
    @property
    def get_board(self):
        return self.space
    



class Cell():
    bk_cell_classic = '#EBECD0'
    wt_cell_classic = '#739552'
    moves_circle ='#D3D3D380'
    
    def __init__(self , side):

        self.surf = pygame.Surface
        if side == Sides.WHITE():
            self.surf.fill((220, 20, 60))
        if side == Sides.BLACK:
            self.surf.fill((0, 0, 0))
    @staticmethod
    def BK_CLASSIC_COLOR():
        return  Cell.bk_cell_classic 
    @staticmethod
    def WT_CLASSIC_COLOR():
        return  Cell.wt_cell_classic
    @staticmethod
    def HG_COLOR():
        return  Cell.moves_circle
    
