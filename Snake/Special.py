import Food
from random import randint
import Core as c
import pygame

powerup = None
xtrafood = []
x3counter = 0

TICKRATE = 4

class minus1(Food.Food):
	def __init__(self, player):
		super().__init__(player)
		self.player = player
		self.life = 30
	
	def update(self):
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:
			if self.player.points == 1:
				pygame.quit()
				exit()				#replace with fail screen
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
		self.life = 30
	
	def update(self):
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:	
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
		self.life = 30
	
	def update(self):
		global x3counter
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:	
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
		self.life = 30
	
	def update(self):
		global x3counter
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:	
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
		self.life = 30
	
	def update(self):
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:	
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
		self.life = 30
	
	def update(self):
		if self.player.getx() == self.xfood and self.player.gety() == self.yfood:	
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
		if randint(1,100) < 5:	#	~5% chance of drop
			match randint(1,6):
				case 1:
					powerup = faster(player)
				case 2:
					if TICKRATE > 4:
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
		if powerup.update() == 0:
			del powerup
			powerup = None
		else:
			powerup.draw()
	for each in xtrafood:
		each.update()
		each.draw()



  
