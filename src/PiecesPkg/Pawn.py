import pygame

from PiecesPkg.Piece import Piece

class Pawn(Piece):
	def __init__(self, x, y, size, color, piece):
		super().__init__(x,y,size,color,piece)
		self.code = ""
	
	def render(self, screen):
		screen.blit(self.piece, (self.x*self.size, self.y*self.size))
		#pygame.draw.rect(screen, (150,150,150), (self.x*self.size, self.y*self.size, self.size,self.size))
	
	def foward(self, squares):
		valid = []
		y = self.y + (-1 if self.color==0 else 1)
		if squares[self.x][y].piece == False:
			if y==0 or y==7:
				valid.append([squares[self.x][y], 4])
			else:
				valid.append([squares[self.x][y], 0])
		if self.y == 1 and self.color == 1:
			if squares[self.x][self.y+2].piece == False:
				valid.append([squares[self.x][self.y+2], 0])
		if self.y == 6 and self.color == 0:
			if squares[self.x][self.y-2].piece == False:
				valid.append([squares[self.x][self.y-2], 0])
		return valid
	def diagonal(self, squares):
		y = self.y + (-1 if self.color==0 else 1)
		valid = []
		if self.x<7:
			if squares[self.x+1][y].piece != False:
				if squares[self.x+1][y].piece.color != self.color:
					valid.append([squares[self.x+1][y], 1])
		if self.x>0:
			if squares[self.x-1][y].piece != False:
				if squares[self.x-1][y].piece.color != self.color:
					valid.append([squares[self.x-1][y], 1])
		return valid
		
	def validmoves(self, squares):
		valid = []
		for i in self.foward(squares): valid.append(i)
		for i in self.diagonal(squares): valid.append(i)
		return valid
		
		
