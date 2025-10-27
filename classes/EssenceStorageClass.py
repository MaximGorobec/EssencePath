from math import trunc

from classes.EssenceClass import EssenceClass
from fun.render_fun import get_EssanceList

class EssenceStorage:
    def __init__(self, screen):
        self.screen = screen
        self.left = 100
        self.top = 100
        self.density = 1.5

        self.EssenceList = get_EssanceList()
        self.collision_mup = [[EssenceClass(el, isicon=True) for el in row] for row in self.EssenceList]

    def render(self, zoom=50):
        for x in range(len(self.EssenceList)):
            for y in range(len(self.EssenceList[x])):
                left = (y * zoom * self.density + self.left)
                top = (x * zoom * self.density + self.top)
                self.collision_mup[x][y].render(self.screen, left, top, zoom)

    def click_on_cell(self, pos):
        for x in range(len(self.EssenceList)):
            for y in range(len(self.EssenceList[x])):
                if self.collision_mup[x][y].rect.collidepoint(pos):
                    return (x, y)