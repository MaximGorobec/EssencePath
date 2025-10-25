import pygame

class TileClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('images/tile.png')

    def render(self, screen, left, top, zoom):
        self.img = pygame.transform.scale(self.img, (zoom * 1.5, zoom * 1.5))
        self.rect = self.img.get_rect(center=(left, top))
        screen.blit(self.img, self.rect)
