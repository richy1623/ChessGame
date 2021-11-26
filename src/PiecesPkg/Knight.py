import pygame

from PiecesPkg.Piece import Piece

class Knight(Piece):
	def __init__(self, x, y, size, color, piece):
		super().__init__(x,y,size,color,piece)
		self.code = "N"
	
	def validmoves(self, squares):
		valid = []
		shift = [-2,-1,0,1,2]
		for x in [0,1,3,4]:
			x2 = self.x+shift[x]
			for y in [0,1,3,4]:
				if (x+y)%2==1:
					y2 = self.y+shift[y]
					if x2>=0 and x2<=7 and y2>=0 and y2<=7:
						if squares[x2][y2].piece == False:
							valid.append([squares[x2][y2], 0])
						elif squares[x2][y2].piece.color != self.color:
							valid.append([squares[x2][y2], 1])
		return valid
		
		
		
