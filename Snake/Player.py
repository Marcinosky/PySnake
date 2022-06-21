import pygame
from Core import WIDTH, HEIGHT, display, setting
import Core as c

class Snake(pygame.sprite.Sprite):
	def __init__(self, filename):
		super().__init__()
		self.x = int(WIDTH/2)
		self.y = int(HEIGHT/2)
		self.xmove = 0
		self.ymove = 0
		self.snake = []
		self.points = 1

	def point(self, value=1):
		self.points += value
		print(value)

	def get(self):
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

		if len(self.snake) > self.points:			# remove the last segment
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
						case _: 
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
		match self.snake[-1][2]:
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

	def getmovex(self):
		return self.xmove
	def getmovey(self):
		return self.ymove	

	def goleft(self):
		self.xmove = -20
		self.ymove = 0
		if self.points == 1:
			self.file = c.START_L
	def goright(self):
		self.xmove = 20
		self.ymove = 0
		if self.points == 1:
			self.file = c.START_R
	def goup(self):
		self.ymove = -20
		self.xmove = 0
		if self.points == 1:
			self.file = c.START_U
	def godown(self):
		self.ymove = 20
		self.xmove = 0
		if self.points == 1:
			self.file = c.START_D

	def update(self):
		self.x += self.xmove
		self.y += self.ymove

	def running(self):
		for segment in self.snake[:-1]:
			if self.points > 1 and self.x == segment[0] and self.y == segment[1]:
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
				return True		# tp setting removes border kill zone
			else:
				return  False
		return True				# if not oob, and not on snake - continue