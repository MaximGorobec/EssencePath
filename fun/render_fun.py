from math import cos, sin
import pygame
import os

from random import randint

def draw_ngon(screen, radius, position):
    pi2 = 2 * 3.14
    n = 6
    color = (255, 255, 255)
    # color = (randint(0, 255), randint(0, 255), randint(0, 255))
    return pygame.draw.lines(screen, color, True,
          [(cos(i / n * pi2) * radius + position[0],
            sin(i / n * pi2) * radius + position[1]) for i in range(0, n)])

def get_EssanceList():
    # EL = ["terra", "aer", "aqua", "ignis", "ordo", "perditio", "gelum", "motus", ""]
    EL =[]
    for entry in os.scandir("images/essentials"):
        if entry.is_file():
            EL.append(entry.name[:-4])
    n = 4
    return [EL[row:row + 4] for row in range(0, len(EL), n)]