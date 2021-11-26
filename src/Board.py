import pygame

from Square import Square
from PiecesPkg.Pieces import Pieces
from PiecesPkg.Pawn import Pawn
from PiecesPkg.Knight import Knight
from PiecesPkg.Bishop import Bishop
from PiecesPkg.Rook import Rook
from PiecesPkg.Queen import Queen
from PiecesPkg.King import King

class Board:
	def __init__(self, x, y, screensize):
		self.reverse = False
		self.size = int(screensize/8)
		self.rect = pygame.Rect(x, y, screensize, screensize)
		self.selected = False
		self.setboard()
		self.validmoves = []
		self.freemove = False
		
	def setboard(self):
		pieces = Pieces(self.size)
		self.squares = [[Square(self.size, x, y) for y in range(8)] for x in range(8)]
		#init pawns
		for i in range(8):
			self.squares[i][1].addPiece(Pawn(i, 1, self.size, 1, pieces.pawnb))
			self.squares[i][6].addPiece(Pawn(i, 6, self.size, 0, pieces.pawnw))
		#init Knights
		self.squares[1][0].addPiece(Knight(1, 0, self.size, 1, pieces.knightb))
		self.squares[6][0].addPiece(Knight(6, 0, self.size, 1, pieces.knightb))
		self.squares[1][7].addPiece(Knight(1, 7, self.size, 0, pieces.knightw))
		self.squares[6][7].addPiece(Knight(6, 7, self.size, 0, pieces.knightw))
		#init Bishops
		self.squares[2][0].addPiece(Bishop(2, 0, self.size, 1, pieces.bishopb))
		self.squares[5][0].addPiece(Bishop(5, 0, self.size, 1, pieces.bishopb))
		self.squares[2][7].addPiece(Bishop(2, 7, self.size, 0, pieces.bishopw))
		self.squares[5][7].addPiece(Bishop(5, 7, self.size, 0, pieces.bishopw))
		#init Rooks
		self.squares[0][0].addPiece(Rook(0, 0, self.size, 1, pieces.rookb))
		self.squares[7][0].addPiece(Rook(7, 0, self.size, 1, pieces.rookb))
		self.squares[0][7].addPiece(Rook(0, 7, self.size, 0, pieces.rookw))
		self.squares[7][7].addPiece(Rook(7, 7, self.size, 0, pieces.rookw))
		#init Queens
		self.squares[3][0].addPiece(Queen(3, 0, self.size, 1, pieces.queenb))
		self.squares[3][7].addPiece(Queen(3, 7, self.size, 0, pieces.queenw))
		#init Kings
		self.squares[4][0].addPiece(King(4, 0, self.size, 1, pieces.kingb))
		self.squares[4][7].addPiece(King(4, 7, self.size, 0, pieces.kingw))
		
	def click(self, pos, eventhandler):
		#if self.selected != '': self.selected.click() 
		x = int((pos[0] - self.rect.x)/self.size)
		y = int((pos[1] - self.rect.y)/self.size)
		if self.selected == False:
			if self.squares[x][y].piece != False:
				self.selected = self.squares[x][y]
				self.selected.recolor(5)
				self.validmoves = self.selected.piece.validmoves(self.squares)
				for i in self.validmoves:
					i[0].recolor(3)
					eventhandler.torender(i[0])
				eventhandler.torender(self.selected)
		else:
			if self.selected is not self.squares[x][y]:
				if  self.freemove:
					eventhandler.logmove(self.selected.piece, self.selected, self.squares[x][y], 0)
					self.selected.movePiece(self.squares[x][y])
					eventhandler.torender(self.squares[x][y])
				else:
					for valid in self.validmoves:
						if self.squares[x][y] == valid[0]: 
							eventhandler.logmove(self.selected.piece, self.selected, self.squares[x][y], valid[1])
							self.selected.movePiece(self.squares[x][y])
							eventhandler.torender(self.squares[x][y])
							break
			eventhandler.torender(self.selected)
			for i in self.validmoves:
				i[0].resetcolor()
				eventhandler.torender(i[0])
			self.selected.resetcolor()
			eventhandler.torender(self.selected)
			self.validmoves = []
			self.selected = False
			
	def render(self, screen):
		for x in range(8):
			for y in range(8) if not self.reverse else range(7,-1,-1):
				 self.squares[x][y].render(screen)
		
