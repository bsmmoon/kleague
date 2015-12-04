from kleague.command.command import Command
from kleague.command.command import AddContract
from kleague.data.contract import Contract
from kleague.parser.tokenizer import Tokenizer
from kleague.parser.token import Token

EXIT = '0'
ADD_TRANSFER_WINDOW_COMMAND = '1'
ADD_PENDING_CONTRACT = '2'

class Parser():


	def __init__(self):
		self.tokenizer = Tokenizer()

	def parse(self, inputString):
		tokens = self.tokenizer.tokenize(inputString)
		
		command = Command()
		if tokens[0].value == EXIT:
			exit()
		elif tokens[0].value == ADD_TRANSFER_WINDOW_COMMAND:
			command = AddTransferWindow(TransferWindow())
		elif tokens[0].value == ADD_PENDING_CONTRACT:
			contract = self.parseContract(tokens)
			command = AddContract(contract)
		else:
			raise KeyError('unknown command')
		
		return command

	def parseContract(self, tokens):
		contract = Contract()
		contract.contractType = tokens[1]
		contract.person = tokens[2]
		contract.team = tokens[3]
		return contract