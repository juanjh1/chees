from board import BoardStates

def  generateMoventX( iter , callback , _from,table , object ):
            for  x in iter:
                if  table[x][_from] is BoardStates.VOID:
                    callback((x, _from))
                else: 
                    if table[_from][x].side != object.side:
                        callback((x, _from))
                    else:
                        break
                
def  generateMoventY( iter , callback , _from, table, object ):
            for  y in iter:
                if table[_from][y] is BoardStates.VOID:
                    callback((_from, y ))
                else: 
                    if table[_from][y].side != object.side:
                        callback((_from , y))
                    else:
                        break