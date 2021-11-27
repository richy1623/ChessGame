class Log:
	def __init__(self):
		self.moves = []
	
	def move(self, piece, oldsquare, newsquare, action, check):
		self.moves.append([piece, oldsquare, newsquare, action, check])
		print(self.formatmove(len(self.moves)-1), end = ("" if piece.color == 0 else "\n"))
			
	def formatmove(self, index):
		if self.moves[index][3]==1:		#take
			move = self.moves[index][0].code+"x"+self.moves[index][2].getnotation()
		elif self.moves[index][3]==2:	#castle K
			move =  "0-0"
		elif self.moves[index][3]==3:	#castle Q
			move =  "0-0-0"
		elif self.moves[index][3]==5:	#take promote
			move =  "x"+self.moves[index][2].getnotation()+"=Q"
		elif self.moves[index][3]==4:	#move promote
			move =  self.moves[index][2].getnotation()+"=Q"
		elif self.moves[index][3]==6:	#en passant
			move =  self.moves[index][1].getnotation()+"x"+self.moves[index][2].getnotation()+" ep."
		else:							#normal move
			move =  self.moves[index][0].code+self.moves[index][2].getnotation()
		if self.moves[index][4]:		#check
			move += "+"
		return f'{move:<12}'
