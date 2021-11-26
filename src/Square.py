import pygame

class Square:
	def __init__(self, size, x, y):#x=0, y=0 is top left
		self.rect = pygame.Rect(x*size, y*size, size, size)
		self.x = x
		self.y = y
		self.basecolor = (150, 150, 255) if (x+y)%2==0 else (50,50,150)
		#self.basecolor = (30*x, 0, 0) if (x+y)%2==0 else (0,30*y,0)
		self.selected = False
		self.piece = False
		self.resetcolor()
	
	def addPiece(self, piece):
		self.piece = piece
	
	def render(self, screen):
		pygame.draw.rect(screen, self.color, self.rect)
		if self.piece != False:
			self.piece.render(screen)
		#TODO: return square
			
	def recolor(self, num):
		self.color = (self.basecolor[0]/(num+1), self.basecolor[1]/(num+1), self.basecolor[2]/(num+1))
	
	def resetcolor(self):
		self.color = (self.basecolor[0], self.basecolor[1], self.basecolor[2])
		
	def movePiece(self, newsquare):
		#animate
		self.piece.move(newsquare.x, newsquare.y)
		newsquare.addPiece(self.piece)
		self.piece=False
		
	def getnotation(self):
		return chr(ord('a')+self.x)+str(8-self.y)
