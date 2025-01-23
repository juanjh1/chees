import pygame
import os
ruta_base = os.path.dirname(__file__)


absolute_path = os.path.abspath(os.path.join(ruta_base, '..', 'img', 'util'))

def path_eng(absolute_path, filename):
    return os.path.abspath(os.path.join(absolute_path, filename))


LOGO = pygame.image.load(path_eng(absolute_path,"tower.png"))


BANER = pygame.image.load(path_eng(absolute_path,"baner.svg"))

BLIT =  pygame.image.load(path_eng(absolute_path,"blits.svg"))

PAWN_W =  pygame.image.load(path_eng(absolute_path,"pawn_w.png"))

PAWN_B =  pygame.image.load(path_eng(absolute_path,"pawn_b.png"))

BISHOP_W =  pygame.image.load(path_eng(absolute_path,"bishop_w.png"))

BISHOP_B =  pygame.image.load(path_eng(absolute_path,"bishop_b.png"))

KNIGHT_B =  pygame.image.load(path_eng(absolute_path,"knight_b.png"))

KNIGHT_W =  pygame.image.load(path_eng(absolute_path,"knight_w.png"))

ROOK_W =  pygame.image.load(path_eng(absolute_path,"rook_w.png"))

ROOK_B =  pygame.image.load(path_eng(absolute_path,"rook_b.png"))

QUEEN_B =  pygame.image.load(path_eng(absolute_path,"queen_b.png"))

QUEEN_W =  pygame.image.load(path_eng(absolute_path,"queen_w.png"))

KING_B =  pygame.image.load(path_eng(absolute_path,"king_b.png"))

KING_W =  pygame.image.load(path_eng(absolute_path,"king_w.png"))