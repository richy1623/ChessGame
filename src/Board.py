import pygame

from Square import Square
from PiecesPkg.Pieces import Pieces
from PiecesPkg.Pawn import Pawn

class Board:
	def __init__(self, x, y, screensize):
		self.reverse = False
		self.size = int(screensize/8)
		self.rect = pygame.Rect(x, y, screensize, screensize)
		self.selected = False
		
		pieces = Pieces(self.size)
		self.squares = [[Square(self.size, x, y) for y in range(8)] for x in range(8)]
		#init pawns
		for i in range(8):
			self.squares[i][1].addPiece(Pawn(i, 1, self.size, 1, pieces.pawnb))
			self.squares[i][6].addPiece(Pawn(i, 6, self.size, 0, pieces.pawnw))
		#init Knights
		self.squares[1][0].addPiece(Pawn(1, 0, self.size, 1, pieces.knightb))
		self.squares[6][0].addPiece(Pawn(6, 0, self.size, 1, pieces.knightb))
		self.squares[1][7].addPiece(Pawn(1, 7, self.size, 1, pieces.knightw))
		self.squares[6][7].addPiece(Pawn(6, 7, self.size, 1, pieces.knightw))
		#init Bishops
		self.squares[2][0].addPiece(Pawn(2, 0, self.size, 1, pieces.bishopb))
		self.squares[5][0].addPiece(Pawn(5, 0, self.size, 1, pieces.bishopb))
		self.squares[2][7].addPiece(Pawn(2, 7, self.size, 1, pieces.bishopw))
		self.squares[5][7].addPiece(Pawn(5, 7, self.size, 1, pieces.bishopw))
		#init Rooks
		self.squares[0][0].addPiece(Pawn(0, 0, self.size, 1, pieces.rookb))
		self.squares[7][0].addPiece(Pawn(7, 0, self.size, 1, pieces.rookb))
		self.squares[0][7].addPiece(Pawn(0, 7, self.size, 1, pieces.rookw))
		self.squares[7][7].addPiece(Pawn(7, 7, self.size, 1, pieces.rookw))
		#init Queens
		self.squares[3][0].addPiece(Pawn(3, 0, self.size, 1, pieces.queenb))
		self.squares[3][7].addPiece(Pawn(3, 7, self.size, 1, pieces.queenw))
		#init Kings
		self.squares[4][0].addPiece(Pawn(4, 0, self.size, 0, pieces.kingb))
		self.squares[4][7].addPiece(Pawn(4, 7, self.size, 0, pieces.kingw))
		
	def click(self, pos, rq):
		#if self.selected != '': self.selected.click() 
		x = int((pos[0] - self.rect.x)/self.size)
		y = int((pos[1] - self.rect.y)/self.size)
		if self.selected == False:
			if self.squares[x][y].piece != False:
				self.selected = self.squares[x][y]
				self.selected.click()
				rq.add(self.selected)
		else:
			if self.selected is self.squares[x][y]:
				rq.add(self.selected)
			else:
				#TODO: check valid
				self.selected.movePiece(self.squares[x][y])
				rq.add(self.selected)
				rq.add(self.squares[x][y])
			self.selected.click()
			self.selected = False
		return
	def render(self, screen):
		for x in range(8):
			for y in range(8) if not self.reverse else range(7,-1,-1):
				 self.squares[x][y].render(screen)
		
