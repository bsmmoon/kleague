from kleague.data.transfercentre import TransferCentre
from kleague.data.demographic import Demographic
from kleague.data.teamregistry import TeamRegistry

class Data():


	def __init__(self):
		self._transferCentre = TransferCentre()
		self._demographic = Demographic()
		self._teamRegistry = TeamRegistry()

		self._searchResult = None

	@property
	def searchResult(self):
		return self._searchResult

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

	def searchPerson(self, keyword):
		self._searchResult = self._demographic.search(keyword)

	def addTeam(self, team):
		self._teamRegistry.addTeam(team)

	def getTeams(self):
		return self._teamRegistry.registry

	def searchTeam(self, keyword):
		self._searchResult = self._teamRegistry.search(keyword)