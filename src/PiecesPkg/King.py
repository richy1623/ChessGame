import pygame

from PiecesPkg.Piece import Piece

class King(Piece):
	def __init__(self, x, y, size, color, piece):
		super().__init__(x,y,size,color,piece)
		self.code = "K"
		self.check = False
	
	def validmoves(self, squares):
		valid = []
		
		for x in [-1,0,1]:
			x2 = self.x+x
			for y in [-1,0,1]:
				if x!=0 or y!=0:
					y2 = self.y+y
					if x2>=0 and x2<=7 and y2>=0 and y2<=7:
						if squares[x2][y2].piece == False:
							valid.append([squares[x2][y2], 0])
						elif squares[x2][y2].piece.color != self.color:
							valid.append([squares[x2][y2], 1])
		
		if not (self.moved or self.check):
			if self.color == 1:
				if squares[0][0].piece != False and squares[0][0].piece.code=='R' and not squares[0][0].piece.moved and not any(squares[x][0].piece for x in [1,2,3]):
					valid.append([squares[2][0], 3])
				if squares[7][0].piece != False and squares[7][0].piece.code=='R' and not squares[7][0].piece.moved and not any(squares[x][0].piece for x in [5,6]):
					valid.append([squares[6][0], 2])
			if self.color == 0:
				if squares[0][7].piece != False and squares[0][7].piece.code=='R' and not squares[0][7].piece.moved and not any(squares[x][7].piece for x in [1,2,3]):
					valid.append([squares[2][7], 3])
				if squares[7][7].piece != False and squares[7][0].piece.code=='R' and not squares[7][7].piece.moved and not any(squares[x][7].piece for x in [5,6]):
					valid.append([squares[6][7], 2])
		return valid
