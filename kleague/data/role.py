class Player():
	def __init__(self):
		self._team = None

	def __str__(self):
		output = ''
		output += (
			'player'
		)
		return output

	@property
	def team(self):
		return self._team

	@team.setter
	def team(self, team):
		self._team = team


class Staff():
	def __init__(self):
		self._team = None

	def __str__(self):
		output = ''
		output += (
			'staff'
		)
		return output

	@property
	def team(self):
		return self._team

	@team.setter
	def team(self, team):
		self._team = team