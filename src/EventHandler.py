import pygame

class EventHandler:
	def __init__(self, renderqueue, board):
		self.rq = renderqueue
		self.board = board
		
		
	def click(self, pos):
		if self.board.rect.collidepoint(pos):
			self.board.click(pos, self.rq)
