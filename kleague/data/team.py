

class Team():
	

	def __init__(self):
		self._teamID = None
		self._teamName = None

	def __str__(self):
		output = ''
		output += (
			str(self._teamID)
			+ ';' + str(self._teamName)
		)
		return output

	@property
	def teamID(self):
		return self._teamID

	@teamID.setter
	def teamID(self, teamID):
		self._teamID = teamID

	@property
	def teamName(self):
		return self._teamName

	@teamName.setter
	def teamName(self, teamName):
		self._teamName = teamName