from classes.TileClass import TileClass
import pygame
from pprint import pprint
from random import choice
from fun.render_fun import get_EssanceList, get_info
from classes.EssenceClass import EssenceClass
from fun.render_fun import is_connected_subgraph


class BoardClass:
    def __init__(self, screen, size, zoom):
        self.size = size
        self.colision_mup = self.colision_mup = [[None] * self.size for _ in range(self.size)]
        self.essence_mup = [[None] * self.size for _ in range(self.size)]
        self.screen = screen
        self.left = 450
        self.top = 100
        self.block_tiles = [(0, (size - 1) // 2 + 1), ((size - 1) // 2, (size - 1)), ((size - 1), (size - 1) // 2), ((size - 1) // 2, 0)]
        self.way = set(self.block_tiles)
        self.graf = dict()
        for i in range(self.size):
            for j in range(self.size):
                self.graf[(i, j)] = set()

        self.zoom = zoom
        for x, y in self.block_tiles:
            top = ((y * zoom + (zoom * (x % 2) / 2)) * 3 ** 0.5) + self.top
            left = (x * zoom * 1.5) + self.left
            self.essence_mup[x][y] = EssenceClass(choice(choice(get_EssanceList())))
            self.essence_mup[x][y].render(screen=self.screen, left=left, top=top, zoom=zoom)

    def render(self):
        for x in range(self.size):
            for y in range(self.size):
                top =((y * self.zoom + (self.zoom * (x % 2) / 2)) * 3 ** 0.5) + self.top
                left =(x * self.zoom* 1.5) + self.left
                Tile = TileClass()
                Tile.render(screen=self.screen, left=left, top=top, zoom=self.zoom)
                self.colision_mup[x][y] = Tile.rect
                if self.essence_mup[x][y] is not None:
                    self.essence_mup[x][y].render(screen=self.screen, left=left, top=top, zoom=self.zoom)
                self.check_connected(x, y)

    def click_on_cell(self, pos):
        for x in range(self.size):
            for y in range(self.size):
                if self.colision_mup[x][y].collidepoint(pos):
                    return (x, y)

    def check_connected(self, x, y):
        t = 0
        if x % 2 == 0:
            li = ((0, -1), (1, -1), (1, 0), (0, 1), (-1, 0), (-1, -1))
        else:
            li = ((0, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0))
        for i in li:
            if (x + i[0] >= 0) and (y + i[1] >= 0) and ((x + i[0]) < self.size) and (y + i[1]) < self.size:
                if (self.essence_mup[x][y] is not None) and (self.essence_mup[x + i[0]][y + i[1]] is not None):
                    if (self.essence_mup[x + i[0]][y + i[1]].essence_type in get_info(
                        self.essence_mup[x][y].essence_type)) or (self.essence_mup[x][y].essence_type in get_info(
                        self.essence_mup[x + i[0]][y + i[1]].essence_type)):
                        pygame.draw.line(self.screen, (255, 255, 255), (self.colision_mup[x][y].center),
                                         self.colision_mup[x + i[0]][y + i[1]].center, 3)
                        self.graf[(x, y)].add((x + i[0], y + i[1]))
                        t = 1
        if t: return True
        return False

    def remove_node(self, tile):
        for i in self.graf[tile]:
            self.graf[i].remove(tile)
        self.graf[tile] = set()

