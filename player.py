from varibales import Sides, BoardStates
from pices import Pown, Rook, Knight, Bishop, Queen,King

class Player():
    def __init__(self, side):
        self.side = side
        self.historial_moves = []

    def fill_table(self, table):
        if self.side == Sides.WHITE:

            for pice in range(len(table[1])):
                table[1][pice] =  Pown(self.side)
            table[0][0]  = Rook(self.side)
            table[0][7]  = Rook(self.side)
            table[0][1]  = Knight(self.side)
            table[0][6]  = Knight(self.side)
            table[0][2]  = Bishop(self.side)
            table[0][5]  = Bishop(self.side)
            table[0][3]  = Queen(self.side)
            table[0][4]  = King(self.side)



        if self.side == Sides.BLACK:
            for pice in range(len(table[6])):
                table[6][pice] =  Pown(self.side)
                
            table[7][0]  = Rook(self.side)
            table[7][7]  = Rook(self.side)
            table[7][1]  = Knight(self.side)
            table[7][6]  = Knight(self.side)
            table[7][2]  = Bishop(self.side)
            table[7][5]  = Bishop(self.side)
            table[7][3]  = Queen(self.side)
            table[7][4]  = King(self.side)
        
    def move_pice(self, _from , to, table, side ):
        if to[0] <=  7 and  to[1] <= 7 :
            print("here 0")
            print(table[to[0]][to[1]] , to[0],to[1])
            if table[to[0]][to[1]] ==  BoardStates.VOID and table[_from[0]][_from[1]].side == side:
                print("here 1")
                if table[_from[0]][_from[1]].move(_from, to):
                    print("here 2")
                    table[to[0]][to[1]] = table[_from[0]][_from[1]] 
                    table[_from[0]][_from[1]] = BoardStates.VOID
                    self.historial_moves.append(((_from[0],_from[1]), (to[0],to[1])))
                    
                    return True

        return False           


        
        

