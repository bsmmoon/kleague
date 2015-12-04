

class Role():


	def __init__(self):
		1+1



class Player(Role):

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


class Staff(Role):

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