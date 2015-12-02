import sys
sys.path.insert(0, '.kleague')
from model import Model

class CLI:


	def __init__(self):
		print('cli init')
		self.model = Model()

	def run(self):
		print('cli run')
		inputString = input('Command? ')
		self.model.insert(inputString)
		self.model.update()