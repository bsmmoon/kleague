import sys
sys.path.insert(0, '.kleague')
from logic import Logic

class Model:


	def __init__(self):
		print('model init')
		self.logic = Logic()

	def insert(self, command):
		print('model insert ({})'.format(command))
		self.logic.insert(command)

	def update(self):
		print('model update')
