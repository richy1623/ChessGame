import pygame

from PiecesPkg.Piece import Piece

class Queen(Piece):
	def __init__(self, x, y, size, color, piece):
		super().__init__(x,y,size,color,piece)
		self.code = "Q"
	
	def validmoves(self, squares):
		valid = []
		#diagonal
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
		#straight
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
