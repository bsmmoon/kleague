from kleague.command.command import Command
from kleague.command.command import AddContract
from kleague.command.command import AddPerson
from kleague.data.contract import Contract
from kleague.data.person import Person
from kleague.data.role import Player
from kleague.data.role import Staff
from kleague.parser.tokenizer import Tokenizer
from kleague.parser.token import Token

EXIT = '0'
ADD_PENDING_CONTRACT = '1'
ADD_PERSON = '2'

class Parser():


	def __init__(self):
		self.tokenizer = Tokenizer()

	def parse(self, inputString):
		tokens = self.tokenizer.tokenize(inputString)
		
		command = Command()
		if tokens[0].value == EXIT:
			exit()
		elif tokens[0].value == ADD_PENDING_CONTRACT:
			parserdObject = self.parseContract(tokens)
			command = AddContract(parserdObject)
		elif tokens[0].value == ADD_PERSON:
			parserdObject = self.parsePerson(tokens)
			command = AddPerson(parserdObject)
		else:
			raise KeyError('unknown command')
		
		return command

	def parseContract(self, tokens):
		contract = Contract()
		contract.contractType = tokens[1]
		contract.person = tokens[2]
		contract.team = tokens[3]
		return contract

	def parsePerson(self, tokens):
		person = Person()
		person.name = tokens[1].value

		if tokens[2].value == 'player':
			person.role = Player()
		elif tokens[2].value == 'staff':
			person.role = Staff()
		else:
			raise KeyError('unknown role')

		return person
