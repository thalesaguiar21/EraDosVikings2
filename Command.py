class Command(object):

	''' Classe que define um comando do jogo '''
	def __init__(self, firstWord, secondWord):
		self.firstWord = firstWord
		self.secondWord = secondWord

	def getFirstWord(self):
		return self.firstWord

	def getSecondWord(self):
		return self.secondWord

	def hasSecondWord(self):
		if self.secondWord == None
			return False
		return True