import pygame, os
import Core as c
from sys import exit
from random import randint
from Core import ON, OFF, RESOLUTION, WIDTH, HEIGHT, SNAKE_LIST

pygame.init()
display = pygame.display.set_mode(RESOLUTION)
icon = pygame.image.load(os.path.abspath('Assets\\Snake\\start_U.png'))
pygame.display.set_icon(icon)
pygame.display.set_caption('PySnake')
clock = pygame.time.Clock()

font1 = pygame.font.Font(os.path.abspath('Pixellari.ttf'), 14)
font2 = pygame.font.Font(os.path.abspath('Pixellari.ttf'), 22)
font3 = pygame.font.Font(os.path.abspath('Pixellari.ttf'), 34)
font4 = pygame.font.Font(os.path.abspath('Pixellari.ttf'), 64)

points = 1

setting = None # border setting

# ---------------------------------------------------------------------------

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
			btn = pygame.image.load(os.path.abspath('buttonclick.png'))
			display.blit(btn,(self.pos_x,self.pos_y))
			super().draw(surface, ON)
		else:
			btn = pygame.image.load(os.path.abspath('button.png'))
			display.blit(btn,(self.pos_x,self.pos_y))
			super().draw(surface, OFF)

	def collidepoint(self, mouse_pos_x, mouse_pos_y):
		if mouse_pos_x >= self.pos_x and \
			mouse_pos_x < self.pos_x + 120 and \
			mouse_pos_y >= self.pos_y and \
			mouse_pos_y < self.pos_y + 60:
			return True

class Snake(pygame.sprite.Sprite):
	def __init__(self, filename):
		super().__init__()
		self.file = filename
		self.rect = self.file.get_rect()
		self.x = int(WIDTH/2)
		self.y = int(HEIGHT/2)
		self.xmove = 0
		self.ymove = 0
		self.snake = []

	def draw(self):
		snake_head = [self.x,self.y]
		self.snake.append(snake_head)
		if len(self.snake) > points:
			del self.snake[0]
		for segment in self.snake:
			pygame.draw.rect(display,ON,[segment[0]-10,segment[1]-10,20,20])
			#display.blit(self.file, self.rect)

	def get(self):
		if self.ymove == 0 and self.xmove != 0:
			return ['x',self.xmove]
		elif self.xmove == 0 and self.ymove != 0:
			return ['y',self.ymove]
		
	def getx(self):
		return self.x
	def gety(self):
		return self.y

	def goleft(self):
		self.xmove = -20
		self.ymove = 0
		self.image = c.START_L
	def goright(self):
		self.xmove = 20
		self.ymove = 0
		self.image = c.START_R
	def goup(self):
		self.ymove = -20
		self.xmove = 0
		self.image = c.START_U
	def godown(self):
		self.ymove = 20
		self.xmove = 0
		self.image = c.START_D

	def update(self):
		self.x += self.xmove
		self.y += self.ymove

	def running(self):
		for segment in self.snake:
			if points > 1 and (self.x + self.xmove) == segment[0] and (self.y + self.ymove) == segment[1]:
				return  False
		if self.x <= 0 or self.x >= WIDTH or self.y <= 0 or self.y >= HEIGHT:
			if setting:
				if self.x <= 0:
					self.x = WIDTH-20
				elif self.x >= WIDTH:
					self.x = 20
				elif self.y <= 0:
					self.y = HEIGHT-20
				elif self.y >= HEIGHT:
					self.y = 20
				return True		# ustawienie tp wyłącza zabijanie oob
			else:
				return  False
		return True				# jeśli nie oob, i nie na wężu kontynuuj gre

class Food():
	def __init__(self, player):
		self.player = player
		self.xfood, self.yfood = 0, 0
		self.xfcords, self.yfcords = [*range(20,WIDTH-10,20)], [*range(20,HEIGHT-10,20)]
		self.genfood()

	def genfood(self):
		self.xfood = self.xfcords[randint(0,len(self.xfcords)-1)]
		self.yfood = self.yfcords[randint(0,len(self.yfcords)-1)]
		if self.xfood == self.player.getx() and self.yfood == self.player.gety(): 
			self.genfood()

	def update(self):
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:
			global points
			points += 1
			self.genfood()

	def draw(self):
		pygame.draw.rect(display,ON,[self.xfood-5, self.yfood-5, 10, 10])


def game():
	
	player = Snake(c.START_U)
	food = Food(player)
	while player.running():
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and player.get() != ['x',20]:
					player.goleft()
					break	# without break turning ON the spot is possible
				elif event.key == pygame.K_RIGHT and player.get() != ['x',-20]:
					player.goright()
					break
				elif event.key == pygame.K_UP and player.get() != ['y',20]:
					player.goup()
					break
				elif event.key == pygame.K_DOWN and player.get() != ['y',-20]:
					player.godown()
					break	
		player.update()	
		food.update() 
					
		display.fill(ON)
	
		pygame.draw.rect(display,OFF,[10,10,WIDTH-20,HEIGHT-20]) 		# ramka
		player.draw()													# wonsz
		food.draw()														# jedzenie
		
		pygame.display.update()

		

		clock.tick(2)

def settings():
	running = True
	while running:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			
		display.fill(ON)
	
		pygame.draw.rect(display,OFF,[10,10,WIDTH-20,HEIGHT-20])				# ramka
	


		pygame.display.update()
		clock.tick(2)

def splash():
	running = True
	while running:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					running=False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running=False
					pygame.quit()
					exit()
			
		display.fill(ON)
	
		pygame.draw.rect(display,OFF,[10,10,WIDTH-20,HEIGHT-20])				# ramka

		logo = pygame.image.load(os.path.abspath('logo.png'))
		display.blit(logo,(70,130))

		Desciption = Text("Press RETURN to start", 320, 350, font3)
		Desciption.draw(display, ON)

		Credit = Text("Made for an university project. Seweryn Marcinowski 2022", 197, 460, font1)
		Credit.draw(display, ON)

		pygame.display.update()
		clock.tick(60)

def menu():
	running = True
	while running:

		click = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
			
		display.fill(ON)
	
		pygame.draw.rect(display,OFF,[10,10,WIDTH-20,HEIGHT-20])				# ramka

		logo = pygame.image.load(os.path.abspath('logo.png'))
		display.blit(logo,(70,60))

		mx, my = pygame.mouse.get_pos()

		play = Button("Start game", 320, 260)
		if play.collidepoint(mx,my):
			play.draw(display, 'hovered')
			if click:
				play.draw(display)
				game()
		else:
			play.draw(display)

		play = Button("Settings", 320, 330)
		if play.collidepoint(mx,my):
			play.draw(display, 'hovered')
			if click:
				play.draw(display)
				settings()
		else:
			play.draw(display)

		play = Button("Exit", 320, 400)
		if play.collidepoint(mx,my):
			play.draw(display, 'hovered')
			if click:
				play.draw(display)
				running=False
				pygame.quit()
				exit()
		else:
			play.draw(display)

		Credit = Text("Made for an university project. Seweryn Marcinowski 2022", 197, 460, font1)
		Credit.draw(display, ON)

		pygame.display.update()
		clock.tick(60)

# splash()
# menu()
game()

pygame.quit()
exit()

