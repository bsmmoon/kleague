

class Demographic():


	def __init__(self):
		self._peopleList = []

	@property
	def peopleList(self):
		return self._peopleList

	def addPerson(self, person):
		person.personID = len(self._peopleList)
		self._peopleList.append(person)

	def printPeople(self):
		for person in self._peopleList:
			print(person)

	def search(self, keyword):
		output = []
		for person in self._peopleList:
			if keyword in person.personName:
				output.append(person.personName)
		return output

