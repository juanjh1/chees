from varibales import Sides
import utils.imports  as images 

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
            return images.ROOK_W
        return images.ROOK_B


class Rook (Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    def get_pice_img (self):
        if self.side == Sides.WHITE:
            return images.ROOK_W
        return images.ROOK_B
    





class Knight (Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    def get_pice_img (self):
        if self.side == Sides.WHITE:
            return images.KNIGHT_W
        return images.KNIGHT_B
    



class Bishop(Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    def get_pice_img (self):
        if self.side == Sides.WHITE:
            return images.BISHOP_W
        return images.BISHOP_B


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
    
    def move(self, _from , to):

        if(self.side == Sides.WHITE):
            if(not self.moved ):
                self.move = True
                return True if( _from[0]  == ( to[0] - 2 )  or   _from[0]  == ( to[0] - 1 ) ) and (_from[1] == to[1])  else False
            elif(self.move): 
                return True if  _from[0]  == ( to[0]- 1 )  and (_from[1] == to[1]) else False
        
        if(self.side == Sides.BLACK):
            if(not self.moved ):
                self.move = True
                return True if _from[0]  == ( to[0] + 2 )  or   _from[0]  == ( to[0] + 1 ) and (_from[1] == to[1])  else False 
            elif(self.move): 
                return True if _from[0]  == ( to[0] + 1 ) and (_from[1] == to[1])  else False