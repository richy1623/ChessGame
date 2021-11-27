import pygame

class EventHandler:
	def __init__(self, renderqueue, board, log):
		self.rq = renderqueue
		self.board = board
		self.log = log
		
		
	def click(self, pos):
		if self.board.rect.collidepoint(pos):
			self.board.click(pos, self)
		
	def torender(self, item):
		self.rq.add(item)
		
	def logmove(self, piece, oldsquare, newsquare, action):
		self.log.move(piece, oldsquare, newsquare, action, False)
		
	def addAnimation(self, item):
		pass
