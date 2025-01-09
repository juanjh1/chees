from varibales import Sides

class Pice():
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return  self.__class__.__name__ + self.side.name
    def __repr__(self):
        return self.__class__.__name__
    def move(self, _from , to):
        pass






class King(Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()






class Queen (Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()


class Rook (Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    





class Knight (Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    



class Bishop(Pice):
    def __init__(self, side):
        super().__init__(side)
    def __repr__(self):
        return super().__repr__()
    


class Pown (Pice):
    def __init__(self, side):
        super().__init__(side)
        self.moved = False

    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
    
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