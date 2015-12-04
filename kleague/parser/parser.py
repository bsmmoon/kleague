from command import Command
from command import AddTransferCentre
from ..data.transfercentre import TransferCentre

class Parser():


	def __init__(self):
		print('parser init')

	def parse(self, inputString):
		print('command object')

		return AddTransferCentre(TransferCentre())