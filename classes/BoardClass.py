from classes.TileClass import TileClass
from random import choice
from fun.render_fun import get_EssanceList
from classes.EssenceClass import EssenceClass

class BoardClass:
    def __init__(self, screen, size):
        self.size = size
        self.colision_mup = self.colision_mup = [[None] * self.size for _ in range(self.size)]
        self.essence_mup = [[None] * self.size for _ in range(self.size)]
        self.screen = screen
        self.left = 450
        self.top = 100
        self.block_tiles = [(0, 2), (3, 5), (5, 2), (2, 0)]
        for i, j in self.block_tiles:
            self.essence_mup[i][j] = EssenceClass(choice(choice(get_EssanceList())))


    def render(self, zoom=50):
        for x in range(self.size):
            for y in range(self.size):
                top =((y * zoom + (zoom * (x % 2) / 2)) * 3 ** 0.5) + self.top
                left =(x * zoom* 1.5) + self.left
                Tile = TileClass()
                Tile.render(screen=self.screen, left=left, top=top, zoom=zoom)
                # draw_ngon(self.screen, zoom, Tile.rect.center)
                self.colision_mup[x][y] = Tile.rect
                if self.essence_mup[x][y] is not None:
                    self.essence_mup[x][y].render(screen=self.screen, left=left, top=top, zoom=zoom)

    def click_on_cell(self, pos):
        for x in range(self.size):
            for y in range(self.size):
                if self.colision_mup[x][y].collidepoint(pos):
                    return (x, y)