

class Person():


	def __init__(self):
		self._personID = None
		self._name = None
		self._role = None

	def __str__(self):
		output = ''
		output += (
			str(self._personID)
			+ ';' + str(self._name)
			+ ';' + str(self._role)
		)
		return output

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

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