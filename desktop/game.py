from board import Board
from varibales import Sides,BoardStates
from pices import Pown, King, Knight, Bishop, Queen, Rook
from player import Player
import re

##
"""
Game functions
"""
##
def change_turn(turn):
    """
    Return side of new turn
    """
    return Sides.BLACK if turn == Sides.WHITE else Sides.WHITE

def createPlayer(side, table):
    """
    Create Player and fill the player pices
    """
    player = Player(side)
    player.fill_table(table)
    return player


def valuateInput(string):
    regex = r"^\((\d),(\d)\)"
    to_match = re.findall(regex,string)
    return  to_match[0]
        




def displayBoard(table):
    format_table= ""
    for line in table:
        table_line = "|"
        for block in line:
            if block == BoardStates.VOID:
                table_line += "   |"
            if isinstance(block, Pown):
                table_line += " P |"
            if isinstance(block, Queen):
                table_line += " Q |"
            if isinstance(block, King):
                table_line += " K |"
            if isinstance(block, Knight):
                table_line += " H |"
            if isinstance(block, Rook):
                table_line += " R |"
            if isinstance(block, Bishop ):
                table_line += " B |"
        format_table += table_line+"\n"
        format_table += len(table_line)*"_"+"\n"
    return format_table



def movingPice(player, gameturn):
        _from = input("Side from: ")
        to = input("Side to: ")
        to_match = valuateInput(to)
        
        to_from = valuateInput(_from)
        
        return player.move_pice(
            (int(to_from[0]), 
            int(to_from[1])),

            (int(to_match[0]),
            int(to_match[1])),

            table,
            gameturn
            )



gameBoard = Board()
table = gameBoard.space 
Gameturn = gameBoard.turn

#CONST
WITEPLAYER = createPlayer(Sides.WHITE, table)
BLACKPLAYER = createPlayer(Sides.BLACK, table)


while True:
    print(displayBoard(table))

    if Gameturn == Sides.WHITE:
        #Muving white pice 
        print("white turn")
        movingPice(WITEPLAYER, Gameturn)
        print(displayBoard(table))
    if Gameturn == Sides.BLACK:
        print("Black turn")
        movingPice(BLACKPLAYER, Gameturn)
        print(displayBoard(table)) 
    Gameturn = change_turn(Gameturn)

