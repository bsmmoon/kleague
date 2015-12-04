

class Contract():


	def __init__(self):
		print('Contract init')
		self.person = None
		self.team = None

	def getPerson(self):
		return self.person

	def getTeam(self):
		return self.team

	def setPerson(self, person):
		print('Contract setPerson')
		self.person = person

	def setTeam(self, team):
		print('Contract setTeam')
		self.team = team


