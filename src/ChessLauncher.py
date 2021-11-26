import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 30

screenwidth = 500
screenheight= 500

screen = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption("Chess")

run = True

while run:
	clock.tick(fps)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	#tick
	
	#render
	pygame.display.update()
