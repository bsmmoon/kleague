import sys
from kleague.model import Model

class CLI:


	def __init__(self):
		print('cli init')
		self.model = Model()

	def run(self):
		print('cli run')
		while True:
			inputString = input('Command? ')
			self.model.insert(inputString)
			self.model.update()