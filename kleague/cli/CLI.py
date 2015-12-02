import sys
sys.path.insert(0, '.kleague')
from model.Model import Model

class CLI:


	def __init__(self):
		print('cli init')
		self.model = Model()

	def run(self):
		print('cli run')
		command = input('Command? ')
		self.model.insert(command)
		self.model.update()