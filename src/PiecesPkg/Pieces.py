import pygame

class Pieces():
	def __init__(self, size):
		font = pygame.font.SysFont('verdana', size)
		self.pawnb = font.render("P", True, (0, 0, 0))
		self.knightb = font.render("N", True, (0, 0, 0))
		self.bishopb = font.render("B", True, (0, 0, 0))
		self.rookb = font.render("R", True, (0, 0, 0))
		self.queenb = font.render("Q", True, (0, 0, 0))
		self.kingb = font.render("K", True, (0, 0, 0))
		
		self.pawnw = font.render("P", True, (255, 255, 255))
		self.knightw = font.render("N", True, (255, 255, 255))
		self.bishopw = font.render("B", True, (255, 255, 255))
		self.rookw = font.render("R", True, (255, 255, 255))
		self.queenw = font.render("Q", True, (255, 255, 255))
		self.kingw = font.render("K", True, (255, 255, 255))
	
