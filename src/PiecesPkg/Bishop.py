import pygame

from PiecesPkg.Piece import Piece

class Bishop(Piece):
	def __init__(self, x, y, size, color, piece):
		super().__init__(x,y,size,color,piece)
		self.code = "B"
	
	def validmoves(self, squares):
		valid = []
		yInc = True
		yDec = True
		for x in range(1, 8-self.x):
			x2 = self.x+x
			y2 = self.y+x
			if yInc and y2<8:
				if squares[x2][y2].piece == False:
					valid.append([squares[x2][y2], 0])
				else:
					if squares[x2][y2].piece.color != self.color:
						valid.append([squares[x2][y2], 1])
					yInc = False
			y2 = self.y-x
			if yDec and y2>=0:
				if squares[x2][y2].piece == False:
					valid.append([squares[x2][y2], 0])
				else:
					if squares[x2][y2].piece.color != self.color:
						valid.append([squares[x2][y2], 1])
					yDec = False
		yInc = True
		yDec = True
		for x in range(1,self.x+1):
			x2 = self.x-x
			y2 = self.y+x
			if yInc and y2<8:
				if squares[x2][y2].piece == False:
					valid.append([squares[x2][y2], 0])
				else:
					if squares[x2][y2].piece.color != self.color:
						valid.append([squares[x2][y2], 1])
					yInc = False
			y2 = self.y-x
			if yDec and y2>=0:
				if squares[x2][y2].piece == False:
					valid.append([squares[x2][y2], 0])
				else:
					if squares[x2][y2].piece.color != self.color:
						valid.append([squares[x2][y2], 1])
					yDec = False
		return valid
