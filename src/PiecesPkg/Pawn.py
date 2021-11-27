import pygame

from PiecesPkg.Piece import Piece

class Pawn(Piece):
	def __init__(self, x, y, size, color, piece):
		super().__init__(x,y,size,color,piece)
		self.code = ""
	
	def render(self, screen):
		screen.blit(self.piece, (self.x*self.size, self.y*self.size))
		#pygame.draw.rect(screen, (150,150,150), (self.x*self.size, self.y*self.size, self.size,self.size))
	
	def legalmoves(self, squares, lastmove):
		return self.validmoves(squares, lastmove)
		
	def validmoves(self, squares, lastmove):
		valid = []
		#forward
		y = self.y + (-1 if self.color==0 else 1)
		if squares[self.x][y].piece == False:
			if y==0 or y==7:
				valid.append([squares[self.x][y], 4])
			else:
				valid.append([squares[self.x][y], 0])
		if self.y == 1 and self.color == 1:
			if squares[self.x][self.y+2].piece == False:
				valid.append([squares[self.x][self.y+2], 7])
		if self.y == 6 and self.color == 0:
			if squares[self.x][self.y-2].piece == False:
				valid.append([squares[self.x][self.y-2], 7])
		
		#diagonal
		y = self.y + (-1 if self.color==0 else 1)
		if self.x<7:
			if squares[self.x+1][y].piece != False:
				if squares[self.x+1][y].piece.color != self.color:
					if y==0 or y==7:
						valid.append([squares[self.x+1][y], 5])
					else:
						valid.append([squares[self.x+1][y], 1])
		if self.x>0:
			if squares[self.x-1][y].piece != False:
				if squares[self.x-1][y].piece.color != self.color:
					if y==0 or y==7:
						valid.append([squares[self.x-1][y], 5])
					else:
						valid.append([squares[self.x-1][y], 1])
					
		#en passant
		if self.y == lastmove[1]:
			y = self.y + (-1 if self.color==0 else 1)
			if self.x+1 == lastmove[0]:
				valid.append([squares[self.x+1][y], 6])
			if self.x-1 == lastmove[0]:
				valid.append([squares[self.x-1][y], 6])
		
		return valid
		
		
		
