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
    def __init__(self , side):
        self.surf = pygame.Surface
        if side == Sides.WHITE():
            self.surf.fill((220, 20, 60))
        if side == Sides.BLACK:
            self.surf.fill((0, 0, 0))