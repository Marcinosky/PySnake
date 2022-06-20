import pygame, os

OFF = (168,198,78)
ON = (60,65,44)

RESOLUTION = WIDTH, HEIGHT = 640, 480

folder = os.path.abspath('Assets\\Snake')
files = os.listdir(folder)

for file_name in files:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(folder, file_name))
    print(image_name)

SNAKE_LIST = [  HEAD_D,
                HEAD_L,
                HEAD_R,
                HEAD_U,
                SEGMENT_BL,
                SEGMENT_BR,
                SEGMENT_H,
                SEGMENT_UL,
                SEGMENT_UR,
                SEGMENT_V,
                START_D,
                START_L,
                START_R,
                START_U,
                TAIL_D,
                TAIL_L,
                TAIL_R,
                TAIL_U ]

