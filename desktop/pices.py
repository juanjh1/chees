from varibales import Sides
import utils.imports  as images 
from varibales import BoardStates
from utils.util_functions import generateMoventX, generateMoventY



class Pice():
    
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return  self.__class__.__name__ + self.side.name
    def __repr__(self):
        return self.__class__.__name__
    def move(self, _from , to):
        pass
    def get_pice_img (self):
        pass 
    def moves_factory(self):
        pass




class King(Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    def get_pice_img (self):
        if self.side == Sides.WHITE:
            return images.KING_W
        return images.KING_B
    




class Queen (Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    def get_pice_img (self):
        if self.side == Sides.WHITE:
            return images.QUEEN_W
        return images.QUEEN_B
    
    def moves_factory(self, _from , table):
        moves = []
        x_start, y_start = _from  #(3,3)
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)] 
        blocked = False
        generateMoventX(range(_from[0], len(table[0])), moves.append, _from[1], table, self)
        generateMoventX(range(_from[0], 0 , -1 ), moves.append, _from[1], table, self)
        generateMoventY(range(_from[1], len(table)), moves.append ,_from[0] , table , self)
        generateMoventY(range(_from[1], 0 , -1), moves.append ,_from[0] , table , self )
        for dx, dy in directions:
            step = 0
            while not blocked:
                step += 1
                new_x = x_start + dx * step
                new_y = y_start + dy * step
                if not (0 <= new_x < 8 and 0 <= new_y < 8):
                    break
                if table[new_x][new_y] == BoardStates.VOID:
                        moves.append((new_x, new_y))
                else: 
                    if table[new_x][new_y].side != self.side:
                        moves.append((new_x, new_y))
                    else:
                        blocked = True  
        return moves
    
    def move(self, _from , to, table):
        moves = self.moves_factory( _from , to, table)                
        return to in moves


class Rook (Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    def get_pice_img (self):
        if self.side == Sides.WHITE:
            return images.ROOK_W
        return images.ROOK_B
    def moves_factory(self, _from ,  table):
        moves = []

        generateMoventX(range(_from[0], len(table[0])), moves.append, _from[1], table, self)
        generateMoventX(range(_from[0], 0 , -1 ), moves.append, _from[1], table, self)
        generateMoventY(range(_from[1], len(table)), moves.append ,_from[0], table, self)
        generateMoventY(range(_from[1], 0 , -1), moves.append ,_from[0] , table, self)

        print(moves)
        return moves 
    def move(self, _from , to, table):
        moves = self.moves_factory( _from , to, table)   
        return to in moves



class Knight (Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    def get_pice_img (self):
        if self.side == Sides.WHITE:
            return images.KNIGHT_W
        return images.KNIGHT_B
    def moves_factory(self, _from ,  table):
        pass



class Bishop(Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    def get_pice_img (self):
        if self.side == Sides.WHITE:
            return images.BISHOP_W
        return images.BISHOP_B
    def moves_factory(self, _from ,  table):
        moves = []  
        x_start, y_start = _from  
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)] 
        blocked = False
        for dx, dy in directions:
            step = 0
            while not blocked:
                step += 1
                new_x = x_start + dx * step
                new_y = y_start + dy * step
                if not (0 <= new_x < 8 and 0 <= new_y < 8):
                    break
                if table[new_x][new_y] == BoardStates.VOID:
                        moves.append((new_x, new_y))
                else: 
                    if table[new_x][new_y].side != self.side:
                        moves.append((new_x, new_y))
                    else:
                        blocked = True
        return moves                 
        
    def move(self, _from , to, table):
        
        moves = self.moves_factory( _from , to, table)  
        return to in moves

class Pown (Pice):

    def __init__(self, side):
        super().__init__(side)
        self.moved = False

    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    
    def get_pice_img (self):
        if self.side == Sides.WHITE:
            return images.PAWN_W
        return images.PAWN_B
    def moves_factory(self, _from, table):
        if(self.side == Sides.WHITE):
            if(not self.moved):
                return [(_from[0] +  1 , _from[1] ), (_from[0]+  2, _from[1] )]
            else: 
                return [(_from[0] +  1 , _from[1] )]

        if(self.side == Sides.BLACK):
            if(not self.moved):
                return [(_from[0] -  1 , _from[1]), (_from[0] -  2 , _from[1])]
            else: 
                return [(_from[0]-  1, _from[1]    )]

        return super().moves_factory()
    
    def move(self, _from , to, table = None):

        if(self.side == Sides.WHITE):
            if(not self.moved):
                self.moved = True
                return True if( _from[0]  == ( to[0] - 2 )  or   _from[0]  == ( to[0] - 1 ) ) and (_from[1] == to[1])  else False
            elif(self.moved): 
                return True if  _from[0]  == ( to[0]- 1 )  and (_from[1] == to[1]) else False
        
        if(self.side == Sides.BLACK):
            if(not self.moved ):
                self.moved = True
                return True if _from[0]  == ( to[0] + 2 )  or  _from[0]  == ( to[0] + 1 ) and (_from[1] == to[1])  else False 
            elif(self.moved): 
                return True if _from[0]  == ( to[0] + 1 ) and (_from[1] == to[1])  else False
            


if __name__ == "__main__":
    table = [
    [BoardStates.VOID for _ in range(8)] for _ in range(8)
    ]

    # Posición inicial del alfil
    bishop = Bishop(side="white")
    _from = (3, 3)  # Posición central
    
    
    # ----------------------------------------------
    # Prueba 1: Movimiento diagonal ↘️ válido (4,4)
    # ----------------------------------------------
    to = (4, 4)
    #print(bishop.move(_from, to, table)) 

    # ----------------------------------------------
    # Prueba 2: Movimiento diagonal ↖️ válido (2,2)
    # ----------------------------------------------
    to = (2, 2)
    #print(bishop.move(_from, to, table))  
    # ----------------------------------------------
    # Prueba 3: Movimiento diagonal ↙️ válido (4,2)
    # ----------------------------------------------
    to = (4, 2)
    #(bishop.move(_from, to, table)) 

    # ----------------------------------------------
    # Prueba 4: Movimiento NO diagonal (3,5) → Inválido
    # ----------------------------------------------
    to = (3, 5)
    #print(bishop.move(_from, to, table))  

    # ----------------------------------------------
    # Prueba 5: Movimiento fuera del tablero (8,8)
    # ----------------------------------------------
    to = (8, 8)
    #print(bishop.move(_from, to, table))  

    # Posición inicial de la torre
    rook = Rook(side="white")
    _from = (0, 1)  # Posición central
    rook.moves_factory(_from,table ) 
