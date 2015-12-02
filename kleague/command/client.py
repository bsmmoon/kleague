import sys
from kleague.command import Invoker

class Client():


	def __init__(self):
		print('client init')

	def insert(self, command):
		print('client insert')
		invoker = Invoker(command)
		invoker.execute()