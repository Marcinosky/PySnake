import pygame
from sys import exit
from random import randint

width, height = 640, 480

pygame.init()
display = pygame.display.set_mode((width,height))

off=(168,198,78)
on=(60,65,44)

x, y = 320, 240
xmove, ymove = 0, 0
xfood, yfood = 0, 0
xfcords, yfcords = [*range(20,630,20)], [*range(20,470,20)]
points = 1
snake = []

setting = 1 # border kill setting

pygame.display.set_caption('Pyton')

clock = pygame.time.Clock()

def genfood():
	global xfood, yfood
	xfood, yfood = xfcords[randint(0,len(xfcords)-1)], yfcords[randint(0,len(yfcords)-1)]
	if xfood == x and yfood == y: genfood()

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
		
	x += xmove
	y += ymove
	snake_head = [x,y]
	snake.append(snake_head)
	if len(snake) > points:
		del snake[0]
	display.fill(on)
	pygame.draw.rect(display,off,[10,10,width-20,height-20])	# ramka
	for segment in snake:
		pygame.draw.rect(display,on,[segment[0]-10,segment[1]-10,20,20])				# wonsz
	pygame.draw.rect(display,on,[xfood-5,yfood-5,10,10])		# jedzenie

	pygame.display.update()

	clock.tick(2)

	if x == xfood and y == yfood:
		points += 1
		genfood()

	if setting:
		if x <= 0 or x >= width or y <= 0 or y >= height:
			if x <= 0:
				print(f"foob {x} {y}")
				x = width
				print(f"toob {x} {y}")
			elif x >= width:
				print(f"foob {x} {y}")
				x = 0
				print(f"toob {x} {y}")
			elif y <= 0:
				print(f"foob {x} {y}")
				y = height
				print(f"toob {x} {y}")
			elif y >= height:
				print(f"foob {x} {y}")
				y = 0
				print(f"toob {x} {y}")
	else:
		if x <= 0 or x >= width or y <= 0 or y >= height:
			running = False
pygame.quit()
exit()

