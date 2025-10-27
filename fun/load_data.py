
import pygame

pygame.init()

background_image = pygame.image.load('data/images/old_paper_fon.jpg')
turning_pages_sound = pygame.mixer.Sound('data/sounds/book-turning-pages.mp3')
pencil_write_on_cardboard = pygame.mixer.Sound('data/sounds/pencil-write-on-cardboard.mp3')
pencil_write_on_paper = pygame.mixer.Sound('data/sounds/pencil-write-on-paper.mp3')
spark_img = pygame.image.load('data/images/spark.png')