import pygame, os

OFF = (168,198,78)
ON = (60,65,44)

RESOLUTION = WIDTH, HEIGHT = 640, 480

Snake = os.path.abspath('Assets\\Snake')
Pickups = os.path.abspath('Assets\\Pickups')
files = os.listdir(Snake)

for file_name in files:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(Snake, file_name))
    print(Pickups)

SNAKE_LIST = [  HEAD_D,
                HEAD_L,
                HEAD_R,
                HEAD_U,
                HEAD_D_OPEN,
                HEAD_L_OPEN,
                HEAD_R_OPEN,
                HEAD_U_OPEN,
                SEGMENT_DL,
                SEGMENT_DR,
                SEGMENT_H,
                SEGMENT_UL,
                SEGMENT_UR,
                SEGMENT_V,
                START_D,
                START_L,
                START_R,
                START_U,
                START_D_OPEN,
                START_L_OPEN,
                START_R_OPEN,
                START_U_OPEN,
                TAIL_D,
                TAIL_L,
                TAIL_R,
                TAIL_U ]

files = os.listdir(Pickups)

for file_name in files:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(Pickups, file_name))
    print(image_name)

PICKUP_LIST = [ MINUS1,
                NORMAL,
                PLUS3,
                SLOW,
                SPEED,
                TIMES3,
                BLANK,
                DIVIDE ]

pygame.init()
display = pygame.display.set_mode(RESOLUTION)
icon = pygame.image.load(os.path.abspath('Assets\\Snake\\start_U.png'))
pygame.display.set_icon(icon)
pygame.display.set_caption('PySnake')
clock = pygame.time.Clock()

font1 = pygame.font.Font(os.path.abspath('Assets\\GUI\\Pixellari.ttf'), 14)
font2 = pygame.font.Font(os.path.abspath('Assets\\GUI\\Pixellari.ttf'), 22)
font3 = pygame.font.Font(os.path.abspath('Assets\\GUI\\Pixellari.ttf'), 34)
font4 = pygame.font.Font(os.path.abspath('Assets\\GUI\\Pixellari.ttf'), 64)

setting = None # border setting

class Text:
    def __init__(self, text, pos_x_center, pos_y_center, font):
        self.text = str(text)
        self.font = font
        self.center = [pos_x_center, pos_y_center]

    def draw(self, surface,  text_colour):
        image = self.font.render(self.text, 1, text_colour)
        rect = image.get_rect()
        rect.center = self.center
        surface.blit(image, rect)

class Button(Text):
	def __init__(self, text, pos_x_center, pos_y_center):
		super().__init__(text, pos_x_center, pos_y_center, font2)
		self.pos_x = pos_x_center - 60
		self.pos_y = pos_y_center - 30

	def draw(self, surface, hover=None):
		if hover:
			btn = pygame.image.load(os.path.abspath('Assets\\GUI\\buttonclick.png'))
			display.blit(btn,(self.pos_x,self.pos_y))
			super().draw(surface, ON)
		else:
			btn = pygame.image.load(os.path.abspath('Assets\\GUI\\button.png'))
			display.blit(btn,(self.pos_x,self.pos_y))
			super().draw(surface, OFF)

	def collidepoint(self, mouse_pos_x, mouse_pos_y):
		if mouse_pos_x >= self.pos_x and \
			mouse_pos_x < self.pos_x + 120 and \
			mouse_pos_y >= self.pos_y and \
			mouse_pos_y < self.pos_y + 60:
			return True