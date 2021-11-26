import pygame
from pygame.locals import *

from Board import Board

pygame.init()

clock = pygame.time.Clock()
fps = 30

screenwidth = 800
screenheight= 800

screen = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption("Chess")

run = True

board = Board(screenwidth)
board.render(screen)

while run:
	clock.tick(fps)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	#tick
	
	#render
	pygame.display.update()
