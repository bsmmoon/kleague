from kleague.data.transfercentre import TransferCentre
from kleague.data.demographic import Demographic

class Data():


	def __init__(self):
		self._transferCentre = TransferCentre()
		self._demographic = Demographic()

	def setData(self):
		1+1

	def getData(self):
		1+1

	def addContract(self, contract):
		self._transferCentre.addContract(contract)

	def getContracts(self):
		return self._transferCentre.contracts

	def addPerson(self, person):
		self._demographic.addPerson(person)

	def getPeople(self):
		return self._demographic.peopleList