import pygame

class EssenceClass(pygame.sprite.Sprite):
    def __init__(self, essence_type):
        super().__init__()
        self.essence_type = essence_type
        try:
            self.img = pygame.image.load(f'images/essentials/{self.essence_type}.png')
        except Exception as e:
            self.img = pygame.image.load(f'images/tile.png')
            print("нет спрайта", essence_type)

    def render(self, screen, left, top, zoom):
        self.img = pygame.transform.scale(self.img, (zoom * 1.5, zoom * 1.5))
        self.rect = self.img.get_rect(center=(left, top))
        if (self.rect.bottom <= screen.get_height()) and (self.rect.bottom > 0):
            screen.blit(self.img, self.rect)

    def render_info(self, EssenceStorage):
        pygame.draw.rect(EssenceStorage.screen, (255, 255, 255), self.rect)
