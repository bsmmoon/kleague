

class Person():


	def __init__(self):
		self._personID = None
		self._personName = None
		self._role = None

	def __str__(self):
		output = ''
		output += (
			str(self._personID)
			+ ';' + str(self._personName)
			+ ';' + str(self._role)
		)
		return output

	@property
	def personName(self):
		return self._personName

	@personName.setter
	def personName(self, personName):
		self._personName = personName

	@property
	def personID(self):
		return self._personID

	@personID.setter
	def personID(self, personID):
		self._personID = personID

	@property
	def role(self):
		return self._role

	@role.setter
	def role(self, role):
		self._role = role