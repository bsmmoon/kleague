

class Invoker():


	def __init__(self, command):
		print('invoker init ({})'.format(command))
		self.command = command

	def execute(self):
		print('invoker execute ({})'.format(self.command))
		self.command.execute()