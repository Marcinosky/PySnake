import pygame, os
from sys import exit
from random import randint

width, height = 640, 480

pygame.init()
display = pygame.display.set_mode((width,height))

off=(168,198,78)
on=(60,65,44)

font1 = pygame.font.Font(os.path.abspath('Pixellari.ttf'), 14)
font2 = pygame.font.Font(os.path.abspath('Pixellari.ttf'), 34)
font3 = pygame.font.Font(os.path.abspath('Pixellari.ttf'), 64)

x, y = 320, 240
xmove, ymove = 0, 0
xfood, yfood = 0, 0
xfcords, yfcords = [*range(20,630,20)], [*range(20,470,20)]
points = 1
snake = []

setting = 1 # border setting

pygame.display.set_caption('Pyton')

clock = pygame.time.Clock()

class Text:
    def __init__(self, text, text_colour, pos_x_center, pos_y_center, font):
        self.text = str(text)
        self.font = font
        self.image = self.font.render(self.text, 1, text_colour)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x_center, pos_y_center]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

def genfood():
	global xfood, yfood
	xfood, yfood = xfcords[randint(0,len(xfcords)-1)], yfcords[randint(0,len(yfcords)-1)]
	if xfood == x and yfood == y: genfood()

def bordertp():
	global x, y
	if x <= 0 or x >= width or y <= 0 or y >= height:
			if x <= 0:
				x = width-20
			elif x >= width:
				x = 20
			elif y <= 0:
				y = height-20
			elif y >= height:
				y = 20

def borderkill():
	if x <= 0 or x >= width or y <= 0 or y >= height:
			running = False

def snakegen():
	global snake
	snake_head = [x,y]
	snake.append(snake_head)
	if len(snake) > points:
		del snake[0]

def game():
	global x, y, snake, xmove, ymove, xfood, yfood, points
	genfood()
	running = True
	while running:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and xmove != 20:
					xmove = -20
					ymove = 0
					break	# without break turning on the spot is possible
				elif event.key == pygame.K_RIGHT and xmove != -20:
					xmove = 20
					ymove = 0
					break
				elif event.key == pygame.K_UP and ymove != 20:
					ymove = -20
					xmove = 0
					break
				elif event.key == pygame.K_DOWN and ymove != -20:
					ymove = 20
					xmove = 0
					break
				elif event.key == pygame.K_SPACE:
					print(f"{x},{y}")
			
		x += xmove
		y += ymove

		for segment in snake:
			if points > 1 and x == segment[0] and y == segment[1]:
				running=False

		if setting:
			bordertp()
		else:
			borderkill()

		if x == xfood and y == yfood:
			points += 1
			genfood()

		snakegen()

		display.fill(on)

		
	
		pygame.draw.rect(display,off,[10,10,width-20,height-20]) 				# ramka

		Desciption = Text("A simplistic Snake clone project", on, 320, 340, font2)
		Desciption.draw(display)

		Credit = Text("Made for an university project. Seweryn Marcinowski 2022", on, 200, 460, font1)
		Credit.draw(display)


		for segment in snake:
			pygame.draw.rect(display,on,[segment[0]-10,segment[1]-10,20,20])	# wonsz
		pygame.draw.rect(display,on,[xfood-5,yfood-5,10,10])					# jedzenie
		
		pygame.display.update()

		clock.tick(2)

def settings():
	running = True
	while running:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			
		display.fill(on)
	
		pygame.draw.rect(display,off,[10,10,width-20,height-20])				# ramka
	


		pygame.display.update()
		clock.tick(2)

def splash():
	running = True
	while running:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			
		display.fill(on)
	
		pygame.draw.rect(display,off,[10,10,width-20,height-20])				# ramka

		logo = pygame.image.load(os.path.abspath('logo.png'))
		display.blit(logo,(70,130))

		Desciption = Text("A simple Snake clone", on, 320, 350, font2)
		Desciption.draw(display)

		Credit = Text("Made for an university project. Seweryn Marcinowski 2022", on, 197, 460, font1)
		Credit.draw(display)

		pygame.display.update()
		clock.tick(2)

def splash():
	running = True
	while running:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					running=False
			
		display.fill(on)
	
		pygame.draw.rect(display,off,[10,10,width-20,height-20])				# ramka

		logo = pygame.image.load(os.path.abspath('logo.png'))
		display.blit(logo,(70,130))

		Desciption = Text("Press RETURN to start", on, 320, 350, font2)
		Desciption.draw(display)

		Credit = Text("Made for an university project. Seweryn Marcinowski 2022", on, 197, 460, font1)
		Credit.draw(display)

		pygame.display.update()
		clock.tick(2)

def menu():
	running = True
	while running:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running=False
			
		display.fill(on)
	
		pygame.draw.rect(display,off,[10,10,width-20,height-20])				# ramka

		logo = pygame.image.load(os.path.abspath('logo.png'))
		display.blit(logo,(70,70))

		

		Credit = Text("Made for an university project. Seweryn Marcinowski 2022", on, 197, 460, font1)
		Credit.draw(display)

		pygame.display.update()
		clock.tick(2)

splash()
menu()

pygame.quit()
exit()

