from math import cos, sin

import numpy as np
import pygame
from collections import deque
import os

from pprint import pprint

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
    EL =[]
    for entry in os.scandir("data/images/essentials"):
        if entry.is_file():
            EL.append(entry.name[:-4])
    n = 4
    return [EL[row:row + 4] for row in range(0, len(EL), n)]

def get_info(essence_type):
    info_list = {'aer': '_', 'alienis': ('tenebre', 'vacous'), 'aqua': '_', 'arbor': ('aer', 'herba'), 'auram': ('aer', 'precantatio'), 'bestia': ('motus', 'victus'), 'cognitio': ('ignis', 'spiritus'), 'corpus': ('bestia', 'mortuus'), 'exanimis': ('mortuus', 'motus'), 'fabrico': ('humanus', 'instrumentum'), 'fames': ('vacous', 'victus'), 'gelum': ('ignis', 'perditio'), 'herba': ('terra', 'victus'), 'humanus': ('bestia', 'cognitio'), 'ignis': '_', 'instrumentum': ('humanus', 'ordo'), 'iter': ('motus', 'terra'), 'limus': ('aqua', 'victus'), 'lucrum': ('fames', 'humanus'), 'lux': ('aer', 'ignis'), 'machina': ('instrumentum', 'motus'), 'messis': ('herba', 'humanus'), 'metallum': ('terra', 'vitreus'), 'meto': ('instrumentum', 'messis'), 'mortuus': ('perditio', 'victus'), 'motus': ('aer', 'ordo'), 'ordo': '_', 'pannus': ('bestia', 'instrumentum'), 'perditio': '_', 'perfodio': ('humanus', 'terra'), 'permutatio': ('ordo', 'perditio'), 'potentia': ('ignis', 'ordo'), 'precantatio': ('potentia', 'vacous'), 'sano': ('ordo', 'victus'), 'sensus': ('aer', 'spiritus'), 'spiritus': ('mortuus', 'victus'), 'telum': ('instrumentum', 'ignis'), 'tempestas': ('aer', 'aqua'), 'tenebre': ('lux', 'vacous'), 'terra': '_', 'tutamen': ('instrumentum', 'terra'), 'vacous': ('aer', 'perditio'), 'venenum': ('aqua', 'perditio'), 'victus': ('aqua', 'terra'), 'vinculum': ('motus', 'perditio'), 'vitium': ('perditio', 'precantatio'), 'vitreus': ('ordo', 'terra'), 'volatus': ('aer', 'motus')}
    if essence_type in info_list:
        return info_list[essence_type]
    else:
        print(f"У элемента {essence_type} нет описания")


def is_connected_subgraph(graph, target_nodes):
    if len(target_nodes) <= 1:
        return True

    start = target_nodes[0]
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return all(node in visited for node in target_nodes)

def white_black_convert(image):
    arr = pygame.surfarray.array3d(image)
    alpha = pygame.surfarray.array_alpha(image)
    gray = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]).astype(np.uint8)
    bw_arr = np.stack([gray, gray, gray], axis=2)
    bw_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)
    pygame.surfarray.blit_array(bw_image, bw_arr)
    pygame.surfarray.pixels_alpha(bw_image)[:] = alpha
    return bw_image