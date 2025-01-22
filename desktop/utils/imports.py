import pygame
import os
ruta_base = os.path.dirname(__file__)


absolute_path = os.path.abspath(os.path.join(ruta_base, '..', 'img', 'util'))

def path_eng(absolute_path, filename):
    return os.path.abspath(os.path.join(absolute_path, filename))


LOGO = pygame.image.load(path_eng(absolute_path,"tower.png"))


BANER = pygame.image.load(path_eng(absolute_path,"baner.svg"))

BLIT =  pygame.image.load(path_eng(absolute_path,"blits.svg"))

