

class TeamRegistry():
	def __init__(self):
		self._registry = []

	@property
	def registry(self):
		return self._registry

	def addTeam(self, team):
		team.teamID = len(self._registry)
		self._registry.append(team)

	def printTeam(self):
		for team in self._registry:
			print(team)

	def search(self, keyword):
		output = []
		for team in self._registry:
			if keyword in team.teamName:
				output.append(team.teamName)
		return output