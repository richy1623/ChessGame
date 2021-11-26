class Log:
	def __init__(self):
		self.moves = []
	
	def move(self, piece, oldsquare, newsquare, action):
		action = "x" if action==1 else ""
		self.moves.append([piece, oldsquare, newsquare, action])
		print(self.formatmove(len(self.moves)-1)+"\t", end = ("" if piece.color == 0 else "\n"))
			
	def formatmove(self, index):
		return self.moves[index][0].code+self.moves[index][3]+self.moves[index][2].getnotation()
