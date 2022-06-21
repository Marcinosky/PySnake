import pygame, os, Special
import Core as c
from sys import exit
from random import randint
from Core import 	ON, OFF, RESOLUTION, WIDTH, HEIGHT, \
					Text, Button, display, clock, \
					font1, font2, font3, font4
from Player import Snake
from Food import Food

# ---------------------------------------------------------------------------

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
				if event.key == pygame.K_LEFT and player.get() != 'r':
					player.goleft()
					break	# without break turning on the spot is possible
				elif event.key == pygame.K_RIGHT and player.get() != 'l':
					player.goright()
					break
				elif event.key == pygame.K_UP and player.get() != 'd':
					player.goup()
					break
				elif event.key == pygame.K_DOWN and player.get() != 'u':
					player.godown()
					break	
				elif event.key == pygame.K_SPACE:
					break	

		player.update()	
		food.update()
					
		display.fill(ON)
	
		pygame.draw.rect(display,OFF,[10,10,WIDTH-20,HEIGHT-20]) 		# ramka
		
		player.draw()													# wonsz
		food.draw()														# jedzenie		
		Special.run(player)
		
		pygame.display.update()
		clock.tick(Special.TICKRATE)

def settings():
	running = True
	while running:

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
			
		display.fill(ON)
	
		pygame.draw.rect(display,OFF,[10,10,WIDTH-20,HEIGHT-20])		# ramka
	
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

		logo = pygame.image.load(os.path.abspath('Assets\\GUI\\logo.png'))
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

		logo = pygame.image.load(os.path.abspath('Assets\\GUI\\logo.png'))
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

splash()
menu()

pygame.quit()
exit()

