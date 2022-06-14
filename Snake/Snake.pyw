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
xfcords, yfcords = [*range(15,625,20)], [*range(15,465,20)]

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
			elif event.key == pygame.K_RIGHT and xmove != -20:
				xmove = 20
				ymove = 0
			elif event.key == pygame.K_UP and ymove != 20:
				ymove = -20
				xmove = 0
			elif event.key == pygame.K_DOWN and ymove != -20:
				ymove = 20
				xmove = 0
		
	x += xmove
	y += ymove
	print(x, y, xfood, yfood)
	display.fill(on)
	pygame.draw.rect(display,off,[10,10,width-20,height-20])	# ramka
	pygame.draw.rect(display,on,[x-10,y-10,20,20])				# glowa
	#for i in xfcords:
	#	for j in yfcords:
	#		pygame.draw.rect(display,on,[i,j,10,10])		# jedzenie
	pygame.draw.rect(display,on,[xfood,yfood,10,10])


	pygame.display.update()

	clock.tick(2)

	if x <= 0 or x > width or y <= 0 or y > height:
		running = False
pygame.quit()
exit()

