from kleague.data import Contract


class Command():


	def __init__(self):
		self.data = None

	def insertData(self, data):
		self.data = data


class AddContract(Command):


	def __init__(self, contract):
		self.contract = contract

	def execute(self):
		self.data.addContract(self.contract)

