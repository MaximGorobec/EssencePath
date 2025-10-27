import pygame
from fun.render_fun import get_info
from fun.render_fun import is_connected_subgraph, white_black_convert

class EssenceClass(pygame.sprite.Sprite):
    def __init__(self, essence_type, gray=False):
        super().__init__()
        self.essence_type = essence_type
        self.gray = gray
        self.clored_img = pygame.image.load(f'data/images/essentials/{self.essence_type}.png').convert_alpha()
        self.gray_img = white_black_convert(self.clored_img)
        try:
            self.img = self.clored_img
        except Exception as e:
            self.img = pygame.image.load(f'data/images/tile.png').convert_alpha()
            print("нет спрайта", essence_type)


    def render(self, screen, left, top, zoom):
        if self.gray:  img = self.gray_img
        else: img = self.clored_img
        img = pygame.transform.scale(img, (zoom * 1.5, zoom * 1.5))
        self.rect = img.get_rect(center=(left, top))
        if (self.rect.bottom <= screen.get_height()) and (self.rect.bottom > 0):
            screen.blit(img, self.rect)


    def render_info(self, EssenceStorage, zoom):
        rect = self.rect.copy()
        rect.width = 200
        rect.center = (self.rect.center[0] + 100, self.rect.center[1] - 75)
        pygame.draw.rect(EssenceStorage.screen, (0, 0, 0), rect)
        info = get_info(self.essence_type)
        if info is not None:
            if len(info) == 1:
                self.render(EssenceStorage.screen, rect[0] + zoom, rect[1] + zoom / 1.5, zoom)
            else:
                el1 = EssenceClass(info[0])
                el2 = EssenceClass(info[1])
                el1.render(EssenceStorage.screen, rect[0] + zoom,rect[1] + zoom / 1.5, zoom )
                el2.render(EssenceStorage.screen, rect[0] + 3 * zoom,rect[1] + zoom / 1.5, zoom )





