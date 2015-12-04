import sys
from data import Data

class Storage():


	def __init__(self, data):
		print('storage init')
		self.data = data

	def load(self):
		print('storage load')
		self.data.setData()

	def save(self):
		print('storage save')
		self.data.getData()
