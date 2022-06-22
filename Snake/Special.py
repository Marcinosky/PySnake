from cgitb import reset
import Food
from random import randint
import Core as c
import pygame, os

powerup = None
xtrafood = []
x3counter = 0

DROP_CHANCE = 5			# Drop chance per tick global value
DROP_LAST = 40			# Drop wait in ticks global value
BASE_TICKRATE = 4		# Base speed global value

TICKRATE = BASE_TICKRATE

def changetickrate(value):
	global BASE_TICKRATE, TICKRATE
	BASE_TICKRATE = value
	TICKRATE = BASE_TICKRATE

def changechance(value):
	global DROP_CHANCE
	DROP_CHANCE = value

def changelast(value):
	global DROP_LAST
	DROP_LAST = value

class minus1(Food.Food):
	def __init__(self, player):
		super().__init__(player)
		self.player = player
		self.life = DROP_LAST
	
	def update(self):
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:
			pygame.mixer.music.load(os.path.abspath('Assets\\Sounds\\eat.wav'))
			pygame.mixer.music.play(1)
			if self.player.points == 1:
				if self.player.gameover():
					return 0 
				else:
					return -1
			else:	
				self.player.point(-1)
				del self.player.snake[0]
				return 0
		else:
			self.life -= 1
			return self.life

	def draw(self):
		if self.life < 10 and self.life %2:
			super().draw(c.BLANK)
		else:
			super().draw(c.MINUS1)

class plus3(Food.Food):
	def __init__(self, player):
		super().__init__(player)
		self.player = player
		self.life = DROP_LAST
	
	def update(self):
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:
			pygame.mixer.music.load(os.path.abspath('Assets\\Sounds\\eat.wav'))
			pygame.mixer.music.play(1)
			self.player.point(3)
			return 0
		else:
			self.life -= 1
			return self.life

	def draw(self):
		if self.life < 10 and self.life %2:
			super().draw(c.BLANK)
		else:
			super().draw(c.PLUS3)

class times3(Food.Food):
	def __init__(self, player):
		super().__init__(player)
		self.player = player
		self.life = DROP_LAST
	
	def update(self):
		global x3counter
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:
			pygame.mixer.music.load(os.path.abspath('Assets\\Sounds\\eat.wav'))
			pygame.mixer.music.play(1)
			x3counter += 1
			for each in range(x3counter*3):
				xtrafood.append(Food.Food(self.player))
			return 0
		else:
			self.life -= 1
			return self.life

	def draw(self):
		if self.life < 10 and self.life %2:
			super().draw(c.BLANK)
		else:
			super().draw(c.TIMES3)

class divide(Food.Food):
	def __init__(self, player):
		super().__init__(player)
		self.player = player
		self.life = DROP_LAST
	
	def update(self):
		global x3counter
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:
			pygame.mixer.music.load(os.path.abspath('Assets\\Sounds\\eat.wav'))
			pygame.mixer.music.play(1)	
			for each in range(x3counter*3):
				xtrafood.pop()
			x3counter -= 1
			return 0
		else:
			self.life -= 1
			return self.life

	def draw(self):
		if self.life < 10 and self.life %2:
			super().draw(c.BLANK)
		else:
			super().draw(c.DIVIDE)

class faster(Food.Food):
	def __init__(self, player):
		super().__init__(player)
		self.player = player
		self.life = DROP_LAST
	
	def update(self):
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:
			pygame.mixer.music.load(os.path.abspath('Assets\\Sounds\\eat.wav'))
			pygame.mixer.music.play(1)	
			global TICKRATE
			TICKRATE += 2
			return 0
		else:
			self.life -= 1
			return self.life

	def draw(self):
		if self.life < 10 and self.life %2:
			super().draw(c.BLANK)
		else:
			super().draw(c.SPEED)

class slower(Food.Food):
	def __init__(self, player):
		super().__init__(player)
		self.player = player
		self.life = DROP_LAST
	
	def update(self):
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:
			pygame.mixer.music.load(os.path.abspath('Assets\\Sounds\\eat.wav'))
			pygame.mixer.music.play(1)	
			global TICKRATE
			TICKRATE -= 2
			return 0
		else:
			self.life -= 1
			return self.life

	def draw(self):
		if self.life < 10 and self.life %2:
			super().draw(c.BLANK)
		else:
			super().draw(c.SLOW)

def run(player):
	global powerup
	if not powerup:
		if randint(1,100) < DROP_CHANCE:	#	default ~5% chance of drop
			pygame.mixer.music.load(os.path.abspath('Assets\\Sounds\\spawn.wav'))
			pygame.mixer.music.play(1)
			match randint(1,6):
				case 1:
					powerup = faster(player)
				case 2:
					if TICKRATE > BASE_TICKRATE:
						powerup = slower(player)
				case 3:
					powerup = times3(player)
				case 4:
					if x3counter != 0:
						powerup = divide(player)
				case 5:
					powerup = minus1(player)
				case 6:
					powerup = plus3(player)
	else:
		result = powerup.update()
		if result == 0:
			del powerup
			powerup = None
		elif result == -1:
			return False
		else:
			powerup.draw()
	for each in xtrafood:
		each.update()
		each.draw()



  
