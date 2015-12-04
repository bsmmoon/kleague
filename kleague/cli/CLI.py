import sys
from kleague.model import Model
from kleague.view import View

class CLI:


	def __init__(self):
		print('cli init')
		self.model = Model()
		self.view = View(self.model)

	def run(self):
		print('cli run')
		while True:
			try:
				inputString = input('Your command? ')
				self.model.insert(inputString)
				self.view.update()
			except KeyError as detail:
				print(detail)