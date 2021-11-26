import pygame

from PiecesPkg.Piece import Piece

class Rook(Piece):
	def __init__(self, x, y, size, color, piece):
		super().__init__(x,y,size,color,piece)
		self.code = "R"
	
	def validmoves(self, squares):
		valid = []
		
		for x in range(self.x+1, 8):
			if squares[x][self.y].piece == False:
				valid.append([squares[x][self.y], 0])
			else:
				if squares[x][self.y].piece.color != self.color:
					valid.append([squares[x][self.y], 1])
				break
		for x in range(self.x-1, -1, -1):
			if squares[x][self.y].piece == False:
				valid.append([squares[x][self.y], 0])
			else:
				if squares[x][self.y].piece.color != self.color:
					valid.append([squares[x][self.y], 1])
				break
		for y in range(self.y+1, 8):
			if squares[self.x][y].piece == False:
				valid.append([squares[self.x][y], 0])
			else:
				if squares[self.x][y].piece.color != self.color:
					valid.append([squares[self.x][y], 1])
				break
		for y in range(self.y-1, -1, -1):
			if squares[self.x][y].piece == False:
				valid.append([squares[self.x][y], 0])
			else:
				if squares[self.x][y].piece.color != self.color:
					valid.append([squares[self.x][y], 1])
				break
		
		return valid
