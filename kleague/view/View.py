from kleague.model import Model

class View:


	def __init__(self, model):
		print('view init')
		self.model = model

	def update(self):
		self.model.update()
		
