import sys
sys.path.insert(0, '.kleague')
from data import Data

class Storage():


	def __init__(self):
		print('storage init')

	def load(self, data):
		print('storage load')
		data.setData()

	def save(self):
		print('storage save')