import pygame

class Square:
	def __init__(self, size, x, y):#x=0, y=0 is top left
		self.rect = pygame.Rect(x*size, y*size, size, size)
		self.color = (200, 200, 200) if (x+y)%2==0 else (50,50,50)
		#self.color = (30*x, 0, 0) if (x+y)%2==0 else (0,30*y,0)
		self.highlight = False
		self.piece = ''
	
	def addPiece(self, piece):
		self.piece = piece
	
	def render(self, screen):
		if self.highlight:
			pygame.draw.rect(screen, (255, 0, 0), self.rect)
		else:
			pygame.draw.rect(screen, self.color, self.rect)
		if self.piece != '':
			self.piece.render(screen)
			
	def click(self):
		self.highlight = not self.highlight
		return self.highlight
