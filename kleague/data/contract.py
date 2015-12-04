

class Contract():


	def __init__(self):
		self._contractType = None
		self._person = None
		self._team = None

	@property
	def contractType(self):
		return self._contractType

	@contractType.setter
	def contractType(self, contractType):
		self._contractType = contractType

	@property
	def person(self):
		return self._person

	@person.setter
	def person(self, person):
		self._person = person

	@property
	def team(self):
		return self._team

	@team.setter
	def team(self, team):
		self._team = team


