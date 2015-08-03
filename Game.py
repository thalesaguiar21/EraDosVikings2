from CommandIdentifier import *
from Command import *
from CommandList import *

class Game(object):

	def __init__(self):
		self.commandId = CommandIdentifier()
		self.rooms = []
		self.createWorld()
		self.actualRoom = rooms[0]
		self.lastRoom = room[0]

	def createWorld(self):
		pass

	def printLogo(self):
		print("  _      __     _    _")
        print(" | |    / / _  | |  / / _   _   _   _____     ______")
        print(" | |   / / | | | | / / | | | \ | | |  _  |   /  ____|")
        print(" | |  / /  | | | |/ /  | | |  \| | | |_| |  /  /__")
        print(" | | / /   | | |   /   | | |     | |___  |  \___  \ ")
        print(" | |/ /    | | |   \   | | |     |     | |      \  \ ")
        print(" |   /     | | | |\ \  | | | |\  |  ___| |  ____/  /")
        print(" |__/      |_| |_| \_\ |_| |_| \_| |_____| |______/ ") 
        print("") 

	def printTutorial(self):
		pass

	def printWelcome(self):
		printLogo()
		printTutorial()
		print(self.actualRoom.getFullDescription() + '\n')

	def selectCommand(self, command):
		if(command.getFirstWord() == 'ir'):
			executarIr(command)
		elif(command.getFirstWord() == 'pegar'):
			pass
		elif(command.getFirstWord() == 'olhar'):
			executarOlhar(command)
			

		

	def play():
		pass