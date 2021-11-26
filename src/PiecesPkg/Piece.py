import pygame

class Piece:
	def __init__(self, x, y, size, color):
		self.size = size
		self.x = x
		self.y = y
		self.color = color # while = 0, black = 1
		self.selected = False

	def move(self, screen):
		pass
