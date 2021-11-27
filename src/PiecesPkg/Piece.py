import pygame

class Piece:
	def __init__(self, x, y, size, color, piece):
		self.size = size
		self.x = x
		self.y = y
		self.color = color # while = 0, black = 1
		self.selected = False
		self.piece = piece
		self.moved = False
	
	def render(self, screen):
		screen.blit(self.piece, (self.x*self.size, self.y*self.size))
		#pygame.draw.rect(screen, (150,150,150), (self.x*self.size, self.y*self.size, self.size,self.size))

	def move(self, x, y):
		#TODO: animate
		self.x = x
		self.y = y
		self.moved = True
