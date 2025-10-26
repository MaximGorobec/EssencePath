from classes.BoardClass import BoardClass
from classes.EssenceStorageClass import EssenceStorage
from fun.render_fun import *
import asyncio
from time import sleep

FPS = 60
pygame.init()
pygame.display.set_caption('Essence Path')
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
EssenceStorage = EssenceStorage(screen)

turning_pages_sound = pygame.mixer.Sound('data/sounds/book-turning-pages.mp3')

async def main():
    running = True
    mouse_memory = None
    mouse_pos = (0, 0)
    mouse_collide = None
    t = 0
    zoom = 50
    Board = BoardClass(screen, randint(4, 6), zoom)
    background_image = pygame.image.load('data/images/old_paper_fon.jpg')

    while running:
        screen.blit(pygame.transform.scale(background_image, screen.get_size()), (0, 0))
        Board.render()
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
                if event.button == 2:
                    mouse_memory = Board.essence_mup[board_click[0]][board_click[1]]

            if event.type == pygame.MOUSEBUTTONUP:
                board_click = Board.click_on_cell(event.pos)
                if (board_click not in Board.block_tiles) and (board_click is not None):
                    if event.button == 1:
                        if board_click is not None:
                            if mouse_memory is not None:
                                Board.essence_mup[board_click[0]][board_click[1]] = mouse_memory
                                pygame.mixer.Sound('data/sounds/pencil-write-on-cardboard.mp3').play().set_volume(0.1)
                                mouse_memory = None
                    if event.button == 3:
                        Board.essence_mup[board_click[0]][board_click[1]] = None
                        Board.remove_node(board_click)
                        pygame.mixer.Sound('data/sounds/pencil-write-on-paper.mp3').play(1, 400).set_volume(0.5)

            if event.type == pygame.MOUSEWHEEL:
                EssenceStorage.top += event.y * 20

        if mouse_memory is not None:
            screen.blit(pygame.transform.scale(pygame.image.load('data/images/spark.png'), (50, 50)), (mouse_pos[0] - 25, mouse_pos[1] - 25))

        if mouse_collide is not None:
            EssenceStorage.collision_mup[mouse_collide[0]][mouse_collide[1]].render_info(EssenceStorage, zoom)

        pygame.display.update()
        clock.tick(FPS)
        if is_connected_subgraph(Board.graf, Board.block_tiles):
            sleep(0.5)
            turning_pages_sound.play(1, 760)
            break

while True:
    asyncio.run(main())

#детектинг пути