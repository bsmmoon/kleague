import sys
from kleague.data import Data

class Storage():


	def __init__(self, data):
		self.data = data

	def load(self):
		self.data.setData()

	def save(self):
		self.data.getData()
