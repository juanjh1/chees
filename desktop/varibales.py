from enum import Enum, auto


class BoardStates(Enum):
    VOID = auto()
    HIGTHLIGTH = auto()
    


class Sides(Enum):
    BLACK = auto()
    WHITE = auto()



class TablesStates(Enum):
    HIGTHLIGTH = auto()
    DEFAULT = auto()