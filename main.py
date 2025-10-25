import pygame
from classes.BoardClass import BoardClass
from classes.EssenceStorageClass import EssenceStorage
FPS = 60


pygame.init()
pygame.display.set_caption('Essence Path')
screen = pygame.display.set_mode((1000, 700))

width, height = screen.get_size()
clock = pygame.time.Clock()
background_image = pygame.image.load('images/old_paper_fon.jpg')

size = 3
Board = BoardClass(screen, 6)
running = True
mouse_memory = None
EssenceStorage = EssenceStorage(screen)
mouse_pos = (0, 0)
mouse_collide = None
t = 0
while running:
    screen.blit(pygame.transform.scale(background_image, screen.get_size()), (0, 0))
    Board.render(50)
    EssenceStorage.render()


    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            for i in range(len(EssenceStorage.collision_mup)):
                for j in range(len(EssenceStorage.collision_mup[i])):
                    if EssenceStorage.collision_mup[i][j].rect.collidepoint(mouse_pos):
                        mouse_collide = (i, j)
                        t = True
            if t:
                t = False
            else:
                mouse_collide = None

        if event.type == pygame.MOUSEBUTTONDOWN:
            board_click = Board.click_on_cell(event.pos)
            essence_storage_click = EssenceStorage.click_on_cell(pos=event.pos)
            if event.button == 1:
                if essence_storage_click is not None:
                    mouse_memory = EssenceStorage.collision_mup[essence_storage_click[0]][essence_storage_click[1]]

        if event.type == pygame.MOUSEBUTTONUP:
            board_click = Board.click_on_cell(event.pos)
            if board_click not in Board.block_tiles:
                if event.button == 1:
                    if board_click is not None:
                        Board.essence_mup[board_click[0]][board_click[1]] = mouse_memory
                        mouse_memory = None
                if event.button == 3:
                    Board.essence_mup[board_click[0]][board_click[1]] = None

        if event.type == pygame.MOUSEWHEEL:
            EssenceStorage.top += event.y * 20


    if mouse_memory is not None:
        screen.blit(pygame.transform.scale(pygame.image.load('images/spark.png'), (50, 50)), (mouse_pos[0] - 25, mouse_pos[1] - 25))

    if mouse_collide is not None:
        EssenceStorage.collision_mup[mouse_collide[0]][mouse_collide[1]].render_info(EssenceStorage)


    pygame.display.update()
    clock.tick(FPS)


#добавление элементов (словарь - элемент: состоит, что из него делается //api и автодобавдение
#соединения
#детектинг пути

