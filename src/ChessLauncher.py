import pygame
from pygame.locals import *

from Board import Board
from RenderQueue import RenderQueue
from EventHandler import EventHandler
from Log import Log

pygame.init()

clock = pygame.time.Clock()
fps = 30

screenwidth = 800
screenheight= 800

screen = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption("Chess")

run = True

renderqueue = RenderQueue()
board = Board(0, 0, screenwidth)
log = Log()
eventhandler = EventHandler(renderqueue, board, log)

board.render(screen)

pygame.display.update()
while run:
	clock.tick(fps)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN: 
			eventhandler.click(pygame.mouse.get_pos())
	#tick
	
	#render
	if renderqueue.render(screen): pygame.display.update()
