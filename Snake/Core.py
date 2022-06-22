import pygame, os

OFF = (168,198,78)	# monochromatic color schme
ON = (60,65,44)		# can be changed but couldn't figure out how to change graphics color

RESOLUTION = WIDTH, HEIGHT = 640, 480	# might try adding custom resolutions but grid system isnt prepared


# initializing game files and pygame
Snake = os.path.abspath('Assets\\Snake')
Pickups = os.path.abspath('Assets\\Pickups')
files = os.listdir(Snake)

for file_name in files:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(Snake, file_name))

files = os.listdir(Pickups)

for file_name in files:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(Pickups, file_name))

pygame.init()
display = pygame.display.set_mode(RESOLUTION)
icon = pygame.image.load(os.path.abspath('Assets\\Snake\\start_U.png'))
pygame.display.set_icon(icon)
pygame.display.set_caption('PySnake')
clock = pygame.time.Clock()

# font loading is really inefficient and it's better to do it once rather than every time when creating a text object
font1 = pygame.font.Font(os.path.abspath('Assets\\GUI\\Pixellari.ttf'), 14)
font2 = pygame.font.Font(os.path.abspath('Assets\\GUI\\Pixellari.ttf'), 22)
font3 = pygame.font.Font(os.path.abspath('Assets\\GUI\\Pixellari.ttf'), 34)
font4 = pygame.font.Font(os.path.abspath('Assets\\GUI\\Pixellari.ttf'), 64)

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
			surface.blit(btn,(self.pos_x,self.pos_y))
			super().draw(surface, ON)
		else:
			btn = pygame.image.load(os.path.abspath('Assets\\GUI\\button.png'))
			surface.blit(btn,(self.pos_x,self.pos_y))
			super().draw(surface, OFF)

	def collidepoint(self, mouse_pos_x, mouse_pos_y):
		if mouse_pos_x >= self.pos_x and \
			mouse_pos_x < self.pos_x + 120 and \
			mouse_pos_y >= self.pos_y and \
			mouse_pos_y < self.pos_y + 60:
			return True

class Option(Text):
	def __init__(self, text, pos_x_center, pos_y_center):
		super().__init__(text, pos_x_center, pos_y_center, font2)
		self.pos_x = pos_x_center - 70
		self.pos_y = pos_y_center - 20

	def draw(self, surface, selected=False):
		if selected:
			btn = pygame.image.load(os.path.abspath('Assets\\GUI\\settingchecked.png'))
			surface.blit(btn,(self.pos_x,self.pos_y))
			super().draw(surface, OFF)
		else:
			btn = pygame.image.load(os.path.abspath('Assets\\GUI\\setting.png'))
			surface.blit(btn,(self.pos_x,self.pos_y))
			super().draw(surface, ON)

	def collidepoint(self, mouse_pos_x, mouse_pos_y):
		if mouse_pos_x >= self.pos_x and \
			mouse_pos_x < self.pos_x + 140 and \
			mouse_pos_y >= self.pos_y and \
			mouse_pos_y < self.pos_y + 40:
			return True

# class Setting(Option):		Might try this later
# 	def __init__(self, text, pos_x_center, pos_y_center):
# 		self.description = super().__init__(text, pos_x_center-295, pos_y_center)
# 		self.choice1 = super().__init__("low", pos_x_center-145, pos_y_center)
# 		self.choice2 = super().__init__("default", pos_x_center+5, pos_y_center)
# 		self.choice3 = super().__init__("high", pos_x_center+155, pos_y_center)
# 		self.pos_x = pos_x_center - 295
# 		self.pos_y = pos_y_center - 20

# 	def draw(self, surface):
# 		self.description.draw(surface)
# 		self.choice1.draw(surface)
# 		self.choice2.draw(surface)
# 		self.choice3.draw(surface)

class Checkbox():
	def __init__(self, pos_x_center, pos_y_center):
		self.pos_x = pos_x_center - 20
		self.pos_y = pos_y_center - 20

	def draw(self, surface, checked=False):
		if checked:
			btn = pygame.image.load(os.path.abspath('Assets\\GUI\\boxchecked.png'))
			surface.blit(btn,(self.pos_x,self.pos_y))
		else:
			btn = pygame.image.load(os.path.abspath('Assets\\GUI\\box.png'))
			surface.blit(btn,(self.pos_x,self.pos_y))

	def collidepoint(self, mouse_pos_x, mouse_pos_y):
		if mouse_pos_x >= self.pos_x and \
			mouse_pos_x < self.pos_x + 40 and \
			mouse_pos_y >= self.pos_y and \
			mouse_pos_y < self.pos_y + 40:
			return True