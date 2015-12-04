

class Token():


	def __init__(self):
		self._value = None

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value

	def __str__(self):
		return self._value