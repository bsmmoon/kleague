from kleague.data import Contract


class Command():
	def __init__(self):
		self._data = None

	def insertData(self, data):
		self._data = data


class AddContract(Command):
	def __init__(self, contract):
		self._data = None
		self._contract = contract

	def execute(self):
		self._data.addContract(self._contract)


class AddPerson(Command):
	def __init__(self, person):
		self._data = None
		self._person = person

	def execute(self):
		self._data.addPerson(self._person)


class AddTeam(Command):
	def __init__(self, team):
		self._data = None
		self._team = team

	def execute(self):
		self._data.addTeam(self._team)

