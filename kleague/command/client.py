import sys
from kleague.command import Invoker

class Client():
	def insert(self, command):
		invoker = Invoker(command)
		invoker.execute()