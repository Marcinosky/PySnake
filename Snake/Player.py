import pygame, os
from Core import WIDTH, HEIGHT, display, font4, font2, ON, OFF
import Core as c
import Special as s
from importlib import reload

class Snake(pygame.sprite.Sprite):
	def __init__(self, filename):
		super().__init__()
		self.x = int(WIDTH/2)
		self.y = int(HEIGHT/2)
		self.xmove = 0
		self.ymove = 0
		self.snake = []		# initializing snake body
		self.points = 1

	def point(self, value=1):
		self.points += value

	def get(self):	# returns the direction of the snake
		if self.ymove == 0 and self.xmove != 0: 	# x
			if self.xmove == -20:
				return 'l'	# left
			if self.xmove == 20:
				return 'r'	# right
		elif self.xmove == 0 and self.ymove != 0: 	# y
			if self.ymove == -20:
				return 'u'	# up
			if self.ymove == 20:
				return 'd'	# down 

	def draw(self):
		snake_head = [self.x,self.y,self.get()]	# x, y, direction
		self.snake.append(snake_head)

		if len(self.snake) > 1:					# change direction of second segment too
			self.snake[-2][2] = self.get()

		if len(self.snake) > self.points:		# remove the last segment
			del self.snake[0]

		for segment in enumerate(self.snake):	# animation
			if self.points == 1:
				match segment[1][2]:
						case 'u':
							display.blit(c.START_U, (segment[1][0]-10,segment[1][1]-10))
						case 'r':
							display.blit(c.START_R, (segment[1][0]-10,segment[1][1]-10))
						case 'd':
							display.blit(c.START_D, (segment[1][0]-10,segment[1][1]-10))
						case 'l':
							display.blit(c.START_L, (segment[1][0]-10,segment[1][1]-10))
						case _: 	# starting position
							display.blit(c.START_U, (segment[1][0]-10,segment[1][1]-10))
			else:
				if segment[0] == len(self.snake)-1:		# head direction
					match segment[1][2]:
						case 'u':
							display.blit(c.HEAD_U, (segment[1][0]-10,segment[1][1]-10))
						case 'r':
							display.blit(c.HEAD_R, (segment[1][0]-10,segment[1][1]-10))
						case 'd':
							display.blit(c.HEAD_D, (segment[1][0]-10,segment[1][1]-10))
						case 'l':
							display.blit(c.HEAD_L, (segment[1][0]-10,segment[1][1]-10))
				elif segment[0] == 0:
					match segment[1][2]:				# tail direction
						case 'u':
							display.blit(c.TAIL_D, (segment[1][0]-10,segment[1][1]-10))
						case 'r':
							display.blit(c.TAIL_L, (segment[1][0]-10,segment[1][1]-10))
						case 'd':
							display.blit(c.TAIL_U, (segment[1][0]-10,segment[1][1]-10))
						case 'l':
							display.blit(c.TAIL_R, (segment[1][0]-10,segment[1][1]-10))
				else:									# turn direction and position
					if self.points > 2 and segment[1][2] != self.snake[segment[0]-1][2]:
						if		segment[1][2] == 'd' and self.snake[segment[0]-1][2] == 'l' or segment[1][2] == 'r' and self.snake[segment[0]-1][2] == 'u':
							display.blit(c.SEGMENT_DR, (segment[1][0]-10,segment[1][1]-10))
						elif 	segment[1][2] == 'u' and self.snake[segment[0]-1][2] == 'l' or segment[1][2] == 'r' and self.snake[segment[0]-1][2] == 'd':
							display.blit(c.SEGMENT_UR, (segment[1][0]-10,segment[1][1]-10))
						elif	segment[1][2] == 'd' and self.snake[segment[0]-1][2] == 'r' or segment[1][2] == 'l' and self.snake[segment[0]-1][2] == 'u':
							display.blit(c.SEGMENT_DL, (segment[1][0]-10,segment[1][1]-10))
						elif 	segment[1][2] == 'u' and self.snake[segment[0]-1][2] == 'r' or segment[1][2] == 'l' and self.snake[segment[0]-1][2] == 'd':
							display.blit(c.SEGMENT_UL, (segment[1][0]-10,segment[1][1]-10))
					else:								# continous body direction
						if segment[1][2] == 'u' or segment[1][2] == 'd':
							display.blit(c.SEGMENT_V, (segment[1][0]-10,segment[1][1]-10))
						else:
							display.blit(c.SEGMENT_H, (segment[1][0]-10,segment[1][1]-10))

	def openwide(self):
		match self.snake[-1][2]:	# opening the mouth if food will be eaten in the next tick
			case 'u':
				if self.points == 1:
					display.blit(c.START_U_OPEN, (self.snake[-1][0]-10,self.snake[-1][1]-10))
				else:
					display.blit(c.HEAD_U_OPEN, (self.snake[-1][0]-10,self.snake[-1][1]-10))
			case 'r':
				if self.points == 1:
					display.blit(c.START_R_OPEN, (self.snake[-1][0]-10,self.snake[-1][1]-10))
				else:
					display.blit(c.HEAD_R_OPEN, (self.snake[-1][0]-10,self.snake[-1][1]-10))
			case 'd':
				if self.points == 1:
					display.blit(c.START_D_OPEN, (self.snake[-1][0]-10,self.snake[-1][1]-10))
				else:
					display.blit(c.HEAD_D_OPEN, (self.snake[-1][0]-10,self.snake[-1][1]-10))
			case 'l':
				if self.points == 1:
					display.blit(c.START_L_OPEN, (self.snake[-1][0]-10,self.snake[-1][1]-10))
				else:
					display.blit(c.HEAD_L_OPEN, (self.snake[-1][0]-10,self.snake[-1][1]-10))

	def getx(self):
		return self.x
	def gety(self):
		return self.y

	def setx(self, value):
		self.x = value
	def sety(self, value):
		self.y = value

	def getmovex(self):
		return self.xmove
	def getmovey(self):
		return self.ymove	

	def goleft(self):
		self.xmove = -20
		self.ymove = 0
	def goright(self):
		self.xmove = 20
		self.ymove = 0
	def goup(self):
		self.ymove = -20
		self.xmove = 0
	def godown(self):
		self.ymove = 20
		self.xmove = 0

	def update(self):
		self.x += self.xmove
		self.y += self.ymove

	def running(self, setting=False):
		for segment in self.snake[:-1]:	# checking collision
			if self.points > 1 and self.x == segment[0] and self.y == segment[1]:
				return self.gameover()
		if self.x <= 0 or self.x >= WIDTH or self.y <= 0 or self.y >= HEIGHT:
			if setting:
				return True		# tp setting removes border kill zone
			else:
				return self.gameover()
		return True				# if not oob, and not on snake - continue

	def gameover(self):	# game over prompt displayed over the game
		pygame.mixer.music.load(os.path.abspath('Assets\\Sounds\\gameover.wav'))
		pygame.mixer.music.play(1)	
		reload(s)	# reloading specials (resets game speed, removes extra food)
		running = True
		while running:

			click = False
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					pygame.quit()
					exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1:
						pygame.mixer.music.load(os.path.abspath('Assets\\Sounds\\click.wav'))
						pygame.mixer.music.play(1)
						click = True

			pygame.draw.rect(display,ON,[WIDTH/2-250,HEIGHT/2-150, 500, 300])
			pygame.draw.rect(display,OFF,[WIDTH/2-240,HEIGHT/2-140, 480, 280])

			mx, my = pygame.mouse.get_pos()
			prompt = c.Text("GAME OVER", WIDTH/2, 160, font4)
			score = c.Text(f"Your score: {self.points}", WIDTH/2, 200, font2)
			
			prompt.draw(display, ON)
			score.draw(display, ON)

			play = c.Button("retry", WIDTH/2, HEIGHT/2+30)
			if play.collidepoint(mx,my):
				play.draw(display, 'hovered')
				if click:	# resets the snake position
					self.x = int(WIDTH/2)
					self.y = int(HEIGHT/2)
					self.xmove = 0
					self.ymove = 0
					self.snake = []
					self.points = 1
					return True	# continues the game
			else: play.draw(display)
			
			play = c.Button("main menu", WIDTH/2, HEIGHT/2+100)
			if play.collidepoint(mx,my):
				play.draw(display, 'hovered')
				if click: running=False
			else: play.draw(display)

			pygame.display.update()
			c.clock.tick(60)
		return False # quits the game