from kleague.command.command import Command
from kleague.command.command import AddTransferWindow
from kleague.data.transferwindow import TransferWindow
from kleague.parser.tokenizer import Tokenizer
from kleague.parser.token import Token

ADD_TRANSFER_WINDOW_COMMAND = 'AddTransferWindow'

class Parser():


	def __init__(self):
		print('parser init')
		self.tokenizer = Tokenizer()

	def parse(self, inputString):
		print('command object')
		tokens = self.tokenizer.tokenize(inputString)
		
		command = Command()
		if tokens[0] is ADD_TRANSFER_WINDOW_COMMAND:
			command = AddTransferWindow(TransferWindow())
		
		return command