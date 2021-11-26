import pygame

from PiecesPkg.Piece import Piece

class Pawn(Piece):
	def __init__(self, x, y, size, color, piece):
		super().__init__(x,y,size,color)
		self.piece = piece
	
	def render(self, screen):
		screen.blit(self.piece, (self.x*self.size, self.y*self.size))
		#pygame.draw.rect(screen, (150,150,150), (self.x*self.size, self.y*self.size, self.size,self.size))
	
	def move(self, screen):
		pass
