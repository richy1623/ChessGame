import pygame

class RenderQueue:
	def __init__(self):
		self.queue = []
		
	def add(self, item):
		self.queue.append(item)
			
	def render(self, screen):
		change = False
		for i in self.queue:
			i.render(screen)
			change = True
		self.queue = []
		return change
