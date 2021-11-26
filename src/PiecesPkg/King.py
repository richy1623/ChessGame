import pygame

from PiecesPkg.Piece import Piece

class King(Piece):
	def __init__(self, x, y, size, color, piece):
		super().__init__(x,y,size,color,piece)
		self.code = "K"
	
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
		
		return valid
